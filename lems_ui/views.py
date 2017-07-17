import os
import time
import collections
import datetime
import logging

import json
from lxml import html, etree
from StringIO import StringIO

from lems_ui.models import LemsElement, LemsTypeTag
from lems_ui.models import LemsModel, ParameterisedModel
from lems_ui.models import Lems2FpgaJob, MODEL_TYPES, all_available_models

from lems.model import model, component, dynamics
from lems.parser import LEMS

from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from utils import model_json_to_lems_xml,component_json_to_lems_xml
from jobExecution import runCheck

from article_utils import create_article

LOG = logging.getLogger(__name__)

LEMS_ELEMENTS = ['component_types', 'components', 'dimensions', 'units']

def home(rq):
    return render(rq,
                  'lems_ui/home.html',
                  {'user':rq.user})

def network_model(rq, model_name=None):
    return comp_type_view(rq, model_name, top_tag='Network')

def synapse_model(rq, model_name=None):
    return comp_type_view(rq, model_name, top_tag='Synapse')

@login_required
def delete_neuron_model(rq, model_name=None):
    try:
        # user can only delete models they own
        model = LemsModel.objects.get(name=model_name,
                              owner__username = rq.user)
        model.delete()
    except:
        model = None

    return redirect('/booking/view_NeuronModels')


@login_required
def comp_type_view(rq, model_name=None, top_tag='Cell'):
    comp_type_names = LemsElement.objects.\
            filter(lems_elem='component_types').\
            values_list('name', flat=True)

    tags = LemsTypeTag.objects.all()

    LOG.debug(comp_type_names)

    synapses = all_available_models(rq.user, MODEL_TYPES.SYN)

    return render(rq,
                  'lems_ui/comp_type_view.html',
          {'elements':comp_type_names, 'tags':tags, 'synapses' : synapses,
           'open_model': model_name, 'top_tag':top_tag})


# add dict of lists e.g. children, comp refs etc.. to another dict of lists
def add_sub_comps(total_sub_comps, new_sub_comps):
    for key in total_sub_comps.keys():
        if new_sub_comps.has_key(key):
            total_sub_comps[key].update(new_sub_comps[key])

    return total_sub_comps

def comp_details(rq):
    comp_obj = LemsElement.objects.get(name=rq.GET['name'],
                                       lems_elem='component_types')

    comp_lxml_obj = etree.parse(StringIO(comp_obj.xml)).getroot()
    response = get_sub_comps(comp_lxml_obj)

    hier = get_lxml_hierarchy(rq.GET['name'])
    for comp in hier:
        subs = get_sub_comps(comp)
        response = add_sub_comps(response, subs)

    if comp_obj.lems_elem!='components':
        response['params'] = get_params(comp_lxml_obj)
    response['xml'] = comp_obj.xml
    response['description'] = comp_obj.description
    response['dynamics_text'] = comp_obj.dynamics_text
    response['tags'] = []
    for tag in comp_obj.tags.all():
        response['tags'].append(tag.tag)

    return HttpResponse(json.dumps(response))


def component_hierarchy(rq):
    comp_obj = LemsElement.objects.get(name=rq.GET['name'])
    response = {}
    xml = comp_obj.xml
    response['xml'] = xml
    response['hierarchy'] = comp_obj.component_data
    return HttpResponse(json.dumps(response))


def get_params(comp_lxml_obj):
    params = collections.OrderedDict()

    hierarchy = get_lxml_hierarchy(comp_lxml_obj.get('name'))

    units = LemsElement.objects.filter(lems_elem='units')

    for obj in hierarchy:
        for sub_elem in obj.getchildren():
            if sub_elem.tag == 'Parameter':
                param_unit = None

                if sub_elem.get('dimension') == 'none':
                    params[sub_elem.get('name')] = []
                    continue

                param_unit = []
                for unit in units:
                    if unit.xml.find('dimension = "' +
                                 sub_elem.get('dimension') + '"') > 0:
                        param_unit.append(unit)

                params[sub_elem.get('name')] = []
                for this_unit in param_unit:
                    unit_lxml_obj = etree.parse(StringIO(this_unit.xml)).getroot()
                    params[sub_elem.get('name')].append( {
                        'symbol' : unit_lxml_obj.get('symbol'),
                        'power' : unit_lxml_obj.get('power')
                    })

    return params

