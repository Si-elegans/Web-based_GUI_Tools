from django.shortcuts import render

# Create your views here.
import logging
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cenet.models import Neuron, SynapticConn, CENetwork
from cenet.views import ids_phar
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from lems_ui.models import LemsModel, ParameterisedModel, Lems2FpgaJob
from rtw_ui.models import RTW_CONF
from lems_ui.models import LemsElement
from lems.model import model, component, dynamics
from lems.parser import LEMS
import json
import mimetypes
import os
import base64
from django.conf import settings

import xmlrpclib
server_address = 'http://152.71.254.9:444/lems2vhdl/xmlrpc'

LOG = logging.getLogger(__name__)

testMode = True

def worm_conf_per_user(rq):
    LOG.debug("Get Worm Conf")

    #get this users rtw configurations

    rtw_confs = RTW_CONF.objects.filter(Q(owner=rq.user)).order_by('name')
    data = []

    for conf in rtw_confs:
        ready = 'ready'
        if conf.network.status != 'Synthesis Complete':
            ready = 'not ready'
        data.append({'worm_conf' : conf.id, 'name' : conf.name, 'network_name' : conf.network.name, 'network_id' : conf.network.id, 'status': ready})
    return HttpResponse(json.dumps(data))


def worm_conf_get_details(rq,worm_conf):
    data = {}
    data['status'] = "building"
    data['bitfiles'] = []
    data['metadata_files'] = []
    data['dmd_files'] = []
    data['initialation_file'] = rq.build_absolute_uri("/djlems/worm_conf_get_intialisation/" + worm_conf) 
    rtw_conf = RTW_CONF.objects.get(Q(id=worm_conf))
    net_conf = rtw_conf.network

    #get the bitfile list if ready
    ready = True
    #if net_conf.status != 'Synthesis Complete':
    #    ready = False
    if (ready) :
        data['status'] = "ready"
        for i in range(1,303):
            data['bitfiles'].append({'id': str(i), 'url' : rq.build_absolute_uri("/djlems/worm_conf_get_bitfile/" + str(worm_conf) + "/" + str(i))})
        for i in range(303,303+27*5,5):
            data['bitfiles'].append({'id': str(i), 'url' : rq.build_absolute_uri("/djlems/worm_conf_get_muscle_bitfile/" + str(worm_conf) + "/" + str(i))})
        for i in range(1,303):
            data['metadata_files'].append({'id': str(i), 'url' : rq.build_absolute_uri("/djlems/worm_conf_get_metadatafile/" + str(worm_conf) + "/" + str(i))})
        n = 0
        for i in ids_phar:
            data['dmd_files'].append({'id': str(n), 'url' : rq.build_absolute_uri("/djlems/getConnectionMap/" + str(i))})
            n = n + 1
        return HttpResponse(json.dumps(data))
    else:
        return HttpResponse("Not Ready")

def worm_conf_get_intialisation(rq,worm_conf):

    #as soon as this is possible the real process is:
    #get the initialisation file - from lems2fpga for each neuron, which means simply appending them to each other
    #for each neuron use the initialisation data above to grab the itemids of each variable that we are recording and create the readback data
    #using the rtw data stored in the RTW_CONF model

    #check if net_conf is finished synthesis
    rtw_conf = RTW_CONF.objects.get(Q(id=worm_conf))
    net_conf = rtw_conf.network
    if net_conf.status != 'Synthesis Complete':
        if (testMode):
            if worm_conf == "15":
                file_path = settings.BASE_DIR + "/worm_conf/chemoSensory_initialization_left.xml"
            elif worm_conf == "16":
                file_path = settings.BASE_DIR + "/worm_conf/chemoSensory_initialization_right.xml"
            else:
                file_path = settings.BASE_DIR + "/worm_conf/dummymetadatafile.xml"
            fsock = open(file_path,"r")
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            print "file size is: " + str(file_size)
            mime_type_guess = mimetypes.guess_type(file_name)
            if mime_type_guess is not None:
                response = HttpResponse(fsock,mime_type_guess[0])
            response['Content-Disposition'] = 'attachment; filename=' + file_name
            return response
        else:
            return HttpResponse("not ready");


    if True or len(rtw_conf.metadata_init) == 0 or len(rtw_conf.metadata_rtw) == 0:
        server = xmlrpclib.Server(server_address)

        metadata1_message =  server.Lems2VHDL.getJobMetadatafile(str(net_conf.jobid)) #server.Lems2VHDL.getSingleMetadatafile(resultsArray[1]) #
        #print metadata1_message
        metadata1 = json.loads(metadata1_message)['message']
        rtw_conf.metadata_init = metadata1
        rtw_conf.metadata_rtw = server.Lems2VHDL.getJobRTWMetadata(
                    str(net_conf.jobid),rtw_conf.json)
        rtw_conf.save();

    response = HttpResponse(( rtw_conf.metadata_init + rtw_conf.metadata_rtw), content_type='application/octet-stream')
    file_name = "metadata_init_combined.xml"
    response['Content-Disposition'] = 'attachment; filename=' + file_name
    return response


