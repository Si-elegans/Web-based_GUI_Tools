import json
from django.contrib import messages
from behaviouralExperimentDefinition.forms import *
from behaviouralExperimentDefinition.models import behaviourExperimentType_model, shareBehaviouralExperiment
from booking.models import Reservation
#from django.views.decorators.csrf import csrf_exempt
#from mysite.my_decorators import http_basic_auth
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from behaviouralExperimentDefinition import models as m
from spirit.models import User
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, redirect
from django.db import IntegrityError
import logging

logger = logging.getLogger(__name__)
#################
#Json - Rest Views
##################
@login_required
def worm_conf_per_user(request):

    if request.method == 'POST':
        resp_data =  [{'worm_conf':1,'description':'Worm mostly with Integrate and fire'},{'worm_conf':2,'description':'Worm mostly with Hoaxley'}]
        return JsonResponse(resp_data, safe=False)
    else:
        resp_data =  [{'worm_conf':1,'description':'Worm mostly with Integrate and fire'},{'worm_conf':2,'description':'Worm mostly with Hoaxley'}]
        return JsonResponse(resp_data, safe=False)


@login_required
def clone_behavExp(request):    
    if request.method == 'POST':
        payload = json.loads(request.body)
        behaviouralExperiment=payload.get('behaviouralExperiment', '')        
        if behaviouralExperiment != '':
            behaviouralExperiment_instance=behaviourExperimentType_model.objects.get (uuid=behaviouralExperiment)
            num_reservations = Reservation.objects.filter(experiment=behaviouralExperiment_instance) #Try to see if there is a reservation for this behavExp
            if len(num_reservations) > 0:
                resp_data = {'clone': 1,}#If there is a reservation, then we need to respond to directly clone otherwise check exception
            else:
                try:
                    behavioralExp_instance = behaviourExperimentType_model.objects.get(uuid=behaviouralExperiment)
                    try:
                        share_instance = shareBehaviouralExperiment.objects.get (behaviouralExperiment=behavioralExp_instance)
                        resp_data = {'clone': 1,}#Experiment is shared with at least one user so it shouldn't be modified, Clone!!
                    except ObjectDoesNotExist: # If the behavExp it is not shared with specific people
                        if behavioralExp_instance.public == True:
                            resp_data = {'clone': 1,}#Experiment shared publicly so it shouldn't be modified, Clone!!
                        else:
                            if behavioralExp_instance.creator==request.user:
                                resp_data = {'clone': 0,}#No reservation for behavExp and Owner. Save and not clone
                            else:
                                resp_data = {'clone': 1,}#It should not enter this option, since would require to be shared or a query from a non-creator user hacking paths
                                #=>No reservation for behavExp, but not Owner, Clone!
                except ObjectDoesNotExist:
                    resp_data ={'clone':-1, 'error' :'User has send a behaviour experiment mode id which does not exist'} #User has send a behaviour experiment mode id which doesn't exist
            return JsonResponse(resp_data)
    resp_data = {'clone': -1, 'error' :'Bad request'} #Bad request   
    return JsonResponse(resp_data)

@login_required
def behavExp_has_reservation(request):   
   if request.method == 'POST':
       payload = json.loads(request.body)
       behaviouralExperiment=payload.get('behaviouralExperiment', '')        
       if behaviouralExperiment != '':
           try:
               Reservation.objects.get(experiment=behaviouralExperiment) #Try to see if there is a reservation for this behavExp
               resp_data = {'response': 1,}
           except ObjectDoesNotExist :
               try:
                   behavioralExp_instance = behaviourExperimentType_model.objects.get(pk=behaviouralExperiment)
                   resp_data = {'response': 0,}
               except ObjectDoesNotExist:
                   resp_data ={'response':-1, 'error' :'User has send a behaviour experiment mode id which does not exist'} #User has send a behaviour experiment mode id which doesn't exist
           return JsonResponse(resp_data)   
   resp_data = {'response': -1, 'error' :'Bad request'} #Bad request   
   return JsonResponse(resp_data)
