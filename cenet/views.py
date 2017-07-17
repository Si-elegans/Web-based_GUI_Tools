import logging
import json

from cenet.models import Neuron, SynapticConn, CENetwork
from lems_ui.models import LemsModel, ParameterisedModel, Lems2FpgaJob
from lems_ui.models import MODEL_TYPES
from lems_ui.models import all_available_models, all_available_param_models
from lems_ui.utils import model_json_to_lems_xml
from rtw_ui.models import RTW_CONF
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect

from populations_xml import POPULATIONS_TEMPLATE
from projections_xml import PROJECTIONS_TEMPLATE

LOG = logging.getLogger(__name__)

@login_required
def config_net(rq, net_name=None):
    LOG.debug("Config CElegans Network")

    neuron_models = all_available_param_models(rq.user, MODEL_TYPES.NEURON)
    syn_models = all_available_param_models(rq.user, MODEL_TYPES.SYN)

    open_net = None
    if(net_name):

        if(net_name.find(':') > 0):
            user_name = net_name.split(':')[-1]
            net_name = net_name.split(':')[0]
        else:
            user_name = rq.user.username

        try:
            open_net = CENetwork.objects.get(name=net_name,
                                             owner__username=user_name)
        except:
            try:
                open_net = CENetwork.objects.get(name=net_name, public=True)
            except:
                pass

    return render(rq, 'cenet/config_net.html',
                 {'neurons': Neuron.objects.order_by('name'),
                  'neuron_models': neuron_models,
                  'syn_models': syn_models,
                  'open_net': open_net})


@login_required
def delete_network_model(rq, net_name=None):
    try:
        model = CENetwork.objects.get(name=net_name,
                                      owner__username=rq.user)
        model.delete()
    except:
        model = None

    return redirect('/booking/view_NeuralNetworks')


def load_neurons(rq):
    f = open('out.js')
    data = json.loads(f.read())
    f.close()

    for neuron_name in list(set(data)):
        n = Neuron()
        n.name = neuron_name
        n.data_source=('Virtual_Worm_February_2012.xls')
        n.save()

    return HttpResponse('Saved')


def load_syns(rq):
    f = open('CElegansNeuronTab_head.csv')
    line = f.readline()

    while line:
        elems = line.split(',')
        synconn = SynapticConn()
        synconn.origin = Neuron.objects.get(name=elems[0].lower())
        synconn.target = Neuron.objects.get(name=elems[1].lower())

        synconn.type = elems[2]
        synconn.num_conns = int(elems[3])
        synconn.neurotransmitter = elems[4].strip('\r\n')
        synconn.save()

        line = f.readline()

    return HttpResponse('Saved')


def net_tolems_xml_internal(net_name,user_name):
    response = ''#'<?xml version="1.0" encoding="utf-8"?>\n'
    net = None
    try:
        net = CENetwork.objects.get(name=net_name,
                                    owner__username = user_name)
    except:
        LOG.error('No network found for user: ' + net_name)
        response += '<error>Error finding requested network, try saving</error>'

    if net:
        response += '<Lems>'

        response += "\n\n\n<!--\n"
        response += '\n'.join(net.json[i:i+100] for i in xrange(0, len(net.json), 50))
        response += "\n-->\n\n\n"
        response += "<Include file=\"../CoreTypes/Cells.xml\" />"
        response += "<Include file=\"../CoreTypes/Networks.xml\" />"
        response += "<Include file=\"../CoreTypes/Simulation.xml\" />"
        response += " <Target component=\"sim_c302_A_Full\" />"
        # write out synapses - name-id can be from db name + id
        # write out cells (default and all custom - create name-id)
        # write out populations from db with link to cell def by name-id
        # write out projections from db with link to synapse and cell def by name-id
        net_data = json.loads(net.json)

        response += "<!-- Synapse Models -->\n"
        syn_ids_written = {}
        response += create_synapses(net_data, syn_ids_written) + '\n\n'

        response += "<!-- Neuron Models -->\n"
        model_ids_written = {}
        response += create_neuron_models(net_data, model_ids_written) + '\n\n'

        response += '<network id="' + net_name + '_' + str(net.id) + '">\n\n'

        response += "<!-- Populations -->\n"
        pops, projs = create_populations(net_data, model_ids_written)
        response += pops + '\n\n'

        response += "<!-- Projections -->\n"
        response += create_projections(net_data, projs, syn_ids_written) + '\n\n'

        response += "</network>\n\n"
        response += " <Simulation id=\"sim_c302_A_Full\" length=\"500ms\" step=\"0.1ms\" target=\"" + net_name + '_' + str(net.id) + "\">\n\n"
        response += " </Simulation>\n\n"
        response += "</Lems>\n"
    return response;