def worm_conf_get_bitfile(rq,worm_conf,neuron_id):

    #get the bitstream file - from lems2fpga (straight file transfer, files need not be changed)

    #try:
    if (testMode):
        file_path = settings.BASE_DIR + "/worm_conf/dummy_neuron_bitfile.bit"
        fsock = open(file_path,"r")
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        print "file size is: " + str(file_size)
        mime_type_guess = mimetypes.guess_type(file_name)
        if mime_type_guess is not None:
            response = HttpResponse(fsock,mime_type_guess[0])
        response['Content-Disposition'] = 'attachment; filename=' + file_name
        return response
    else:
        rtw_conf = RTW_CONF.objects.get(Q(id=worm_conf))
        net_conf = rtw_conf.network
        if net_conf.status != 'Synthesis Complete':
            return HttpResponse("not ready");
        server = xmlrpclib.Server(server_address)
        results = json.loads(server.Lems2VHDL.getJobBitfilesList(str(net_conf.jobid)))['message']
        resultsArray = results[1:-1].split(', ')
        bitfile1_b64_message = server.Lems2VHDL.getJobBitfile(resultsArray[int(neuron_id)])
        bitfile1_b64 = json.loads(bitfile1_b64_message)['message']
        bitfile1 = base64.b64decode(bitfile1_b64)
        response = HttpResponse(bitfile1, content_type='application/octet-stream')
        file_name = "bitfile.sof"
        response['Content-Disposition'] = 'attachment; filename=' + file_name
        return response
    #except IOError:
    #    response = HttpResponseNotFound()


def worm_conf_get_muscle_bitfile(rq,worm_conf,neuron_id):

    #get the bitstream file - from lems2fpga (straight file transfer, files need not be changed)

    #try:
    if (testMode):
        file_path = settings.BASE_DIR + "/worm_conf/dummy_muscle_bitfile.bit"
        fsock = open(file_path,"r")
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        print "file size is: " + str(file_size)
        mime_type_guess = mimetypes.guess_type(file_name)
        if mime_type_guess is not None:
            response = HttpResponse(fsock,mime_type_guess[0])
        response['Content-Disposition'] = 'attachment; filename=' + file_name
        return response
    else:
        rtw_conf = RTW_CONF.objects.get(Q(id=worm_conf))
        net_conf = rtw_conf.network
        file_path = settings.BASE_DIR + "/worm_conf/muscle_" + net_conf.muscleModel + "_bitfile.bit"
        fsock = open(file_path,"r")
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        print "file size is: " + str(file_size)
        mime_type_guess = mimetypes.guess_type(file_name)
        if mime_type_guess is not None:
            response = HttpResponse(fsock,mime_type_guess[0])
        response['Content-Disposition'] = 'attachment; filename=' + file_name
        return response
    #except IOError:
    #    response = HttpResponseNotFound()

def worm_conf_get_metadatafile(rq,worm_conf,neuron_id):

    #get the metadata file - from lems2fpga (straight file transfer, files need not be changed)

    #try:
    file_path = settings.BASE_DIR + "/worm_conf/dummymetadatafile.xml"
    fsock = open(file_path,"r")
    #file = fsock.read()
    #fsock = open(file_path,"r").read()
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    print "file size is: " + str(file_size)
    mime_type_guess = mimetypes.guess_type(file_name)
    if mime_type_guess is not None:
        response = HttpResponse(fsock,mime_type_guess[0])
    response['Content-Disposition'] = 'attachment; filename=' + file_name
    return response

def worm_conf_get_dmdfile(rq,worm_conf,dmd_id):

    #try:
    file_path = settings.BASE_DIR + "/worm_conf/dummy_dmd/" + str(dmd_id) + ".dmd"
    fsock = open(file_path,"r")
    #file = fsock.read()
    #fsock = open(file_path,"r").read()
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    print "file size is: " + str(file_size)
    mime_type_guess = mimetypes.guess_type(file_name)
    if mime_type_guess is not None:
        response = HttpResponse(fsock,mime_type_guess[0])
    response['Content-Disposition'] = 'attachment; filename=' + file_name
    return response