def get_sub_comps(comp_lxml_obj):
    child_list = {}
    children_list = {}
    comp_ref_list = {}
    attachments_list = {}
    path_list = {}

    for sub_elem in comp_lxml_obj.getchildren():
        if sub_elem.tag == 'Child':
            child_list[sub_elem.get('name')] = sub_elem.get('type')
        elif sub_elem.tag == 'Children':
            children_list[sub_elem.get('name')] = sub_elem.get('type')
        elif sub_elem.tag == 'ComponentReference':
            comp_ref_list[sub_elem.get('name')] = sub_elem.get('type')
        elif sub_elem.tag == 'Attachments':
            attachments_list[sub_elem.get('name')] = sub_elem.get('type')
        elif sub_elem.tag == 'Path':
            path_list[sub_elem.get('name')] = sub_elem.get('type')

    # NOTE: these 'lists' are actually dicts
    return {'child_list': child_list,
            'children_list': children_list,
            'comp_ref_list': comp_ref_list,
            'attachments_list': attachments_list,
            'path_list': path_list}

def get_descendants(rq):
    root_name = rq.GET['name']

    comp_list = descendants(root_name, [root_name])

    return HttpResponse(json.dumps(comp_list))

def get_descendantscomponents(rq):
    root_name = rq.GET['name']

    comp_list = descendants_components(root_name, [root_name],[])

    return HttpResponse(json.dumps(comp_list))



# recursively called to get a list of all descendants
def descendants(comp_type, desc_list):
    comp_objs = LemsElement.objects.\
                        filter(lems_elem='component_types').\
                        filter(extends=comp_type)

    for comp in  comp_objs:
        desc_list.append(comp.name)
        new_list = descendants(comp.name, desc_list)

    return desc_list

# recursively called to get a list of all descendants
def descendants_components(comp_type, desc_list,desc_list_ret):
    comp_objs = LemsElement.objects.\
                        filter(Q(lems_elem='component_types') | Q(lems_elem='components')).\
                        filter(extends=comp_type)

    for comp in  comp_objs:
        if comp.lems_elem == 'components' :
            desc_list_ret.append(comp.name)
        desc_list.append(comp.name)
        new_list = descendants_components(comp.name, desc_list,desc_list_ret)

    return desc_list_ret


# Return a list of elements associated with optional tag name
# if no tag name is present then all items are returned
def element_list(rq):
    comp_type_names = []
    if rq.GET.has_key('tag') and rq.GET['tag']:
        tag = rq.GET['tag']
        comp_type_names = LemsElement.objects.\
            filter(Q(public=True)).\
            filter(Q(lems_elem='component_types') | Q(lems_elem='components')).\
            filter(tags__tag=tag).\
            values_list('name', flat=True)
    else:
        comp_type_names = LemsElement.objects.\
            filter(Q(public=True)).\
            filter(Q(lems_elem='component_types') | Q(lems_elem='components')).\
            values_list('name', flat=True)

    names = []
    all_tags = []
    for name in comp_type_names:
        comp_obj = LemsElement.objects.\
            filter(Q(public=True)).\
            filter(Q(lems_elem='component_types') | Q(lems_elem='components')).\
            filter(name=name)

        tags = []
        if len(comp_obj) > 0:
            for tag in comp_obj[0].tags.all():
                tags.append(tag.tag)

        names.append(name)
        all_tags.append(tags)

    return HttpResponse(json.dumps([names, all_tags]))

# Return a list of elements associated with optional tag name
# if no tag name is present then all items are returned
def element_list_custom(rq):
    comp_type_names = []
    if rq.GET.has_key('tag') and rq.GET['tag']:
        tag = rq.GET['tag']
        comp_type_names = LemsElement.objects.\
            filter(Q(owner=rq.user)).\
            filter(Q(public=False)).\
            filter(Q(lems_elem='component_types') | Q(lems_elem='components')).\
            filter(tags__tag=tag).\
            values_list('name', flat=True)
    else:
        comp_type_names = LemsElement.objects.\
            filter(Q(owner=rq.user)).\
            filter(Q(public=False)).\
            filter(Q(lems_elem='component_types') | Q(lems_elem='components')).\
            values_list('name', flat=True)

    names = []
    all_tags = []
    for name in comp_type_names:
        comp_obj = LemsElement.objects.\
            filter(Q(owner=rq.user)).\
            filter(Q(lems_elem='component_types') | Q(lems_elem='components')).\
            filter(name=name)

        tags = []
        if len(comp_obj) > 0:
            for tag in comp_obj[0].tags.all():
                tags.append(tag.tag)

        names.append(name)
        all_tags.append(tags)

    names = sorted(names, key=lambda s: s.lower())
    return HttpResponse(json.dumps([names, all_tags]))