def net_to_lems_xml(rq):
    net_name = rq.GET['net_name']

    try:
        user_name = rq.GET['user_name']
    except:
        user_name = rq.user.username

    net_list = net_name.split(':')
    if len(net_list) > 1:
        user_name = net_name[1]
        net_name = net_name[0]

    response = net_tolems_xml_internal(net_name,user_name)
    return HttpResponse(response, content_type="text/xml")


def create_neuron_models(net_data, param_model_ids_written):
    # Need to write out lems xml for all neuron models that are used in the net
    response = ''

    # 1. write out the top-level default neuron model
    # 2. for each group, write out the customised neuron model

    # 1. top-level default neuron
    xml, root_comp_name = get_model_xml(net_data['default_model_id'])
    response += xml
    param_model_ids_written[net_data['default_model_id']] = root_comp_name


    # 2. for each customised group
    for group in net_data['groups'].keys():
        group_json = net_data['parameterised_data']['neuron_groups'][group]

        # TODO: This is not using the new parameters entered on the net screen!!!
        # TODO: Incomplete, Must be fixed
        param_model_id = group_json['model_id']

        if param_model_id in param_model_ids_written:
            continue

        xml, root_comp_name = get_model_xml(param_model_id)
        response += xml
        param_model_ids_written[param_model_id] = root_comp_name

    return response


def create_synapses(net_data, param_model_ids_written):
    # Need to write out lems xml for all synapses that are used in the net
    response = ''

    # 1. write out the top-level default synapse
    # 2. write out any neuro transmitter specific synapses
    # 3. for each customised pre-synaptic neuron
    #   a) write out neuron default synapse
    #   b) write out any individual connection synapses

    # 1. top-level default synapse
    xml, root_comp_name = get_model_xml(net_data['default_syn_model_id'])
    response += xml
    param_model_ids_written[net_data['default_syn_model_id']] = root_comp_name



    # 2. any neurotx specific synapses
    for param_model_id in net_data['neurotx_data'].values():
        if param_model_id in param_model_ids_written:
            continue

        xml, root_comp_name = get_model_xml(param_model_id)
        response += xml
        param_model_ids_written[param_model_id] = root_comp_name

    # 3 each customised neuron
    syn_groups_json = net_data['parameterised_data']['syn_groups']
    for customised_neuron in syn_groups_json:
        # 3. a) default synapse model for this neuron
        param_model_id = syn_groups_json[customised_neuron]['data']['default_syn']

        if not param_model_id in param_model_ids_written:
            xml, root_comp_name = get_model_xml(param_model_id)
            response += xml
            param_model_ids_written[param_model_id] = root_comp_name

        # 3. b) each customised specific connection
        syn_data_json = syn_groups_json[customised_neuron]['syn_data']
        for param_model_id in syn_data_json.values():
            if not param_model_id in param_model_ids_written:
                xml, root_comp_name = get_model_xml(param_model_id)
                response += xml
                param_model_ids_written[param_model_id] = root_comp_name

    return response


def get_model_xml(param_model_id):
    param_model_obj = ParameterisedModel.objects.get(id=param_model_id)
    xml = model_json_to_lems_xml(param_model_obj.model.json,
                                 include_hier=True,
                                 include_header=False)

    pos = 0
    namespaced_xml = ''
    ids = []
    # try to namespace the ids using the param_model id
    # try to replace all occurances of each id with
    # the same id string + the param_model_id
    while xml[pos:].find('id="') >= 0:
        id_start = xml[pos:][xml[pos:].find('id="') + 4:]
        ids.append(id_start[: id_start.find('"')])
        pos += xml[pos:].find('id="') + 4

    for this_id in ids:
        xml = xml.replace('"' + this_id + '"',
                          '"' + this_id + '_' + str(param_model_obj.id) + '"')

    # Deduce the root component name
    root_comp_idx = xml.rfind('\n<Component id="') + 16
    root_comp_name = xml[ root_comp_idx : 
                      root_comp_idx + xml[root_comp_idx :].find('"') ]

    return xml, root_comp_name