@login_required
def behavExp_make_public(request):   
   if request.method == 'POST':
       payload = json.loads(request.body)
       behaviouralExperiment=payload.get('behaviouralExperiment', '')
       public_check = payload.get('public_check', '')    
       if behaviouralExperiment != '':
            try:
               behavioralExp_instance = behaviourExperimentType_model.objects.get(pk=behaviouralExperiment)
            except ObjectDoesNotExist:
                resp_data ={'response':-1, 'msg' :'User has send a behaviour experiment id which does not exist'} #User has send a behaviour experiment mode id which doesn't exist
                return JsonResponse(resp_data)   
            try:
                Reservation.objects.get(experiment=behaviouralExperiment) #Try to see if there is a reservation for this behavExp
                if public_check == True:
                    behavioralExp_instance.public = True
                    behavioralExp_instance.save()
                    resp_data = {'response': 1,'msg':'Behavioral experiment public field set correctly'}
                else:
                    resp_data = {'response': 0,'msg':'Experiment cannot be set unpublic since it has reservations'}
            except ObjectDoesNotExist :
                if public_check == True:
                    behavioralExp_instance.public = True
                    behavioralExp_instance.save()
                else:
                    behavioralExp_instance.public = False
                    behavioralExp_instance.save()
                resp_data = {'response': 1,'msg': 'Behavioral experiment public field set correctly'}               
            return JsonResponse(resp_data)   
   resp_data = {'response': -1, 'msg' :'Bad request'} #Bad request   
   return JsonResponse(resp_data)
#################
#WEBVIEWs
##################

@login_required
def experimentDefinition (request):    
    return render (request, "behaviouralExperimentDefinition/experimentDefinition.html", { 
        })
@login_required
def experimentDefinition_Selection (request):    
    if request.method == 'POST':
        if 'addBehavExp' in request.POST:
            experiment=m.experimentType_model.objects.create(experimentDuration=30000)
            cylinder = m.CylinderType_model.objects.create (length=10, radius= 5)
            plate_conf = m.plateConfigurationType_model.objects.create(lid=False, bottomMaterial='A', dryness=0, shape='CY', Cylinder=cylinder)
            word_data = m.wormDataType_model.objects.create (gender='FH', age=1,stageOfLifeCycle=1,timeOffFood=1)
            worm_status=m.wormStatusType_model.objects.create (wormData=word_data,xCoordFromPlateCentre=1, yCoorDFromPlateCentre=1, angleRelativeXaxis=1)
            crowding = m.crowdingType_model.objects.create (wormsDistributionInPlate = 'Center', wormsInPlate=1)
            environment=m.environmentType_model.objects.create(crowding=crowding,wormStatus=worm_status, plateConfiguration=plate_conf)
            behaviorExp = m.behaviourExperimentType_model.objects.create(experimentDefinition=experiment,environmentDefinition=environment,creator=request.user)
            return redirect('/behaviouralExperimentDefinition/experimentDefinition#/experiment/'+ unicode (behaviorExp.uuid))
        elif 'delBehavExp' in request.POST:
            behavExp_uuid = request.POST['delBehavExp']
            behavExp_object_instance = m.behaviourExperimentType_model.objects.filter(uuid=behavExp_uuid)[0]
            reservation_list=Reservation.objects.filter(experiment=behavExp_object_instance)
            if len(reservation_list) == 0:
                try:
                    m.behaviourExperimentType_model.objects.filter(uuid=behavExp_uuid).delete()
                except Exception as e:
                    messages.warning(request, 'Cannot delete the behavioural experiment' + secure_exception_to_str(e))
                    logger.error(
                        'Strange error while deleting behavioural experiment:' + secure_exception_to_str(
                            e))
                messages.success(request, 'Behavioural experiment deleted correctly')
            else:
                messages.warning(request,
                                     'Cannot delete the behavioural experiment, since it is part of a reservation')


    return render (request, "behaviouralExperimentDefinition/experimentDefinition-selection.html", {
          'behaviouralExperiments' : m.behaviourExperimentType_model.objects.all(),
                               'shared_behavExperiments':m.shareBehaviouralExperiment.objects.all(),
    })

