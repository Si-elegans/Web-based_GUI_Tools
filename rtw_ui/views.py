from django.shortcuts import render

# Create your views here.
import logging
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cenet.models import Neuron, SynapticConn, CENetwork
from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from lems_ui.models import LemsModel, ParameterisedModel, Lems2FpgaJob
from lems_ui.models import all_available_param_models, MODEL_TYPES
from rtw_ui.models import RTW_CONF
from lems_ui.models import LemsElement
from lems.model import model, component, dynamics
from lems.parser import LEMS
from django.shortcuts import render, redirect
import json

from django.conf import settings
User = settings.AUTH_USER_MODEL

LOG = logging.getLogger(__name__)

def hier_details(this_comp_name):

    lems_model = model.Model()
    parser = LEMS.LEMSFileParser(lems_model)
    this_ret_data = {'name': this_comp_name, 'exposures':[]}
    while 1:
        # get the lems element
        this_lems_elem = LemsElement.objects.get(lems_elem='component_types',
                                            name=this_comp_name)

        if not this_lems_elem.extends:
            break

        parser.parse('<LEMS>' + this_lems_elem.xml + '</LEMS>')
        this_lems_obj = lems_model.component_types[this_comp_name]


        for elem in this_lems_obj.exposures:
            this_ret_data['exposures'].append(
                {'name': elem.name, 'dim': elem.dimension})

        this_comp_name = this_lems_elem.extends

    return this_ret_data

@login_required
def delete_rtw_model(rq, model_name=None):
    try:
        # user can only delete models they own
        model = RTW_CONF.objects.get(name=model_name, owner=rq.user)
        model.delete()
    except:
        model = None

    return redirect('/djlems/rtw_ui/dashboard/')

@login_required
def rtw_ui(rq,rtw_id=None):
    if not rq.user.is_authenticated():
        return render(rq, 'base/base.heml', {'user':rq.user})

    open_rtw_conf = None
    network_confs = CENetwork.objects.filter(Q(owner=rq.user) | Q(public=True)).order_by('name')

    # all models shared with user
    models = all_available_param_models(rq.user, MODEL_TYPES.NEURON)

    for model in models:
        this_comps = json.loads(model.json_data)['comps']
        for key, value in this_comps.items():
            #if value['name'] == 'neuron_model':
            model.ctjson_data = json.dumps( hier_details(value['type']))


    if rtw_id is not None:
        open_rtw_conf = RTW_CONF.objects.get(name=rtw_id, owner=rq.user)
        rtw_id = open_rtw_conf.id


    return render(rq, 'rtw_ui/rtw_ui.html',
                  {'user':rq.user, 'rtw_id':rtw_id, 'network_confs':network_confs,
                   'neurons': Neuron.objects.order_by('name'),
                   'open_rtw_conf':open_rtw_conf, 'models' : models})




@csrf_exempt
def save_conf(rq):
    post_data = rq.POST['msg']
    data = json.loads(post_data)
    LOG.debug('SAVING NETWORK: ' + data['rtw_name'])
    data['net_name'] = data['net_name'].split(':')[0]

    net = CENetwork.objects.get(name=data['net_name'], owner=rq.user)
    try:
        rtw = RTW_CONF.objects.get(name=data['rtw_name'], owner=rq.user)
    except:
        rtw = RTW_CONF()

        rtw.owner = rq.user
        rtw.name = data['rtw_name']
        rtw.network = net

    rtw.json = post_data
    rtw.save()
    net.status = "Ready for Synthesis"
    net.save()
    return HttpResponse(json.dumps('RTW: ' + rtw.name + ' saved ok'))


def get_net(rq, net_id=None):
    LOG.debug("Get CElegans Network")

    open_net = None

    if(id):
        try:
            open_net = CENetwork.objects.get(id=net_id)
        except:
            pass

    return HttpResponse((open_net.json))



@login_required
def view_RTW_dashboard (request):
   sorted_rb_results = []
   sorted_share = []
   rtw_confs = RTW_CONF.objects.filter(Q(owner=request.user)).order_by('name')
   rtw_confs_share = {}
   rtw_confs_public = RTW_CONF.objects.filter(Q(public=True)).order_by('name')

   return  render(request, "rtw_ui/dashboard.html",
                               dict(rtw_confs = rtw_confs, rtw_confs_share = rtw_confs_share, rtw_confs_public =rtw_confs_public)
                               )