def create_populations(net_data, model_ids_written):
    neurons = Neuron.objects.order_by('name')

    customized_neurons = \
        [item for sublist in net_data['groups'].values() for item in sublist]

    # immutable strings in python, no need to copy
    pops_template = POPULATIONS_TEMPLATE
    projs_template = PROJECTIONS_TEMPLATE

    for group in net_data['groups']:
        for neuron in net_data['groups'][group]:

            param_model_id = net_data['parameterised_data']['neuron_groups']\
                                                           [group]['model_id']

            # find in template and add neuron model id
            # TODO: the actual model id isn't using the parameterised data
            # it would have to be a new ParameterisedModel object
            # TODO: don't rely on top-level being called "neuron_model"
            comp_idx = pops_template.find('"' + neuron.upper() + '"')
            comp_idx += pops_template[ comp_idx :].find('component=""') + 11

            pops_template = pops_template[:comp_idx] +\
                                model_ids_written[param_model_id] +\
                                pops_template[comp_idx:]

            projs_template = projs_template.replace(
                                '"../'+neuron.upper() + '/0/"',
                                '"../'+neuron.upper() + '/0/' +
                                model_ids_written[param_model_id]+'"')

    for neuron in neurons:
        if neuron.name not in customized_neurons:

            # TODO: Same TODOs as above
            comp_idx = pops_template.find(neuron.name.upper())
            comp_idx += pops_template[ comp_idx :].find('component=""') + 11

            pops_template = pops_template[:comp_idx] +\
                                model_ids_written[net_data["default_model_id"]] +\
                                pops_template[comp_idx:]


            projs_template = projs_template.replace(
                                '"../'+neuron.name.upper() + '/0/"',
                               '"../'+ neuron.name.upper() + '/0/' +
                                model_ids_written[net_data["default_model_id"]]+'"')

    return pops_template, projs_template


def create_projections(net_data, projs_template, syn_ids_written):
    neurons = Neuron.objects.order_by('name')

    customized_neurons = \
        [item for sublist in net_data['groups'].values() for item in sublist]

    # 1. Set every synapse to default
    default_id = net_data['default_syn_model_id']
    projs_template = projs_template.replace(
                                    '""',
                                    '"' + syn_ids_written[default_id] + '"')

    # 2. Set all neuro transmitter to specified
    for neurotx in net_data['neurotx_data']:
        idx = 0
        while projs_template[idx:].find(neurotx) >= 0:
            tx_idx = projs_template[idx:].find(neurotx)
            syn_idx = idx + tx_idx + projs_template[idx + tx_idx:].find('synapse="') + 9

            projs_template = projs_template[: syn_idx] +\
                             syn_ids_written[net_data['neurotx_data'][neurotx]] +\
                             projs_template[ syn_idx + projs_template[syn_idx :].find('"') :]
            idx = syn_idx

    # 3. Set all cusomised to their default
    syn_groups = net_data['parameterised_data']['syn_groups']
    for neuron_name in syn_groups:
        default_id = syn_groups[neuron_name]['data']['default_syn']

        idx = 0#
        search_str = 'presynapticPopulation="' + neuron_name.upper()
        while projs_template[idx:].find(search_str) >= 0:
            tx_idx = projs_template[idx:].find(search_str)
            syn_idx = idx + tx_idx + projs_template[idx + tx_idx:].find('synapse="') + 9

            projs_template = projs_template[: syn_idx] +\
                             syn_ids_written[default_id] +\
                             projs_template[ syn_idx + projs_template[syn_idx :].find('"') :]
            idx = syn_idx


    # 4. Set all specific customised to specified
    for neuron_name in syn_groups:
        for (post_syn, syn_id) in syn_groups[neuron_name]['syn_data'].items():
            idx = 0#
            search_str = 'NC_' + neuron_name.upper() + '_' + post_syn.upper()
            while projs_template[idx:].find(search_str) >= 0:
                tx_idx = projs_template[idx:].find(search_str)
                syn_idx = idx + tx_idx + projs_template[idx + tx_idx:].find('synapse="') + 9

                projs_template = projs_template[: syn_idx] +\
                                 syn_ids_written[syn_id] +\
                                 projs_template[ syn_idx + projs_template[syn_idx :].find('"') :]
                idx = syn_idx

    return projs_template