@login_required  
def shareExperimentBehaviour(request):
    if request.method == 'POST':
        users = request.POST.getlist("userExperimentShare","")
        behaviouralExperiments =  request.POST.getlist("behaviouralExperimentShare","")        
        behaviouralExperimentPublic = request.POST.getlist("behaviouralExperimentPublic","")  
        if 'sharePublic' in request.POST:
            #Complete loop through all the experiments to check what has been defined to be public and to set it accordingly
            #GE: This can be improved, maybe using Javascript and using a different view to trigger a single update when cliked over it        
            for  selectedBehaviouralExperiment in m.behaviourExperimentType_model.objects.all():            
                if behaviouralExperimentPublic.count(str(selectedBehaviouralExperiment.pk))>0:
                    selectedBehaviouralExperiment.public = True
                    selectedBehaviouralExperiment.save()
                else:
                    selectedBehaviouralExperiment.public = False
                    selectedBehaviouralExperiment.save()
            messages.success(request,'Your behavioural experiments\' public sharing has been updated. ')
        elif 'sharePeople' in request.POST:         
            if (not behaviouralExperiments or not users):
                messages.error (request, 'No behavioural experiment or user to share with selected')
            else:
                for selectedBehaviouralExperiment in behaviouralExperiments:
                    for selectedUser in users:
                        try:
                            #print "Try barruan"
                            # code that produces error
                            post = m.shareBehaviouralExperiment.objects.create(user=User.objects.get(pk=selectedUser),behaviouralExperiment=m.behaviourExperimentType_model.objects.get(pk=selectedBehaviouralExperiment),)
                        except IntegrityError as e:
                            print {"IntegrityError": e.message}
                            messages.warning(request,'The given share relationship is already defined: User: '+ User.objects.get(pk=selectedUser).username
                                           + ", Behavioural experiment: " + unicode(m.behaviourExperimentType_model.objects.get(uuid=selectedBehaviouralExperiment).uuid) + ", Exception message: "+ str(e.message))
                            return render(request, "behaviouralExperimentDefinition/shareExperimentBehaviour.html",
                                   dict(behaviouralExperiments = m.behaviourExperimentType_model.objects.all() , users = User.objects.all(), share=m.shareBehaviouralExperiment.objects.all())              
                                   ) 
                        messages.success(request,'Thank you for sharing a new behavioural experiment. ' +
                                         'User: '+ User.objects.get(pk=selectedUser).username
                                           + ", Behavioural experiment: " + unicode(m.behaviourExperimentType_model.objects.get(uuid=selectedBehaviouralExperiment).uuid))
    return  render(request, "behaviouralExperimentDefinition/shareExperimentBehaviour.html",
                               dict(behaviouralExperiments = m.behaviourExperimentType_model.objects.all() , users = User.objects.all(), share=m.shareBehaviouralExperiment.objects.all())              
                               )    
@login_required  
def fillExperimentBehaviour(request):
    if request.method == 'GET':
        form = behaviourExperimentType_form()
    else:
        # A POST request: Handle Form Upload
        form = behaviourExperimentType_form(request.POST) # Bind data from request.POST into a PostForm
 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            about = form.cleaned_data['about']
            public = form.cleaned_data['public']
            description = form.cleaned_data['public']
            creator =form.cleaned_data['creator']
            users_with_access =form.cleaned_data['users_with_access']
            ExperimentDefinition = form.cleaned_data['experimentDefinition']
            EnvironmentDefinition =form.cleaned_data['environmentDefinition']
            post = m.behaviourExperimentType_model(about=about,creator=creator,experimentDefinition=ExperimentDefinition,environmentDefinition=EnvironmentDefinition, public=public, )
            post.save()
            for user in users_with_access:
                shareBehaviouralExperiment.objects.create(user=user, behaviouralExperiment= post)
            messages.success(request,'Thank you for adding a new behavioural experiment')
            
            #GE: The following line would allow to display a new page. The example of this page is available in the templates folder
            #return HttpResponseRedirect('/thank-you/')
            
 
    return render(request, 'behaviouralExperimentDefinition/fillExperimentBehaviour.html', {
        'form': form,                              
    })