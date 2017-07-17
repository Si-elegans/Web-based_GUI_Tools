import sys
import os
import json
import time
import requests
import logging
import datetime
from django.core.context_processors import csrf
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from booking import models as m
from lems_ui import models as m_neural
from lems_ui.models import MODEL_TYPES
from cenet import models as m_net
from rtw_ui import models as m_rtw
from django.db.models import Q, Max
from booking.models import Reservation, PE_results, RB_results
from booking.constants import *
from behaviouralExperimentDefinition.models import behaviourExperimentType_model
from django.db import IntegrityError
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from lxml import etree
from lxml.etree import XMLSyntaxError
from requests.exceptions import ConnectionError
from django.views.decorators.csrf import csrf_exempt
from mysite.my_decorators import http_basic_auth
from siteLogic.utils import secure_exception_to_str
from spirit.models import User
import httplib
from django.core.exceptions import ObjectDoesNotExist
from cenet.models import Neuron
from booking.forms import Reservation_form

# Get an instance of a logger
logger = logging.getLogger(__name__)

mainURL = 'http://' + IP_SC + '/SC/api/emulator/'
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CA_BUNDLE = "https-certificates/cloud_server_runsslserver.crt"


################
# VIEWS TO RESPOND ACTIONS TRIGGERED IN THE BOOKING WEB
###############
# Create your views here.