def syn_conns(rq, neuron):
    LOG.debug('requeseted synapses for neuron: ' + str(neuron))

    conns = SynapticConn.objects.filter(Q(origin__name=neuron.lower()))

    output = []
    for conn in conns:
        output.append({'origin': conn.origin.name,
                       'target': conn.target.name,
                       'num_conns': conn.num_conns,
                       'neurotransmitter': conn.neurotransmitter})
    return HttpResponse(json.dumps(output))


def syn_conns_all(rq):
    LOG.debug('requeseted synapses for all neurons')

    conns = SynapticConn.objects.all()

    output = []
    for conn in conns:
        output.append({'origin': conn.origin.name,
                       'target': conn.target.name,
                       'num_conns': conn.num_conns,
                       'neurotransmitter': conn.neurotransmitter})
    return HttpResponse(json.dumps(output))


@csrf_exempt
def save_net(rq):
    post_data = rq.POST['msg']
    data = json.loads(post_data)
    LOG.debug('SAVING NETWORK: ' + data['net_name'])
    data['net_name'] = data['net_name'].split(':')[0]

    try:
        net = CENetwork.objects.get(name=data['net_name'], owner=rq.user)

    except:
        net = CENetwork()

        net.owner = rq.user
        net.name = data['net_name']
        net.status = "Under Development"

    net.description = data['net_description']
    net.muscleModel = data['muscleModel']
    if net.muscleModel is None:
        net.muscleModel = 1
    net.json = post_data

    if (net.status != "Under Development" and net.status != ""):
        return HttpResponse(json.dumps('Error: ' + net.name + " can't be saved since it is already being used for a simulation configuration."))

    net.status = "Under Development"
    net.save()

    return HttpResponse(json.dumps('Network: ' + net.name + ' saved ok'))


@login_required
def dashboard(rq):

    model_objs = all_available_models(rq.user, MODEL_TYPES.NEURON)
    syn_models = all_available_models(rq.user, MODEL_TYPES.SYN)
    net_models = all_available_models(rq.user, MODEL_TYPES.NET)

    # TODO: as above but for CENetwork - individual sharing allowed?
    nets = CENetwork.objects.filter(Q(owner=rq.user)).order_by('name')
    rtw_confs = RTW_CONF.objects.filter(Q(owner=rq.user)).order_by('name')
    job_objs = Lems2FpgaJob.objects.filter(Q(owner=rq.user)).\
                        filter(Q(out_of_date=False)).order_by('-created')

    # arrange into {model : [obj, obj]}
    models = []
    jobs_found = False
    for model in model_objs:
        jobs = []
        for job in job_objs:
            if job.lems_model == model:
                jobs_found = True
                jobs.append(job)

        models.append((model, jobs))

    return render(rq, 'cenet/dashboard.html',
                  {'models':models, 'nets':nets, 'jobs_found':jobs_found,
                   'syn_models':syn_models, 'net_models':net_models, 'rtw_confs':rtw_confs})


ids_phar = ["MCL","MCR","M4","NSMR","M3R","M3L","NSML","MI","I4","M2L","M5",
            "I2R","M2R","I2L","I6","I5","M1","I1L","I1R","I3"]