def get_lxml_hierarchy(comp_name):
    results = []
    while 1:
        # get the element
        try:
            comp_type = LemsElement.objects.get(name=comp_name,
                                                lems_elem='component_types')
        except:
            break

        comp_type_obj = etree.parse(StringIO(comp_type.xml)).getroot()

        results.append(comp_type_obj)

        if not comp_type_obj.get('extends'):
            break

        comp_name = comp_type_obj.get('extends')

    return results


# Given a component type name, get a dict representing it's hierarchy
def type_hierarchy(rq):
    curr_name = rq.GET['name']

    hierarchy = get_lxml_hierarchy(curr_name)
    results = []

    for elem in hierarchy:
        results.append(elem.get('name'))

    return HttpResponse(json.dumps(results))


def load_file(rq):
    if rq.method == 'POST':
        LOG.debug(str(rq.FILES['file_uploaded'].name))
        LOG.debug('file posted: ' + str(dir(rq.FILES['file_uploaded'])))

        inmem_file = rq.FILES['file_uploaded']
        saved_name = str(time.time()) + '.' + inmem_file.name

        f = open('uploads/' + saved_name, 'w')
        f.write(inmem_file.read())
        f.close()

        saved_elems = save_lems_model(rq.user, saved_name)

        return HttpResponse("File Added<br>" +
                            str(saved_elems))
    else:
        return render(rq,
                      'lems_ui/file_upload.html',
                      {'dest':reverse('lems_ui.views.load_file')})


def login_user(rq):
    try:
        username = rq.POST['username']
        password = rq.POST['password']
    except:
        return redirect('/')
    user = authenticate(username=username, password=password)
    if user:
        if user.is_active:
            login(rq,user)
            try:
                return redirect(rq.META['HTTP_REFERER'])
            except Exception as e:
                LOG.error("Login error: " + str(e))
                return redirect('/djlems/')
    else:
        messages.add_message(rq, messages.ERROR,
                             "Login Failed, Invalid username or password" )
        return redirect('/djlems/')


def logout_user(rq):
    logout(rq)
    return redirect('/djlems/')


@login_required
def model_list(rq):
    model_type = MODEL_TYPES.NEURON

    LOG.debug('top_tag: ' + str(rq.GET.has_key('top_tag')))

    if rq.GET.has_key('top_tag') and rq.GET['top_tag'] == 'Synapse':
        model_type = MODEL_TYPES.SYN
    elif rq.GET.has_key('top_tag') and rq.GET['top_tag'] == 'Network':
        model_type = MODEL_TYPES.NET

    LOG.debug('model_type: ' + str(model_type))

    models = all_available_models(rq.user, model_type)

    retval = []

    for model in models:
        retval.append(
            {'name': model.name,
             #'description': model.description,
             'owner': model.owner.username,
             'id': model.id,
             'public': model.public
        })

    return HttpResponse(json.dumps(retval))


def save_lems_model(user, lems_filename):
    retval = []

    m = model.Model(include_includes=False)
    m.import_from_file('uploads/' + lems_filename)

    for elem_name in LEMS_ELEMENTS:
        elems = getattr(m, elem_name)

        for elem in elems:
            db_elem = LemsElement()
            db_elem.name = elem.name
            db_elem.lems_elem = elem_name
            db_elem.description = elem.description
            db_elem.owner = user
            # public stays at default
            db_elem.xml = elem.toxml()
            db_elem.from_file = lems_filename

            try:
                db_elem.extends = elem.extends
            except:
                pass

            db_elem.save()

            retval.append(elem_name + ' : ' + elem.name)

    return retval