#################
# Json - Rest Views
##################
@login_required
def rb_result_make_public(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        rb_result = payload.get('rb_result', '')
        public_check = payload.get('public_check', '')
        if public_check != '':
            try:
                rb_result_instance = RB_results.objects.get(pk=rb_result)
            except ObjectDoesNotExist:
                resp_data = {'response': -1,
                             'msg': 'User has send a rb result id which does not exist'}  # User has send a behaviour experiment mode id which doesn't exist
                return JsonResponse(resp_data)
            if public_check == True:
                rb_result_instance.public = True
                rb_result_instance.save()
            else:
                rb_result_instance.public = False
                rb_result_instance.save()
            resp_data = {'response': 1, 'msg': 'rb_result public field set correctly'}
            return JsonResponse(resp_data)
    resp_data = {'response': -1, 'msg': 'Bad request'}  # Bad request
    return JsonResponse(resp_data)


#################
# Web Views
##################
@login_required
def view_RB_results(request):
    sorted_rb_results = []
    sorted_rb_results_secure = []
    sorted_share = []
    sorted_share_secure = []
    rb_results = m.RB_results.objects.all()
    share = m.share_rb_results.objects.all()
    if len(rb_results) > 0:
        try:
            sorted_rb_results = sorted(rb_results, reverse=True)
        except IndexError as e:
            logger.error(
                    "Error: indexError, " + secure_exception_to_str(
                        e) + ". rb_result that has missing file_order=0 is:")
    if len(share) > 0:
        sorted_share = sorted(share, reverse=True)
    simIdList = [-1]
    for sorted_rb_result in sorted_rb_results:
        if hasattr(sorted_rb_result, 'reservation_for_rb_result'):
            simIdList.append(sorted_rb_result.reservation_for_rb_result.sim_id)
    for sorted_rb_result in sorted_share:
        if hasattr(sorted_rb_result, 'reservation_for_rb_result'):
            simIdList.append(sorted_rb_result.rb_results.reservation_for_rb_result.sim_id)
    # print 'sorted_rb_results', sorted_rb_results
    # print 'sorted_share', sorted_share
    if simIdList:
        # print 'simIdList',  simIdList
        conn2 = httplib.HTTPSConnection('results.si-elegans.eu')
        reqData = "/NUIG_RUS/doesSimDataExist/simIds=" + ','.join([str(x) for x in simIdList])
        conn2.request("GET", reqData)
        response2 = conn2.getresponse()
        responseData2 = response2.read()  # If 'Availability == true' received, ok to transmit
        simIdsValid = json.loads(responseData2)
        # print 'simIdsValid', simIdsValid
    for sorted_rb_result in sorted_rb_results:
        found = False
        if hasattr(sorted_rb_result, 'reservation_for_rb_result'):
            test = sorted_rb_result.reservation_for_rb_result.sim_id
            for simIdValid in simIdsValid:
                # print 'simIdValid' , simIdValid, '; test', test
                if str(simIdValid[0]) == str(test):
                    found = True
        if found == True:
            sorted_rb_results_secure.append(sorted_rb_result)
    for sorted_rb_result in sorted_share:
        found =False
        if hasattr(sorted_rb_result, 'reservation_for_rb_result'):
            test = sorted_rb_result.rb_results.reservation_for_rb_result.sim_id
            for simIdValid in simIdsValid:
                # print 'simIdValid', simIdValid, '; test', test
                if str(simIdValid[0]) == str(test):
                    found = True
        if found == True:
            # print 'sorted_rb_results.remove(sorted_rb_result)', sorted_rb_result
            sorted_share_secure.append(sorted_rb_result)
    # print 'sorted_rb_results_secure', sorted_rb_results_secure
    # print 'sorted_share_secure', sorted_share_secure
    return render(request, "booking/view_RB_results.html",
                  dict(rb_results=sorted_rb_results_secure, users=User.objects.all(), share=sorted_share_secure)
                  )


@login_required
def neuronModel_make_public(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        rb_result = payload.get('neuronModel', '')
        public_check = payload.get('public_check', '')
        if public_check != '':
            try:
                lemsModel = m_neural.LemsModel.objects.get(pk=rb_result)
            except ObjectDoesNotExist:
                resp_data = {'response': -1,
                             'msg': 'User has send a neuronModel result id which does not exist'}  # User has send a behaviour experiment mode id which doesn't exist
                return JsonResponse(resp_data)
            if public_check == True:
                lemsModel.public = True
                lemsModel.save()
            else:
                lemsModel.public = False
                lemsModel.save()
            resp_data = {'response': 1, 'msg': 'rb_result public field set correctly'}
            return JsonResponse(resp_data)
    resp_data = {'response': -1, 'msg': 'Bad request'}  # Bad request
    return JsonResponse(resp_data)


@login_required
def share_RB_results(request):
    # print("HERE1")
    return render(request, "booking/share_RB_results.html",
                  dict(rb_results=m.RB_results.objects.all(), users=User.objects.all(),
                       share=m.share_rb_results.objects.all())
                  )


#################
# Json - Rest Views
##################
@login_required
def pe_result_make_public(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        pe_result = payload.get('pe_result', '')
        public_check = payload.get('public_check', '')
        if public_check != '':
            try:
                pe_result_instance = PE_results.objects.get(pk=pe_result)
            except ObjectDoesNotExist:
                resp_data = {'response': -1,
                             'msg': 'User has send a pe_result id which does not exist'}  # User has send a behaviour experiment mode id which doesn't exist
                return JsonResponse(resp_data)
            if public_check == True:
                pe_result_instance.public = True
                pe_result_instance.save()
            else:
                pe_result_instance.public = False
                pe_result_instance.save()
            resp_data = {'response': 1, 'msg': 'pe_result public field set correctly'}
            return JsonResponse(resp_data)
    resp_data = {'response': -1, 'msg': 'Bad request'}  # Bad request
    return JsonResponse(resp_data)


#################
# Web Views
##################
@login_required
def view_integrated_results(request):
    #TODO: Add extra security for integrated visualization. Right now is not giving an error, because for other reasons, we're requesting reservation for pe_result and rb_result within a for in the template, check this in detail in the future
    sorted_pe_results = []
    sorted_share = []
    pe_results_secure = []  # This list will contain those pe_results that have no missing sources.list file_order=0
    pe_results = m.PE_results.objects.all()
    share = m.share_pe_results.objects.all()
    share_rb_results = m.share_rb_results.objects.all()
    share_secure = []  # This list will contain those shares that have no missing sources.list file_order=0
    if len(pe_results) > 0:
        for pe_result in pe_results:
            try:
                pe_result.pe_results_files.filter(file_order=0)[
                    0]  # If sources.list is missing then it will raise an IndexError, we are not interested in getting sources.list, rather in taking out those pe_results that do not contain a valid
                pe_results_secure.append(pe_result)
            except IndexError as e:
                logger.error("Error: indexError, " + secure_exception_to_str(
                    e) + ". pe_result that has missing file_order=0 is: " + unicode(pe_result.uuid))
        if len(pe_results_secure) > 0:
            sorted_pe_results = sorted(pe_results_secure,
                                       key=lambda pe_result: pe_result.pe_results_files.filter(file_order=0)[0].created,
                                       reverse=True)
    if len(share) > 0:
        for share_iterator in share:
            try:
                share_iterator.pe_results.pe_results_files.filter(file_order=0)[0]
                # If sources.list is missing then it will raise an IndexError, we are not interested in getting
                #  sources.list, rather in taking out those share that do not contain a valid
                share_secure.append(share_iterator)
            except IndexError as e:
                logger.error("Error: indexError, " + secure_exception_to_str(
                    e) + ". share_pe_results that has missing file_order=0 is:" + unicode(
                    share_iterator.pe_results.uuid))
        if len(share_secure):
            sorted_share = sorted(share_secure, key=lambda share_instance:
            share_instance.pe_results.pe_results_files.filter(file_order=0)[0].created, reverse=True)
    return render(request, "booking/integrated_results_review.html",
                  dict(pe_results=sorted_pe_results, users=User.objects.all(), share=sorted_share, share_rb_results=share_rb_results)
                  )


@login_required
def view_PE_results(request):
    sorted_pe_results = []
    sorted_share = []
    pe_results_secure = []  # This list will contain those pe_results that have no missing sources.list file_order=0 & missing reservation
    pe_results = m.PE_results.objects.all()
    share = m.share_pe_results.objects.all()
    share_secure = []  # This list will contain those shares that have no missing sources.list file_order=0  & missing reservation
    if len(pe_results) > 0:
        for pe_result in pe_results:
            try:
                pe_result.pe_results_files.filter(file_order=0)[
                    0]  # If sources.list is missing then it will raise an IndexError, we are not interested in getting sources.list, rather in taking out those pe_results that do not contain a valid
                try:
                    reservation_instance = Reservation.objects.filter(pe_result=pe_result)[0] #Checking if pe_result has reservation to about error in template
                    pe_results_secure.append(pe_result)
                except (ObjectDoesNotExist, IndexError) as e:
                    logger.error(
                        "ObjectDoesNotExist, Seems that some of the pe_result don't have reservation; pe_result:" + str(pe_result) + ', exception:' + secure_exception_to_str(
                            e))

            except (ObjectDoesNotExist, IndexError) as e:
                logger.error("Error: indexError, " + secure_exception_to_str(
                    e) + ". pe_result that has missing file_order=0 is: " + unicode(pe_result.uuid))



        if len(pe_results_secure) > 0:
            sorted_pe_results = sorted(pe_results_secure,
                                       key=lambda pe_result: pe_result.pe_results_files.filter(file_order=0)[0].created,
                                       reverse=True)
    if len(share) > 0:
        for share_iterator in share:
            try:
                share_iterator.pe_results.pe_results_files.filter(file_order=0)[0]# If sources.list is missing then it will raise an IndexError, we are not interested in getting
                #  sources.list, rather in taking out those share that do not contain a valid
                try:
                    reservation_instance = Reservation.objects.filter(pe_result=share_iterator.pe_results)[0] #Checking if pe_result has reservation to about error in template
                    share_secure.append(share_iterator)
                except (ObjectDoesNotExist, IndexError) as e:
                    logger.error(
                        "ObjectDoesNotExist, Seems that some of the shared pe_result don't have reservation; pe_result:" + str(pe_result) + ', exception:' + secure_exception_to_str(
                            e))
            except (ObjectDoesNotExist, IndexError) as e:
                logger.error("Error: indexError, " + secure_exception_to_str(
                        e) + ". share_pe_results that has missing file_order=0 is:" + unicode(
                        share_iterator.pe_results.uuid))
        if len(share_secure):
            sorted_share = sorted(share_secure, key=lambda share_instance:
            share_instance.pe_results.pe_results_files.filter(file_order=0)[0].created, reverse=True)
    return render(request, "booking/view_PE_results.html",
                  dict(pe_results=sorted_pe_results, users=User.objects.all(), share=sorted_share)
                  )


@login_required
def share_PE_results(request):
    if request.method == 'POST':
        users = request.POST.getlist("user_pe_results_share", "")
        pe_results = request.POST.getlist("pe_results_share", "")
        pe_results_public = request.POST.getlist("pe_results_public", "")
        if 'sharePublic' in request.POST:
            # Complete loop through all the experiments to check what has been defined to be public and to set it accordingly
            # GE: This can be improved, maybe using Javascript and using a different view to trigger a single update when cliked over it
            for selected_pe_result in m.PE_results.objects.all():
                if pe_results_public.count(str(selected_pe_result.pk)) > 0:
                    selected_pe_result.public = True
                    selected_pe_result.save()
                else:
                    selected_pe_result.public = False
                    selected_pe_result.save()
            messages.success(request, 'Your pe results\' public sharing has been updated. ')
        elif 'sharePeople' in request.POST:
            if (not pe_results or not users):
                messages.error(request, 'No pe results or user to share with selected')
            else:
                for selected_pe_result in pe_results:
                    for selectedUser in users:
                        try:
                            # print "Try barruan"
                            # code that produces error
                            post = m.share_pe_results.objects.create(user=User.objects.get(pk=selectedUser),
                                                                     pe_results=m.PE_results.objects.get(
                                                                             pk=selected_pe_result), )
                        except IntegrityError as e:
                            print {"IntegrityError": e.message}
                            messages.warning(request,
                                             'The given share relationship is already defined: User: ' + User.objects.get(
                                                     pk=selectedUser).username
                                             + ", Pe result: " + unicode(m.PE_results.objects.get(
                                                     uuid=selected_pe_result).uuid) + ", Exception message: " + str(
                                                     e.message))
                            return render(request, "booking/share_PE_results.html",
                                          dict(pe_results=m.PE_results.objects.all(), users=User.objects.all(),
                                               share=m.share_pe_results.objects.all())
                                          )
                        messages.success(request, 'Thank you for sharing new Pe results' +
                                         'User: ' + User.objects.get(pk=selectedUser).username
                                         + ", Pe result: " + unicode(
                                m.PE_results.objects.get(uuid=selected_pe_result).uuid))
    sorted_pe_results = []
    sorted_share = []
    pe_results_secure = []  # This list will contain those pe_results that have no missing sources.list file_order=0 & missing reservation
    pe_results = m.PE_results.objects.all()
    share = m.share_pe_results.objects.all()
    share_secure = []  # This list will contain those shares that have no missing sources.list file_order=0  & missing reservation
    if len(pe_results) > 0:
        for pe_result in pe_results:
            try:
                pe_result.pe_results_files.filter(file_order=0)[
                    0]  # If sources.list is missing then it will raise an IndexError, we are not interested in getting sources.list, rather in taking out those pe_results that do not contain a valid
                try:
                    reservation_instance = Reservation.objects.filter(pe_result=pe_result)[0] #Checking if pe_result has reservation to about error in template
                    pe_results_secure.append(pe_result)
                except (ObjectDoesNotExist, IndexError) as e:
                    logger.error(
                        "ObjectDoesNotExist, Seems that some of the pe_result don't have reservation; pe_result:" + str(pe_result) + ', exception:' + secure_exception_to_str(
                            e))

            except (ObjectDoesNotExist, IndexError) as e:
                logger.error("Error: indexError, " + secure_exception_to_str(
                    e) + ". pe_result that has missing file_order=0 is: " + unicode(pe_result.uuid))



        if len(pe_results_secure) > 0:
            sorted_pe_results = sorted(pe_results_secure,
                                       key=lambda pe_result: pe_result.pe_results_files.filter(file_order=0)[0].created,
                                       reverse=True)
    if len(share) > 0:
        for share_iterator in share:
            try:
                share_iterator.pe_results.pe_results_files.filter(file_order=0)[0]# If sources.list is missing then it will raise an IndexError, we are not interested in getting
                #  sources.list, rather in taking out those share that do not contain a valid
                try:
                    reservation_instance = Reservation.objects.filter(pe_result=share_iterator.pe_results)[0] #Checking if pe_result has reservation to about error in template
                    share_secure.append(share_iterator)
                except (ObjectDoesNotExist, IndexError) as e:
                    logger.error(
                        "ObjectDoesNotExist, Seems that some of the shared pe_result don't have reservation; pe_result:" + str(pe_result) + ', exception:' + secure_exception_to_str(
                            e))
            except (ObjectDoesNotExist, IndexError) as e:
                logger.error("Error: indexError, " + secure_exception_to_str(
                        e) + ". share_pe_results that has missing file_order=0 is:" + unicode(
                        share_iterator.pe_results.uuid))
        if len(share_secure):
            sorted_share = sorted(share_secure, key=lambda share_instance:
            share_instance.pe_results.pe_results_files.filter(file_order=0)[0].created, reverse=True)
    return render(request, "booking/share_PE_results.html",
                  dict(pe_results=sorted_pe_results, users=User.objects.all(), share=sorted_share)
                  )


@login_required
def view_NeuronModels(request):
    neuronModels_my = m_neural.get_lems_models(request.user, MODEL_TYPES.NEURON)
    synapseModels_my = m_neural.get_lems_models(request.user, MODEL_TYPES.SYN)

    neuronModels_curated = m_neural.get_curated_lems_models(MODEL_TYPES.NEURON)
    synapseModels_curated = m_neural.get_curated_lems_models(MODEL_TYPES.SYN)

    neuronModels_shared = m_neural.get_shared_lems_models(request.user,
                                                          MODEL_TYPES.NEURON)
    synapseModels_shared = m_neural.get_shared_lems_models(request.user,
                                                           MODEL_TYPES.SYN)

    return render(request, "booking/view_neuronModels.html",
                  dict(neuronModels_my=neuronModels_my,
                       synapseModels_my=synapseModels_my,
                       neuronModels_curated=neuronModels_curated,
                       synapseModels_curated=synapseModels_curated,
                       neuronModels_shared=neuronModels_shared,
                       synapseModels_shared=synapseModels_shared))


@login_required
def share_NeuronModels(request):
    neuronModels_my = m_neural.get_lems_models(request.user, MODEL_TYPES.NEURON)
    synapseModels_my = m_neural.get_lems_models(request.user, MODEL_TYPES.SYN)

    neuronModels_curated = m_neural.get_curated_lems_models(MODEL_TYPES.NEURON)
    synapseModels_curated = m_neural.get_curated_lems_models(MODEL_TYPES.SYN)

    neuronModels_public = m_neural.get_public_lems_models(MODEL_TYPES.NEURON)
    synapseModels_public = m_neural.get_public_lems_models(MODEL_TYPES.SYN)

    neuronModels_shared = m_neural.get_shared_lems_models(request.user,
                                                          MODEL_TYPES.NEURON)
    synapseModels_shared = m_neural.get_shared_lems_models(request.user,
                                                           MODEL_TYPES.SYN)

    return render(request, "booking/share_NeuronModels.html",
                  dict(neuronmodels_my=neuronModels_my,
                       synapsemodels_my=synapseModels_my,
                       neuronModels_curated = neuronModels_curated,
                       synapseModels_curated = synapseModels_curated,
                       neuronModels_public = neuronModels_public,
                       synapseModels_public = synapseModels_public,
                       neuronModels_shared=neuronModels_shared,
                       synapseModels_shared=synapseModels_shared,
                       allModels_shared=m_neural.share_LemsModel.objects.all(),
                       users=User.objects.all()))


@login_required
def networkModel_make_public(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        networkModel = payload.get('networkModel', '')
        public_check = payload.get('public_check', '')
        if public_check != '':
            try:
                ceNetwork = m_net.CENetwork.objects.get(pk=networkModel)
            except ObjectDoesNotExist:
                resp_data = {'response': -1,
                             'msg': 'User has send a neuronModel result id which does not exist'}  # User has send a behaviour experiment mode id which doesn't exist
                return JsonResponse(resp_data)
            if public_check == True:
                ceNetwork.public = True
                ceNetwork.save()
            else:
                ceNetwork.public = False
                ceNetwork.save()
            resp_data = {'response': 1, 'msg': 'ceNetwork public field set correctly'}
            return JsonResponse(resp_data)
    resp_data = {'response': -1, 'msg': 'Bad request'}  # Bad request
    return JsonResponse(resp_data)


@login_required
def view_NeuralNetworks(request):
    neuralNetworks_orig_my = m_net.get_owned_nets(request.user)
    neuralNetworks_orig_curated = m_net.get_curated_nets()

    neuralNetworks_shared = m_net.share_CENetwork.objects.all()

    # for model in neuralNetworks_shared:
    #    if model.user == request.user:
    #        if model.ceNetwork not in neuralNetworks_orig:
    #            neuralNetworks_orig.add(model.ceNetwork)

    return render(request, "booking/view_neuralNetworks.html",
                  dict(neuralNetworks_my=neuralNetworks_orig_my,
                       neuralNetworks_curated=neuralNetworks_orig_curated,
                       share=neuralNetworks_shared,
                       users=User.objects.all()))


@login_required
def share_NetworkModels(request):

    neuralNetworks_orig_my = m_net.get_owned_nets(request.user)
    neuralNetworks_orig_curated = m_net.get_curated_nets()
    neuralNetworks_orig_public = m_net.get_public_nets(request.user)

    return render(request, "booking/share_NetworkModels.html",
                  dict(neuralNetworks_my=neuralNetworks_orig_my,
                       neuralNetworks_curated = neuralNetworks_orig_curated,
                       neuralNetworks_public = neuralNetworks_orig_public,
                       users=User.objects.all(),
                       models_shared=m_net.share_CENetwork.objects.all())
                  )


@login_required
def view_RTWs(request):
    rtws_orig = m_rtw.RTW_CONF.objects.filter(Q(owner=request.user)).order_by('name')

    return render(request, "booking/view_RTWs.html",
                  dict(rtws=rtws_orig, users=User.objects.all())
                  )


@login_required
def reserve(request):
    if request.method == 'POST':
        reservationDelete = request.POST.getlist("reservationDelete", "")
        behavExpAdd = request.POST.get("behavExpAdd", "")
        wormConfAdd = request.POST.get("wormConfAdd", "")
        description = request.POST.get("description", "")
        if 'deleteReservation' in request.POST:
            if (not reservationDelete):
                messages.error(request, 'No reservation selected to delete')
            else:
                # Delete reservation
                # If experiment has more than one creator, the creator is deleted
                # IF experiment has only on creator left, do the following
                # If experiment needs to be either in WAITING or ABORTED state
                # If experiment has a PE_result or RB_results, it cannot be deleted
                for reservation in reservationDelete:
                    reservation_object_instance = m.Reservation.objects.get(uuid=reservation)
                    if (len(reservation_object_instance.creator.all()))>1:
                        reservation_object_instance.creator.remove(request.user)
                    elif (reservation_object_instance.status == "WAITING" or reservation_object_instance.status == "ABORTED" or reservation_object_instance.status == "ERROR") and reservation_object_instance.pe_result == None:
                        try:
                            m.Reservation.objects.filter(uuid=reservation).delete()
                        except Exception as e:
                            messages.warning(request, 'Cannot delete the Reservation' + secure_exception_to_str(e))
                            logger.error(
                                'Strange error while deleting Reservation:' + secure_exception_to_str(
                                    e))
                            return render(request, "booking/reservation.html",
                                          dict(reservations=m.Reservation.objects.all(),
                                               behaviourExperiments=behaviourExperimentType_model.objects.all()))
                        messages.success(request, 'Reservation deleted correctly')
                    else:
                        messages.warning(request, 'Cannot delete the Reservation, since status is not WAITING or ABORTED or ERROR and / or has some locomotion or readback results')
        elif 'addReservation' in request.POST:
            if (not behavExpAdd or not wormConfAdd):
                messages.error(request, 'No behavioral experiment or worm conf selected to add')
            else:
                try:
                    behaviouralExperiment = behaviourExperimentType_model.objects.get(pk=behavExpAdd)
                    if (m.Reservation.objects.filter(experiment=behaviouralExperiment, worm_conf=wormConfAdd)):
                        previousReservation = m.Reservation.objects.get(experiment=behaviouralExperiment,
                                                                        worm_conf=wormConfAdd)
                        if previousReservation.creator.filter(id=request.user.pk):
                            warning_message = 'The given experiment is already in the reservation list by the same creator=> ', 'behaviouralExperiment=>', previousReservation.experiment, '; worm_conf=>', previousReservation.worm_conf
                            messages.warning(request, warning_message)
                        else:
                            previousReservation.creator.add(request.user)
                            previousReservation.save()
                            success_message = 'The given experiment was reserved previously by another user, you have been ' \
                                              'added as creator to it'
                            messages.success(request, success_message)
                    else:
                        rb_result = m.RB_results()
                        post = rb_result.save()
                        if description == "":
                            description = 'BehavExp description:' + str(behaviouralExperiment.description) + '; network_name:' + str(m_rtw.RTW_CONF.objects.filter(pk=int(wormConfAdd))[0].network.name) + '; Recording_profile_name: ' + str (m_rtw.RTW_CONF.objects.filter(pk=int(wormConfAdd))[0].name)
                        reservation = m.Reservation(experiment=behaviouralExperiment, worm_conf=wormConfAdd,
                                                    rb_result=rb_result, description=description)
                        if m.Reservation.objects.all().aggregate(Max('sim_id')) == None:
                            reservation.sim_id = 1
                        else:
                            reservation.sim_id = int(m.Reservation.objects.all().aggregate(Max('sim_id')).get('sim_id__max'))+1
                        post = reservation.save()
                        reservation.creator.add(request.user)
                        messages.success(request, 'New reservation added=>' + str(reservation.uuid))
                except IntegrityError as e:
                    logger.error("IntegrityError" + secure_exception_to_str(e))
                    messages.warning(request, 'The given reservation is already defined' + secure_exception_to_str(e))
                except ObjectDoesNotExist as e:
                    logger.error("ObjectDoesNotExist, Seems that some of the components of the reservation was deleted on the meantime, please try again" + secure_exception_to_str(e))
                    messages.warning(request, 'Seems that some of the components of the reservation was deleted on the meantime, please try again')
    # Query restful to get the list of worm conf
    # Code disabled for uploading to GitHub

    # CA_BUNDLE = os.path.join(BASE_DIR,"https-certificates/1.crt")
    # csrftoken = request.META.get('CSRF_COOKIE', None)
    # payload = {'user': request.user}
    # # print 'payload=>', payload
    # url_referer = 'https://' + request.get_host() + reverse('reserve')
    # headers = {'Content-Type': 'application/json', "X-CSRFToken": csrftoken, 'Referer': url_referer}
    # #################################################################################
    # #For NUIG integrations - change the url name in reverse('worm_conf_per_user') below
    # #################################################################################
    # url = 'https://' + request.get_host() + reverse('worm_conf_per_user')
    # # print 'url', url
    # try:
    #     cookies = dict(request.COOKIES)
    #     #################################################################################
    #     # For NUIG integrations - Final deployment, use a self-signed / paid certificate and enable the line
    #     # with verify=CA_BUNDLE. Right now is commented to work with runserver_plus (FOR DEVELOPMENT),
    #     # since we (GE and RA) were not able to get it working with any self-signed certificate
    #     #################################################################################
    #     # response = requests.post(url, data=payload, verify=CA_BUNDLE,  headers=headers, cookies=cookies)
    #     response = requests.post(url, data=payload, verify=False, headers=headers, cookies=cookies)
    #
    #     worm_confs_user = response.json
    #
    # except Exception as inst:
    #     print 'except request to NUIG', sys.exc_info()[0]
    #     print 'inst args: ', inst.args
    #     worm_confs_user = []
    worm_confs_user = []
    return render(request, "booking/reservation.html", dict(reservations=m.Reservation.objects.all(),
                                                            behaviourExperiments=behaviourExperimentType_model.objects.all(),
                                                            worm_confs_user=worm_confs_user))


@login_required
def jointExperimentReview(request, pe_result_uuid):
    PE_result = m.PE_results.objects.get(uuid=pe_result_uuid)
    PE_result_files = PE_result.pe_results_files.all()
    PE_results_path = ""
    for result_file in PE_result_files:
        if result_file.file_order == 0:
            PE_results_path = result_file.results_file
            PE_results_path = settings.MEDIA_URL + str(PE_results_path)
            last_slash = PE_results_path.rfind("/")
            PE_results_path = PE_results_path[:last_slash + 1]
    if PE_results_path == "":
        PE_results_path = "-1"
    return render(request, "booking/jointExperimentReview.html", {
        'PE_results_path': PE_results_path, 'behavExp': PE_result.reservation_for_pe_result.experiment.uuid, 'neurons': Neuron.objects.order_by('name'), 'sim_id' : PE_result.reservation_for_pe_result.sim_id})


@login_required
def experimentReview(request, pe_result_uuid):
    PE_result = m.PE_results.objects.get(uuid=pe_result_uuid)
    PE_result_files = PE_result.pe_results_files.all()
    PE_results_path = ""
    for result_file in PE_result_files:
        if result_file.file_order == 0:
            PE_results_path = result_file.results_file
            PE_results_path = settings.MEDIA_URL + str(PE_results_path)
            last_slash = PE_results_path.rfind("/")
            PE_results_path = PE_results_path[:last_slash + 1]
    if PE_results_path == "":
        PE_results_path = "-1"
    return render(request, "booking/experimentReview.html", {
        'PE_results_path': PE_results_path, 'behavExp': PE_result.reservation_for_pe_result.experiment.uuid})

@user_passes_test(lambda u: u.is_superuser)
@login_required
def errors_review(request):
    if request.method == 'POST':
        uuid = request.POST.get("uuid", "")
        print 'uuid'
        status = request.POST.get("status", "")
        error_admin_updates = request.POST.get("error_admin_updates", "")
        reservation_to_save = m.Reservation.objects.get(uuid=uuid)
        reservation_to_save.status = status
        reservation_to_save.error_admin_updates = error_admin_updates
        reservation_to_save.save()
    Reservations_error = m.Reservation.objects.filter(status="ERROR")
    forms = [Reservation_form(prefix=str(x.pk), instance=x) for x in Reservations_error]
    return render(request, "booking/errors_review.html", {
        'reservations': m.Reservation.objects.all(), 'status_choices': m.Reservation.POLLING_STATUS, 'forms': forms})


@login_required
def abort_experiment(request):
    # GE: Experiment set to 0, should we ask for id and capture it from request?
    # GE: We need to set the experiment to aborted, so we might need to ask the id and replace this 
    payload = '<root><uuid>' + '0' + '</uuid><action>abort</action><timestamp>0</timestamp></root>'
    headers = {'Content-Type': 'application/xml'}
    try:
        result = requests.put(mainURL + 'services', data=payload, headers=headers)
        xml = etree.fromstring(result.content)
    except ConnectionError as e:
        logger.error('ConnectionError: ' + secure_exception_to_str(e))
        return HttpResponse('ConnectionError: Abort SC NOT executed correctly')
    except Exception as e:
        logger.error('Strange XML result received from SC: Either bad query or bad response from SC:' + str(e))
        return HttpResponse('Exception: Abort SC NOT executed correctly')
    status = xml.findtext(".//response")
    reservation_id = xml.findtext(".//response")
    msg = xml.findtext(".//msg")
    if status == '1':
        if id != '-1':
            reservation = m.Reservation.objects.get(pk=reservation_id)
            reservation.status = Reservation.ABORTED
            reservation.save()
        logger.debug('Abort SC executed correctly')
        return HttpResponse('Abort SC executed correctly')
    else:
        logger.error('Abort SC NOT executed correctly')
        return HttpResponse('Abort SC NOT executed correctly')


################    
# SC - API CALLS - That's why I use csrf_exempt here and not above when accessing from web browser
###############
'''
This endpoint is called once all the experiment has been configured and start command has been send
to the IM
The main aim of this endpoint is to fill the start_timestamp, to be able to check in the periodic task
if the experiment needs to be stopped (for future resume)
For initial development - integration, start_timestamp is filled for debug purposes and stop/resume is disabled for the moment
'''


@http_basic_auth
@csrf_exempt
def emulation_started_IM(request):
    try:
        xml_request = etree.fromstring(request.body)
    except XMLSyntaxError as e:
        root = etree.Element('root')
        child = etree.Element('response')
        child.text = '0'
        root.append(child)
        child = etree.Element('msg')
        child.text = 'Request has malformed XML or has been called as a GET + e.message =' + secure_exception_to_str(e)
        root.append(child)
        # pretty string
        s = etree.tostring(root, pretty_print=True)
        logger.debug('0-Request has malformed XML or has been called as a GET')
        return HttpResponse(s, content_type='application/xml')
    reservation_id = xml_request.findtext('uuid')
    if reservation_id == None or reservation_id == '':
        root = etree.Element('root')
        child = etree.Element('response')
        child.text = '0'
        root.append(child)
        child = etree.Element('msg')
        child.text = 'Request does not include a uuid (reservation_id) field'
        root.append(child)
        # pretty string
        s = etree.tostring(root, pretty_print=True)
        logger.debug('0-Request does not include a uuid (reservation_id) field')
        return HttpResponse(s, content_type='application/xml')
    try:
        reservation = m.Reservation.objects.get(uuid=reservation_id)
    except (ObjectDoesNotExist, IndexError):
        root = etree.Element('root')
        child = etree.Element('response')
        child.text = '0'
        root.append(child)
        child = etree.Element('msg')
        child.text = 'Request uuid (reservation_id) does not correspond to a valid uuid'
        root.append(child)
        # pretty string
        s = etree.tostring(root, pretty_print=True)
        logger.debug('0-Request uuid (reservation_id) does not correspond to a valid uuid')
        return HttpResponse(s, content_type='application/xml')
    # get status, y si no es running
    if reservation.status == Reservation.CONFIGURING or reservation.status == Reservation.CONFIGURING_INTERFACE_MANAGER or reservation.status == Reservation.CONFIGURING_PHYSICS_ENGINE or reservation.status == Reservation.RUNNING:
        reservation.status = Reservation.RUNNING
        reservation.start_time = int(time.time())
        reservation.save()
        # XML Response
        ##############
        # create XML 1
        root = etree.Element('root')
        # root.append(etree.Element('child'))
        # another child with text
        child = etree.Element('response')
        child.text = '1'
        root.append(child)
        child = etree.Element('msg')
        child.text = 'Emulation started message received correctly from the SC'
        root.append(child)
        # pretty string
        s = etree.tostring(root, pretty_print=True)
        logger.debug('1-Emulation started message received correctly from the SC')
        # Before Django 1.7 mimetype was used, take into account for future implementations
        return HttpResponse(s, content_type='application/xml')

        # Json Response
        ##############
        # resp_data = {'my_key': 'my value',}
        # return JsonResponse(resp_data)
    else:
        root = etree.Element('root')
        # root.append(etree.Element('child'))
        # another child with text
        child = etree.Element('response')
        child.text = '0'
        root.append(child)
        child = etree.Element('msg')
        # Configuring or running / running is added since, periodic task could be processed before this endpoint call
        child.text = 'Emulation started message received, but not processed since the Booking is not in CONFIGURING or RUNNING status'
        root.append(child)
        # pretty string
        s = etree.tostring(root, pretty_print=True)
        # Before Django 1.7 mimetype was used, take into account for future implementations
        logger.debug(
                '0-Emulation started message received, but not processed since the Booking is not in CONFIGURING or RUNNING status + reservation.status = ' + reservation.status)
        return HttpResponse(s, content_type='application/xml')


'''
The following endpoint is only used  in a stop/resume scenario, when stop is called.
SC calls this once in WAITING_CONTEXT, and PE and IM have finished storing context
Main action => To store the timestamp provided by the SC from which the experiment should continue
when an emulation slot is available
'''


@http_basic_auth
@csrf_exempt
def experiment_context_stored(request):
    try:
        xml_request = etree.fromstring(request.body)
    except XMLSyntaxError as e:
        root = etree.Element('root')
        child = etree.Element('response')
        child.text = '0'
        root.append(child)
        child = etree.Element('msg')
        child.text = 'Request has malformed XML or has been called as a GET + e.message=>' + secure_exception_to_str(e)
        root.append(child)
        # pretty string
        s = etree.tostring(root, pretty_print=True)
        return HttpResponse(s, content_type='application/xml')
    timestamp = xml_request.findtext('timestamp')
    reservation_id = xml_request.findtext('uuid')
    if timestamp == None or reservation_id == None:
        root = etree.Element('root')
        child = etree.Element('response')
        child.text = '0'
        root.append(child)
        child = etree.Element('msg')
        child.text = 'Request does not include a timestamp or uuid (reservation_id) field'
        root.append(child)
        # pretty string
        s = etree.tostring(root, pretty_print=True)
        return HttpResponse(s, content_type='application/xml')
    try:
        reservation = m.Reservation.objects.get(uuid=reservation_id)
    except (ObjectDoesNotExist, IndexError):
        root = etree.Element('root')
        child = etree.Element('response')
        child.text = '0'
        root.append(child)
        child = etree.Element('msg')
        child.text = 'Request uuid (reservation_id) does not correspond to a valid uuid'
        root.append(child)
        # pretty string
        s = etree.tostring(root, pretty_print=True)
        logger.debug('0-Request uuid (reservation_id) does not correspond to a valid uuid')
        return HttpResponse(s, content_type='application/xml')
    reservation.status = Reservation.WAITING_UPLOAD
    reservation.resume_timestamp = timestamp
    reservation.save()
    root = etree.Element('root')
    child = etree.Element('response')
    child.text = '1'
    root.append(child)
    child = etree.Element('msg')
    child.text = 'Experiment context stored message received correctly from the SC'
    root.append(child)
    # pretty string
    s = etree.tostring(root, pretty_print=True)
    # Before Django 1.7 mimetype was used, take into account for future implementations
    return HttpResponse(s, content_type='application/xml')


'''
The main aim of this endpoint is to update the Django Reservation object in the database with DONE for
a finished experiment and WAITING_RESUME for an experiment to be resumed when a experiment slot is available
'''


@http_basic_auth
@csrf_exempt
def experiment_ended(request):
    try:
        xml_request = etree.fromstring(request.body)
    except XMLSyntaxError as e:
        root = etree.Element('root')
        child = etree.Element('response')
        child.text = '0'
        root.append(child)
        child = etree.Element('msg')
        child.text = 'Request has malformed XML or has been called as a GET + e.message=>' + secure_exception_to_str(e)
        root.append(child)
        # pretty string
        s = etree.tostring(root, pretty_print=True)
        return HttpResponse(s, content_type='application/xml')
    reservation_id = xml_request.findtext('uuid')
    if reservation_id == None:
        root = etree.Element('root')
        child = etree.Element('response')
        child.text = '0'
        root.append(child)
        child = etree.Element('msg')
        child.text = 'Request does not include a uuid (reservation_id) field'
        root.append(child)
        # pretty string
        s = etree.tostring(root, pretty_print=True)
        return HttpResponse(s, content_type='application/xml')
    try:
        reservation = m.Reservation.objects.get(uuid=reservation_id)
    except (ObjectDoesNotExist, IndexError):
        root = etree.Element('root')
        child = etree.Element('response')
        child.text = '0'
        root.append(child)
        child = etree.Element('msg')
        child.text = 'Request uuid (reservation_id) does not correspond to a valid uuid'
        root.append(child)
        # pretty string
        s = etree.tostring(root, pretty_print=True)
        logger.debug('0-Request uuid (reservation_id) does not correspond to a valid uuid')
        return HttpResponse(s, content_type='application/xml')
    # TODO: Check if experiment ended is called from a good reservation.status, e.g. Running? Anyone else
    if reservation.resume_timestamp == 0:
        reservation.status = Reservation.DONE
    else:
        reservation.status = Reservation.WAITING_RESUME
    reservation.save()
    root = etree.Element('root')
    child = etree.Element('response')
    child.text = '1'
    root.append(child)
    child = etree.Element('msg')
    child.text = 'Experiment end message received correctly from the SC'
    root.append(child)
    # pretty string
    s = etree.tostring(root, pretty_print=True)
    # Before Django 1.7 mimetype was used, take into account for future implementations
    return HttpResponse(s, content_type='application/xml')

'''
The main aim of this endpoint is to update the Django Reservation object in the database with DONE for
a finished experiment and WAITING_RESUME for an experiment to be resumed when a experiment slot is available
'''


@http_basic_auth
@csrf_exempt
def error_report(request):
    try:
        xml_request = etree.fromstring(request.body)
    except XMLSyntaxError as e:
        root = etree.Element('root')
        child = etree.Element('response')
        child.text = '0'
        root.append(child)
        child = etree.Element('msg')
        child.text = 'Request has malformed XML or has been called as a GET + e.message=>' + secure_exception_to_str(e)
        root.append(child)
        # pretty string
        s = etree.tostring(root, pretty_print=True)
        return HttpResponse(s, content_type='application/xml')
    reservation_id = xml_request.findtext('uuid')
    error_code = xml_request.findtext('error_code')
    logger.error('Emulation error on Reservation: ' + unicode(reservation_id) + ', error_code: ' + unicode(error_code) + ', time now: ' + unicode(datetime.datetime.now()))
    if reservation_id == None:
        root = etree.Element('root')
        child = etree.Element('response')
        child.text = '0'
        root.append(child)
        child = etree.Element('msg')
        child.text = 'Request does not include a uuid (reservation_id) field'
        root.append(child)
        # pretty string
        s = etree.tostring(root, pretty_print=True)
        return HttpResponse(s, content_type='application/xml')
    if error_code == None:
        root = etree.Element('root')
        child = etree.Element('response')
        child.text = '0'
        root.append(child)
        child = etree.Element('msg')
        child.text = 'Request does not include an error_code'
        root.append(child)
        # pretty string
        s = etree.tostring(root, pretty_print=True)
        return HttpResponse(s, content_type='application/xml')
    try:
        reservation = m.Reservation.objects.get(uuid=reservation_id)
    except (ObjectDoesNotExist, IndexError):
        root = etree.Element('root')
        child = etree.Element('response')
        child.text = '0'
        root.append(child)
        child = etree.Element('msg')
        child.text = 'Request uuid (reservation_id) does not correspond to a valid uuid'
        root.append(child)
        # pretty string
        s = etree.tostring(root, pretty_print=True)
        logger.debug('0-Request uuid (reservation_id) does not correspond to a valid uuid')
        return HttpResponse(s, content_type='application/xml')
    # TODO: Check if experiment ended is called from a good reservation.status, e.g. Running? Anyone else
    reservation.status = Reservation.ERROR
    reservation.error_code = error_code
    reservation.save()
    root = etree.Element('root')
    child = etree.Element('response')
    child.text = '1'
    root.append(child)
    child = etree.Element('msg')
    child.text = 'Error report received correctly from the SC'
    root.append(child)
    # pretty string
    s = etree.tostring(root, pretty_print=True)
    # Before Django 1.7 mimetype was used, take into account for future implementations
    return HttpResponse(s, content_type='application/xml')