# order is ,I1L,I1R,I2L,I2R,I3,I4,I5,I6,M1,M2L,M2R,M3L,M3R,M4,M5,
#           MCL,MCR,MI,NSML,NSMR
def getConnectionMap(rq,neuron):

    conns = SynapticConn.objects.filter(Q(target__name=neuron.lower()))
    output = ""
    output2 = ""
    output3 = ""
    neurons = Neuron.objects.filter( fpga_id__gt= -1).order_by('fpga_id')
    #ids = ["ADAL","ADAR","ADEL","ADER","ADFL","ADFR","ADLL","ADLR","AFDL","AFDR","AIAL","AIAR","AIBL","AIBR","AIML","AIMR","AINL","AINR","AIYL","AIYR","AIZL","AIZR","ALA","ALML","ALMR","ALNL","ALNR","AQR","AS1","AS2","AS3","AS4","AS5","AS6","AS7","AS8","AS9","AS10","AS11","ASEL","ASER","ASGL","ASGR","ASHL","ASHR","ASIL","ASIR","ASJL","ASJR","ASKL","ASKR","AUAL","AUAR","AVAL","AVAR","AVBL","AVBR","AVDL","AVDR","AVEL","AVER","AVFL","AVFR","AVG","AVHL","AVHR","AVJL","AVJR","AVKL","AVKR","AVL","AVM","AWAL","AWAR","AWBL","AWBR","AWCL","AWCR","BAGL","BAGR","BDUL","BDUR","CANL","CANR","CEPDL","CEPDR","CEPVL","CEPVR","DA1","DA2","DA3","DA4","DA5","DA6","DA7","DA8","DA9","DB1/3","DB2","DB3/1","DB4","DB5","DB6","DB7","DD1","DD2","DD3","DD4","DD5","DD6","DVA","DVB","DVC","FLPL","FLPR","HSNL","HSNR","I1L","I1R","I2L","I2R","I3","I4","I5","I6","IL1DL","IL1DR","IL1L","IL1R","IL1VL","IL1VR","IL2DL","IL2DR","IL2L","IL2R","IL2VL","IL2VR","LUAL","LUAR","M1","M2L","M2R","M3L","M3R","M4","M5","MCL","MCR","MI","NSML","NSMR","OLLL","OLLR","OLQDL","OLQDR","OLQVL","OLQVR","PDA","PDB","PDEL","PDER","PHAL","PHAR","PHBL","PHBR","PHCL","PHCR","PLML","PLMR","PLNL","PLNR","PQR","PVCL","PVCR","PVDL","PVDR","PVM","PVNL","PVNR","PVPL","PVPR","PVQL","PVQR","PVR","PVT","PVWL","PVWR","RIAL","RIAR","RIBL","RIBR","RICL","RICR","RID","RIFL","RIFR","RIGL","RIGR","RIH","RIML","RIMR","RIPL","RIPR","RIR","RIS","RIVL","RIVR","RMDDL","RMDDR","RMDL","RMDR","RMDVL","RMDVR","RMED","RMEL","RMER","RMEV","RMFL","RMFR","RMGL","RMGR","RMHL","RMHR","SAADL","SAADR","SAAVL","SAAVR","SABD","SABVL","SABVR","SDQL","SDQR","SIADL","SIADR","SIAVL","SIAVR","SIBDL","SIBDR","SIBVL","SIBVR","SMBDL","SMBDR","SMBVL","SMBVR","SMDDL","SMDDR","SMDVL","SMDVR","URADL","URADR","URAVL","URAVR","URBL","URBR","URXL","URXR","URYDL","URYDR","URYVL","URYVR","VA1","VA2","VA3","VA4","VA5","VA6","VA7","VA8","VA9","VA10","VA11","VA12","VB1","VB2","VB3","VB4","VB5","VB6","VB7","VB8","VB9","VB10","VB11","VC1","VC2","VC3","VC4","VC5","VC6","VD1","VD2","VD3","VD4","VD5","VD6","VD7","VD8","VD9","VD10","VD11","VD12","VD13"]

    #for neuron in neurons:
    #    try:
    #        neuron.fpga_id = ids.index(neuron.name.upper())
    #        neuron.save();
    #    except ValueError:
    #        neuron.fpga_id = -1
    #        neuron.save();
    #        "nothing"
    for neuron2 in neurons:
        if neuron2.name.upper() in ids_phar:
            exists = False
            for conn in conns:
                if conn.origin == neuron2:
                    exists = True
            if exists:
                output = output + "1"
            else:
                output = output + "0"
            output2 = output2 + "," + neuron2.name.upper()
            output3 = output3 + "," + str(neuron2.fpga_id)
    output = output + "\r\n" #+ output2 + "\r\n" + output3

    return HttpResponse(output )