def get_model(rq):
    model_name = rq.GET['model_name']

    if(model_name.find(':') > 0):
        user_name = model_name.split(':')[-1]
        model_name = model_name.split(':')[0]
    else:
        user_name = rq.user.username

    try:
        model = LemsModel.objects.get(name=model_name,
                                      owner__username=user_name)
    except:
        model = None

    # this should not be reached, the username should always be appended
    # to the model name separated by :
    # IF no username is appended AND the current user doesn't have a model
    # with this name, then we'll look for a public model with this name
    if not model:
        try:
            model = LemsModel.objects.get(name=model_name,
                                          public=True)
        except:
            model = None

    if not model:
        LOG.error('No model found: ' + model_name)
        response = json.dumps({'error':'No model found ' + model_name})
    else:
        response = json.loads(model.json)
        response['model_desc'] = model.description
        response['model_public'] = model.public
        response = json.dumps(response)

    return HttpResponse(response)


# For now don't use CSRF as it makes ajax posts awkward
@csrf_exempt
def save_model(rq):
    post_data = rq.POST['msg']
    data = json.loads(post_data)
    LOG.debug('SAVING MODEL: ' + data['model_name'])
    data['model_name'] = data['model_name'].split(':')[0]
    try:
        # if THIS user has a model with this name then it'll get overwritten
        # otherwise a new model will be created, owned by this user
        model = LemsModel.objects.get(name=data['model_name'], owner=rq.user)

    except:
        model = LemsModel()
        model.owner = rq.user
        model.name = data['model_name']

        if data['top_tag'] == 'Synapse':
            model.model_type=MODEL_TYPES.SYN
        if data['top_tag'] == 'Network':
            model.model_type=MODEL_TYPES.NET

    model.description = data['model_description']
    model.public = data['model_public']
    model.json = post_data
    model.save()

    # mark all previous job results as out of date
    # TODO decide if we want to delete these jobs
    jobs = Lems2FpgaJob.objects.filter(lems_model=model)
    for job in jobs:
        job.out_of_date = True
        job.save()

    try:
        param_model = ParameterisedModel.objects.get(model=model)
    except:
        param_model = ParameterisedModel()

    param_model.model = model
    param_model.json_data = json.dumps(data['param_data'])
    param_model.save()
    article_msg = "not a neuron model";
    if model.model_type == MODEL_TYPES.NEURON:
        synId = rq.POST['synId']
        article_msg = create_article(rq, model,synId)

    return HttpResponse(json.dumps(
            {'message': 'Model: ' + model.name + ' saved ok : ' + article_msg,
             'model_id' : model.pk}))


def save_component_to_lems_xml(rq):
    model_name = rq.GET['model_name']
    prefab_name = rq.GET['prefab_name']
    description = rq.GET['description']
    component_id = rq.GET['component_id']
    tag_name = rq.GET['tag']

    tags = LemsTypeTag.objects.all()

    try:
        user_name = rq.GET['user_name']
    except:
        user_name = rq.user.username

    model_list = model_name.split(':')
    if len(model_list) > 1:
        user_name = model_name.split(':')[1]
        model_name = model_name.split(':')[0]

    model = None
    try:
        model = LemsModel.objects.get(name=model_name,
                              owner__username = user_name)
    except:
        LOG.error('No model found for user: ' + model_name)
        response = '<?xml version="1.0" encoding="utf-8"?>\n'
        response += '<error>Error finding requested model, try saving</error>'

    if model:
        response = component_json_to_lems_xml(model.json,component_id)
        db_elem = LemsElement()
        db_elem.name = prefab_name
        db_elem.lems_elem = 'components'
        db_elem.description = description
        db_elem.owner = rq.user
        db_elem.extends = response['components'][response['components'].keys()[0]]['type']
        # public stays at default
        db_elem.xml = response['xml']
        db_elem.component_data = json.dumps(response['components'])
        db_elem.from_file = 'GUI Created'
        db_elem.save()
        for tag in tags:
            if tag.tag == tag_name:
                db_elem.tags.add(tag)
        db_elem.save()

    return HttpResponse(response)


def model_to_lems_xml(rq):
    model_name = rq.GET['model_name']

    try:
        user_name = rq.GET['user_name']
    except:
        user_name = rq.user.username


    model_list = model_name.split(':')
    if len(model_list) > 1:
        user_name = model_list[1]
        model_name = model_list[0]

    model = None
    try:
        model = LemsModel.objects.get(name=model_name,
                              owner__username = user_name)
    except:
        LOG.error('No model found for user: ' + model_name)
        response = '<?xml version="1.0" encoding="utf-8"?>\n'
        response += '<error>Error finding requested model, save the model first</error>'

    if model:
        response = model_json_to_lems_xml(model.json)

    return HttpResponse(response, content_type="text/xml")


def sched_job(rq):
    user = rq.user
    model_id = rq.GET['model_id']
    synapse_id = rq.GET['synapse_id']
    sim_type = rq.GET['sim_type']

    if (not user) or (not model_id) or (not sim_type) or (not synapse_id):
        return HttpResponse('Parameter Error')

    lems_model = LemsModel.objects.get(id=int(model_id))
    lems_model_synapse = LemsModel.objects.get(pk=int(synapse_id))

    # Check for parse errors
    lems_xml = model_json_to_lems_xml(lems_model.json)
    lems_xml_synapse = model_json_to_lems_xml(lems_model_synapse.json)
    if lems_xml.startswith('<error>'):
        return HttpResponse('Unable to schedule job:\n' + lems_xml)
    if lems_xml_synapse.startswith('<error>'):
        return HttpResponse('Unable to schedule job:\n' + lems_xml_synapse)

    # Create entry in the jobs table, get id of new entry
    job = Lems2FpgaJob()
    job.owner = user
    job.lems_model = lems_model
    job.syn_ids = synapse_id

    job.sim_type = sim_type
    job.status = 0
    job.save()
    runCheck()

    return HttpResponse(json.dumps({'message':'Created Job: ' + str(job),
                                    'sim_id':job.pk}))


@login_required
def new_comp(rq, parent_name=None):
    user = rq.user

    all_types = LemsElement.objects.filter(lems_elem='component_types')\
                                   .values_list('name')

    model_name = ''
    if(rq.GET.has_key('model_name')):
        model_name = rq.GET['model_name']

    # js style bools for edit
    edit = 'false'
    if(rq.GET.has_key('edit')):
        edit = 'true'

    all_names = []
    for this_type in all_types:
        all_names.append(this_type[0]) 


    all_dims = LemsElement.objects.filter(lems_elem='dimensions').values_list('name')

    all_dim_names = []
    for this_dim in all_dims:
        all_dim_names.append(this_dim[0])

    all_names.sort()

    synapses = all_available_models(rq.user, MODEL_TYPES.SYN)

    return render(rq,
                  'lems_ui/new_comp.html',
                  {'parent':parent_name, 'synapses' : synapses,
                   'all_comp_type_names':json.dumps(all_names),
                   'all_dim_names':json.dumps(all_dim_names),
                   'source_model_name':model_name,
                   'edit':edit,
                   'dest':reverse('lems_ui.views.save_comp')})


@login_required
def save_comp(rq):
    LOG.debug(rq.POST)

    try:
        name = rq.POST['name']
        description = rq.POST['description']
        extends = rq.POST['extends']

        new_comp_type = model.ComponentType(name, description, extends)
        new_on_start = None

        for key, value in rq.POST.items():
            if key.startswith('param_') and not key.endswith('dim'):
                param_dim = rq.POST[key + '_dim']
                new_comp_type.add_parameter(component.Parameter(value, param_dim))

            elif key.startswith('exp_') and not key.endswith('dim'):
                exp_dim = rq.POST[key + '_dim']
                new_comp_type.add_exposure(component.Exposure(value, exp_dim))

            elif(key.startswith('const_') and not key.endswith('dim')
                 and not key.endswith('_value')):
                const_value = rq.POST[key + '_value']
                const_dim = rq.POST[key + '_dim']
                new_comp_type.add_constant(component.Constant(value, const_value, const_dim))

            elif(key.startswith('child_') and not key.endswith('type')
               and not key.endswith('multi')):
                child_type = rq.POST[key + '_type']
                child_multi = False
                if rq.POST.has_key(key + '_multi'):
                    child_multi = rq.POST[key + '_multi']
                new_comp_type.add_children(component.Children(value, 
                                                    child_type, child_multi))

            elif(key.startswith('attach_') and not key.endswith('type')):
                attach_type = rq.POST[key + '_type']
                new_comp_type.add_attachments(component.Attachments(value, attach_type))

            elif(key.startswith('statevar_') and not key.endswith('dim')
                 and not key.endswith('exp')):
                statevar_dim = rq.POST[key + '_dim']
                statevar_exp = rq.POST[key + '_exp']
                if statevar_exp == 'none':
                    statevar_exp = None

                new_comp_type.dynamics.add_state_variable(
                    dynamics.StateVariable(value, statevar_dim, exposure=statevar_exp))

            elif key.startswith('derivedvar_') and len(key.split('_')) == 2:
                derivedvar_dim = rq.POST[key + '_dim']
                derivedvar_exp = rq.POST[key + '_exp']

                derivedvar = dynamics.DerivedVariable(value,
                                                      dimension=derivedvar_dim,
                                                      exposure=derivedvar_exp)

                if(rq.POST[key + '_selval'] == 'select'):
                    derivedvar.select = rq.POST[key + '_selvaleqn']
                    derivedvar.reduce = rq.POST[key + '_selvalred']
                else:
                    derivedvar.value = rq.POST[key + '_selvaleqn']

                new_comp_type.dynamics.add_derived_variable(derivedvar)

            elif key.startswith('timederiv_') and not key.endswith('_eqn'):
                new_comp_type.dynamics.add_time_derivative(
                    dynamics.TimeDerivative(value, rq.POST[key + '_eqn']))

            elif key.startswith('onstartassign') and not key.endswith('_param'):
                if not new_on_start:
                    new_on_start = dynamics.OnStart()
                    new_comp_type.dynamics.add_event_handler(new_on_start)

                new_on_start.add_action(
                    dynamics.StateAssignment(value, rq.POST[key + '_param']))

            elif key.startswith('onstartevent'):
                if not new_on_start:
                    new_on_start = dynamics.OnStart()
                    new_comp_type.dynamics.add_event_handler(new_on_start)

                new_on_start.add_action(dynamics.EventOut(value))

            elif(key.startswith('oncond') and key.find('assign') < 0
                 and key.find('event') < 0):
                cond = value.replace('<', '.lt.')
                cond = cond.replace('>', '.gt.')
                cond = cond.replace('==', '.eq.')
                new_cond = dynamics.OnCondition(cond)

                for k, v in rq.POST.items():
                    if k.startswith(key):
                        if k.find('assign') > 0 and not k.endswith('_param'):
                            new_cond.add_action(
                                dynamics.StateAssignment(v, rq.POST[k + '_param']))

                        elif k.find('event') > 0: 
                            new_cond.add_action(dynamics.EventOut(v))

                new_comp_type.dynamics.add_event_handler(new_cond)

    except Exception as e:
        return HttpResponse('Invalid Request, ' + str(e))

    db_elem = LemsElement()
    db_elem.name = name
    db_elem.lems_elem = 'component_types'
    db_elem.description = description
    db_elem.owner = rq.user

    # public stays at default
    db_elem.xml = new_comp_type.toxml()
    db_elem.extends = extends
    db_elem.from_file = 'GUI Created'
    db_elem.save()

    db_elem.tags = [1]
    db_elem.save()

    dest = '/djlems/neuron_model/'
    if rq.POST['source_model_name']:
        dest += rq.POST['source_model_name'] + '/'
    return redirect(dest)


# Returns all of the parameters, components and exposures in the
# entire hierarchy for the given component type. Includes the details
# for the type 'comp_type_name'
def hier_details(rq):
    ret_data = []

    this_comp_name = rq.GET['comp_type_name']
    lems_model = model.Model()
    parser = LEMS.LEMSFileParser(lems_model)
    while 1:
        # get the lems element
        this_lems_elem = LemsElement.objects.get(lems_elem='component_types',
                                            name=this_comp_name)

        parser.parse('<LEMS>' + this_lems_elem.xml + '</LEMS>')
        this_lems_obj = lems_model.component_types[this_comp_name]

        this_ret_data = {'name': this_comp_name,
                         'parameters': [],
                         'constants': [],
                         'exposures':[],
                         'event_ports':[]}

        for elem in this_lems_obj.parameters:
            this_ret_data['parameters'].append(
                {'name': elem.name, 'dim': elem.dimension})

        for elem in this_lems_obj.exposures:
            this_ret_data['exposures'].append(
                {'name': elem.name, 'dim': elem.dimension})

        for elem in this_lems_obj.constants:
            this_ret_data['constants'].append(
                {'name': elem.name, 'dim': elem.dimension, 'value': elem.value})

        for elem in this_lems_obj.event_ports:
            this_ret_data['event_ports'].append(
                {'name': elem.name, 'direction': elem.direction })

        ret_data.append(this_ret_data)

        if not this_lems_elem.extends:
            break

        this_comp_name = this_lems_elem.extends

    return HttpResponse(json.dumps(ret_data))


