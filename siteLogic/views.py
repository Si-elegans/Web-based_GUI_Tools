#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import json
import logging
from siteLogic.utils import secure_exception_to_str
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from social.backends.utils import load_backends, user_backends_data, get_backend
from django.contrib.auth import authenticate, login as auth_login # auth_login renamed from login to avoid recursive calls
# http://stackoverflow.com/questions/1134476/django-login-takes-exactly-1-argument-2-given-error
from django.contrib.auth import logout as auth_logout
from social.actions import do_disconnect
from social.backends.google import GooglePlusAuth
from django import forms
from siteLogic.forms import support_request_form
from behaviouralExperimentDefinition import models as m
from lems_ui.models import share_LemsModel, LemsModel
from cenet.models import share_CENetwork, CENetwork
from booking import models as mbok
from spirit.models import User, Comment
from wiki.models import Article, ArticleRevision
from social.apps.django_app.default.models import UserSocialAuth
from django.core.mail import send_mail
from datetime import datetime,date, timedelta

# Get an instance of a logger
logger = logging.getLogger(__name__)


#!!!!!!!!!!!!! Note !!!!!!!!!!!!!!!!!!!!
#
#If you're using Django's render_to_response() shortcut to populate a template with the contents of a dictionary,
#your template will be passed a Context instance by default (not a RequestContext).
#To use a RequestContext in your template rendering, use the render() shortcut which is the same as a call
#to render_to_response() with a context_instance argument that forces the use of a RequestContext.

# Create your views here.

def about_us(request):
    return render (request,"about_us.html",
                               {})

def home (request):
    return render (request,"homepage.html",                              
                               {})
def thankyou (request):    
    return render  (request,"thankyou.html",                               
                               {                               
                               })
def google_login(request):
  # Create a 'context' dictionary,
  # populate it with the current time
  # and return it
  scope = ' '.join(getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_SCOPE',None))  
  context = {}
  context['plus_id'] = getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY',None)
  context['plus_scope'] = scope
  return context

def context(**extra):
    
    return dict({
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
        'plus_scope': scope
    }, **extra)

def logoutPipeline (strategy, entries, user_storage, *args, **kwargs):
    #This is used in the python-social-auth disconnect pipeline check SOCIAL_AUTH_DISCONNECT_PIPELINE in settings.py
    return redirect('/logout')
    

def login(request):    
    if request.method == 'GET':
        nextPage = request.GET.get('next','/dashboard/')
    else:
        nextPage = request.POST.get('next','/dashboard/')

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    if username and password:
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                #messages.success (request, 'Success') #Not necessary since if login is valid, page is redirected and navbar changes
                # Redirect to a success page.
                if nextPage == "":#given the request gets above, the line below is not being used
                    return HttpResponseRedirect('/dashboard/')
                else:
                    return HttpResponseRedirect(nextPage)
                #return redirect('/dashboard/')
            else:
                # Return a 'disabled account' error message
                messages.error (request, 'disabled account')
                return render(request, "homepage.html",  {'next':
                    nextPage })
        else:
            # Return an 'invalid login' error message.
            messages.error (request, 'invalid login')
            return render(request, "homepage.html",  {'next':
                    nextPage })
    else:
            # Return an 'invalid login' error message.
            messages.error (request, 'invalid login')
            return render(request, "homepage.html",  {'next':
                    nextPage})

@login_required
def dashboard (request):        
    #########
    # Reservations for dashboard
    #####
    i = 0
    reservations_dashboard=[]
    reservations_super_users=[]
    reservations_regular_users=[]
    if request.user.is_superuser:
        for reserve in  mbok.Reservation.objects.all():
            if reserve.status == 'WAITING':
                try: 
                    creators=reserve.creator.all()
                    for creator in creators:     
                        if creator.is_superuser:
                            reservations_super_users.append (reserve)
                            break
                except Exception as e:
                    logger.error( 'Error when accessing creators corresponding to a reservation:' + secure_exception_to_str (e))                    
        for reserve_super in reservations_super_users:
            if i==4:
                break
            else:                    
                try: 
                    creators=reserve_super.creator.all()
                    for creator in creators:     
                       if creator == request.user:                                      
                            reserve_dashboard = dict (uuid =  reserve_super.uuid, position= reservations_super_users.index(reserve_super) )
                            reservations_dashboard.append (reserve_dashboard)                        
                            i=i+1
                except Exception as e:
                    logger.error( 'Error when accessing creators corresponding to a reservation:' + secure_exception_to_str (e))
        if len(reservations_super_users)>0:
            my_list =  filter(lambda x: request.user in x.creator.all(), reservations_super_users)            
            pending_reservation = len(my_list)
        else:
            pending_reservation = 0        
    else:
        for reserve in  mbok.Reservation.objects.all():
            if reserve.status == 'WAITING':
                only_non_super_user = True
            try:
                creators=reserve.creator.all()
                for creator in creators: 
                    if creator.is_superuser:
                        only_non_super_user = False
                        break
                if only_non_super_user== True:
                        reservations_regular_users.append (reserve)
            except Exception as e:
                    logger.error( 'Error when accessing creators corresponding to a reservation:' + secure_exception_to_str (e))                   
        pending_reservation = len(reservations_super_users)
        for reserve_regular in reservations_regular_users:
            if i==4:
                break
            else:
                try:
                    creators=reserve_regular.creator.all()
                    for creator in creators:     
                       if creator == request.user:                                      
                            reserve_dashboard = dict (uuid = reserve_regular.uuid, position= reservations_regular_users.index(reserve_regular) )
                            reservations_dashboard.append (reserve_dashboard)                        
                            i=i+1
                except Exception as e:
                    logger.error( 'Error when accessing creators corresponding to a reservation:' + secure_exception_to_str (e))                    
        if len(reservations_regular_users)>0:
            my_list =  filter(lambda x: request.user in x.creator.all(), reservations_regular_users)            
            pending_reservation = len(my_list)
        else:
            pending_reservation = 0  
    
    if i<4:
      while i!=4:
         reserve_dashboard = dict ( uuid =  -1, position= 0)
         reservations_dashboard.append (reserve_dashboard)
         i=i+1
    #print 'reservations_dashboard',reservations_dashboard
    #print 'reservations_dashboard',json.dumps(reservations_dashboard)
    #########
    # Last obtained results for dashboard
    ########
    j = 0    
    pe_results_dashboard = []
    sorted_pe_results_dashboard = []
    for pe_result in mbok.PE_results.objects.all():
        if j==4:
            break
        else:
            try:
                if request.user in pe_result.reservation_for_pe_result.creator.all():
                    if pe_result.pe_results_files.filter(file_order=0)[0]:
                        pe_result_to_add = dict (uuid = pe_result.uuid, created= pe_result.pe_results_files.filter(file_order=0)[0].created)
                        pe_results_dashboard.append (pe_result_to_add)  
                        j=j+1
            except Exception as e:
                logger.error( 'Error when accessing reservation corresponding to pe_result:'+ unicode (pe_result.uuid) + ' ' + secure_exception_to_str (e))
    if len (pe_results_dashboard)>0:
        sorted_pe_results_dashboard = sorted(pe_results_dashboard, key=lambda shared: shared['created'], reverse = True)    
    if len(sorted_pe_results_dashboard)>0:
        pe_results_dashboard_time = filter(lambda x: x['created'].date()>(date.today()-timedelta (days=14)), sorted_pe_results_dashboard)    
        last_results = len(pe_results_dashboard_time)
    else:
        last_results = 0
    if j<4:
      while j!=4:
         pe_result_to_add = dict ( uuid =  -1, created = 0)
         sorted_pe_results_dashboard.append (pe_result_to_add)
         j=j+1
    #########
    # Last shared with me for dashboard
    ########
    NM_shared_me = []
    NC_shared_me = []
    BE_shared_me = []
    PER_shared_me = []
    RBR_shared_me = []

    sorted_merged_shared_list = []
    try:
        for NCS in share_CENetwork.objects.all():
            if NCS.user == request.user:
                NCS_to_add = dict(uuid=NCS.ceNetwork.name, type='NCS', created=NCS.shared_date)
                NC_shared_me.append(NCS_to_add)
        for NMS in share_LemsModel.objects.all():
            if NMS.user == request.user:
                NMS_to_add = dict(uuid=NMS.lemsModel.name, type='NMS', created=NMS.shared_date)
                NM_shared_me.append (NMS_to_add)
        for BES in m.shareBehaviouralExperiment.objects.all():
            if BES.user == request.user:
                BES_to_add = dict (uuid=BES.behaviouralExperiment.uuid, type='BES', created=BES.shared_date)
                BE_shared_me.append (BES_to_add)
        for PERS in mbok.share_pe_results.objects.all():
            if PERS.user == request.user:
                PERS_to_add = dict (uuid=PERS.pe_results.uuid, type='PERS', created=PERS.shared_date)
                PER_shared_me.append(PERS_to_add)
        for RBRS in mbok.share_rb_results.objects.all():
            if RBRS.user == request.user:
                if RBRS.rb_results.reservation_for_rb_result.uuid == None:
                    RBRS_to_add = dict(uuid=0, type='RBRS', created=RBRS.shared_date)
                else:
                    RBRS_to_add = dict(uuid=RBRS.rb_results.reservation_for_rb_result.sim_id, type='RBRS',
                                       created=RBRS.shared_date)
                PER_shared_me.append(RBRS_to_add)

    except Exception as e:
                logger.error( 'Error when accessing elements from share_pe_results:' + secure_exception_to_str (e))                
    merged_shared_list =  NC_shared_me + NM_shared_me + BE_shared_me + PER_shared_me + RBR_shared_me
    # print 'merged_shared_list=>',merged_shared_list
    if len (merged_shared_list)>0:
        sorted_merged_shared_list = sorted(merged_shared_list, key=lambda shared: shared['created'], reverse = True)
    if len(sorted_merged_shared_list)>0:                
        sorted_merged_shared_list_time = filter(lambda x: x['created'].date()>(date.today()-timedelta (days=14)), sorted_merged_shared_list)    
        last_shared_me = len(sorted_merged_shared_list_time)
    else:
        last_shared_me = 0
    #print 'sorted_merged_shared_list=>',sorted_merged_shared_list
    while len (sorted_merged_shared_list)<4:
        shared_to_add =  dict (uuid = -1, type='', created = 0)
        sorted_merged_shared_list.append (shared_to_add)            
    #print 'sorted_merged_shared_list_final=>',sorted_merged_shared_list
    
    #########
    # Last shared with public - this would be based on the date of creation not shared
    ########

    NM_public = []
    NC_public = []
    BE_public = []
    PER_public = []
    RBR_public = []
    sorted_merged_public_list =[]
    try:
        for NM in LemsModel.objects.all():
            if NM.public == True:
                NMP_to_add = dict (uuid= NM.name, type = 'NMP', last_modified = NM.updated)
                NM_public.append (NMP_to_add)
        for NC in CENetwork.objects.all():
            if NC.public == True:
                NCP_to_add = dict (uuid= NM.name, type = 'NCP', last_modified = NC.updated)
                NC_public.append (NCP_to_add)
        for BEP in m.behaviourExperimentType_model.objects.all():
            if BEP.public == True:
                BEP_to_add = dict (uuid= BEP.uuid, type = 'BEP', last_modified = BEP.public_set_date)
                BE_public.append (BEP_to_add)
        for PERP in mbok.PE_results.objects.all():
            if PERP.public == True:            
                PERP_to_add = dict (uuid = PERP.uuid, type='PERP', last_modified = PERP.public_set_date)
                PER_public.append(PERP_to_add)
        for RBRP in mbok.RB_results.objects.all():
            if RBRP.public == True:
                if RBRP.reservation_for_rb_result.uuid == None:
                    RBRP_to_add = dict(uuid=0, type='RBRP', last_modified=RBRP.public_set_date)
                else:
                    RBRP_to_add = dict(uuid=RBRP.reservation_for_rb_result.sim_id, type='RBRP', last_modified=RBRP.public_set_date)
                RBR_public.append(RBRP_to_add)

    except Exception as e:
                logger.error( 'Error when accessing elements from share_pe_results:' + secure_exception_to_str (e))                          
    merged_public_list = NM_public + NC_public + BE_public + PER_public + RBR_public
    #print 'merged_public_list=>',merged_public_list
    if len(merged_public_list)>0:
        sorted_merged_public_list = sorted(merged_public_list, key=lambda shared: shared['last_modified'], reverse = True)
    if len(sorted_merged_public_list)>0:                
        sorted_merged_public_list_time = filter(lambda x: x['last_modified'].date()>(date.today()-timedelta (days=14)), sorted_merged_public_list)    
        last_made_public = len(sorted_merged_public_list_time)
    else:
        last_made_public = 0
    #print 'sorted_merged_public_list=>',sorted_merged_public_list
    while len (sorted_merged_public_list)<4:
        public_to_add =  dict (uuid = -1, type='', created = 0)
        sorted_merged_public_list.append (public_to_add)            
    # print 'sorted_merged_public_list_final=>',sorted_merged_public_list [:4]
           
    #########
    # Spirit forum 
    ########
    
    forum_dashboard =[]
    sorted_forum_dashboard =[]
    try:
        for comment in Comment.objects.all():
            #url to create in template => https://localhost:8000/forumtopic/3/topiko/#c3
            if comment.is_removed!=True:
                try:
                    forum_to_add = dict (social_type='forum',topic = comment.topic.pk, username= comment.user, topic_slug =comment.topic.slug , comment = comment.pk, comment_content=comment.comment_own.all()[0].comment_html , last_modified = comment.comment_own.all()[0].date )
                    forum_dashboard.append (forum_to_add)
                except:
                    forum_to_add = dict (social_type='forum',topic = comment.topic.pk, username= comment.user, topic_slug =comment.topic.slug , comment = comment.pk, comment_content=comment.comment_html,  last_modified = comment.date )
                    forum_dashboard.append (forum_to_add)
    except Exception as e:
        logger.error( 'Error when accessing elements from forum:' + secure_exception_to_str (e))                          
    if len (forum_dashboard)>0:
        sorted_forum_dashboard = sorted(forum_dashboard, key=lambda shared: shared['last_modified'], reverse = True)   
    if len(sorted_forum_dashboard)>0:                
        sorted_forum_dashboard_time = filter(lambda x: x['last_modified'].date()>(date.today()-timedelta (days=14)), sorted_forum_dashboard)    
        forum_len = len(sorted_forum_dashboard_time)
    else:
        forum_len = 0
        
    #########
    # wiki 
    ########
    wiki_dashboard =[]
    sorted_wiki_dashboard =[]
    sorted_social_dashboard =[]
    try:
        for article in Article.objects.all():
            #url to create in template => https://localhost:8000/wiki/ => root https://localhost:8000/wiki/kkkakakka/
            if article.current_revision.deleted != True:
                wiki_to_add = dict (social_type='wiki', topic = article.pk, title=article.current_revision.title, username= article.current_revision.user,content=article.current_revision.content ,last_modified = article.modified )
                wiki_dashboard.append (wiki_to_add)
    except Exception as e:
        logger.error( 'Error when accessing elements from wiki:' + secure_exception_to_str (e))                          
    if len (wiki_dashboard)>0:
        sorted_wiki_dashboard = sorted(wiki_dashboard, key=lambda shared: shared['last_modified'], reverse = True)   
    if len(sorted_wiki_dashboard)>0:                
        sorted_wiki_dashboard_time = filter(lambda x: x['last_modified'].date()>(date.today()-timedelta (days=14)), sorted_wiki_dashboard)    
        wiki_len = len(sorted_wiki_dashboard_time)
    else:
        wiki_len = 0
    ### Merge sorted_wiki and sorted_forum
    sorted_social_dashboard = sorted_wiki_dashboard + sorted_forum_dashboard
    sorted_social_dashboard = sorted(sorted_social_dashboard, key=lambda shared: shared['last_modified'], reverse = True)   
    
    ### If len <8 fill up to 8 with "empty" values
    while len (sorted_social_dashboard)<8:
        social_to_add =  dict (topic = -1, topic_slug = '', comment = -1 , comment_content='', last_modified='')
        sorted_social_dashboard.append (social_to_add)    
    dashboard_number = dict (pending_reservation = pending_reservation, last_results= last_results, last_shared_me= last_shared_me, last_made_public= last_made_public, social_len = forum_len+wiki_len)
    
    return render  (request,"dashboard.html",                               
                               {'reservations' :  reservations_dashboard, 'pe_results_files' : sorted_pe_results_dashboard[:4],
                               'shared_me':sorted_merged_shared_list [:4], 'public_made':sorted_merged_public_list [:4],'dashboard_number':dashboard_number, 'social_dashboard':sorted_social_dashboard[:8],
                               })
@login_required
def ajaxDRFTest (request):    
    return render(request, "ajaxDRF-test.html", {  })

def support_without_login (request):
    if request.method == 'GET':
        form = support_request_form()
    else:
        # A POST request: Handle Form Upload
        form = support_request_form(request.POST) # Bind data from request.POST into a PostForm

        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            send_mail('[SupportRequest]['+ str(email) + '] '+str(subject), str(body), str(email),
    [settings.SUPPORT_MAILING_LIST], fail_silently=False)
            #from_email (email) => Gmail will not let you spoof where the email came from. (http://stackoverflow.com/questions/6803009/the-email-from-in-django-send-mail-function-not-working)
            #fail_silently: A boolean. If it?s False, send_mail will raise an smtplib.SMTPException. See the smtplib docs for a list of possible exceptions, all of which are subclasses of SMTPException.
            messages.success(request,'Your support request has been send, we will come back to you when possible')
        else:
            messages.failure (request, 'Support request not sent due to a failed form validation')


    return render(request, 'support-without-login.html', {
        'form': form})

@login_required
def support (request):    
    if request.method == 'GET':
        form = support_request_form()
    else:
        # A POST request: Handle Form Upload
        form = support_request_form(request.POST) # Bind data from request.POST into a PostForm
 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']                                    
            send_mail('[SupportRequest]['+ str(email) + '] '+str(subject), str(body), str(email),
    [settings.SUPPORT_MAILING_LIST], fail_silently=False)
            #from_email (email) => Gmail will not let you spoof where the email came from. (http://stackoverflow.com/questions/6803009/the-email-from-in-django-send-mail-function-not-working)
            #fail_silently: A boolean. If it?s False, send_mail will raise an smtplib.SMTPException. See the smtplib docs for a list of possible exceptions, all of which are subclasses of SMTPException.    
            messages.success(request,'Your support request has been send, we will come back to you when possible')
        else:
            messages.failure (request, 'Support request not sent due to a failed form validation')
            
            
    return render(request, 'support.html', {
        'form': form})
    
        
        
        

@login_required
def neuronModelLibrary (request):
    
    return render (request, "neuronModelLibrary.html",      {})   
@login_required
def neuronModelDefinition (request):    
    return render (request, "neuronModelDefinition.html", {})
@login_required
def neuronNetworkDefinition (request):
       
    
    return render (request, "neuronNetworkDefinition.html",  {})
@login_required
def neuronNetworkLibrary (request):       
    
    return render (request, "neuronNetworkLibrary.html",  {})

def disconnectSocial (request):       
    return render (request,"disconnectSocial.html",{'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)})



#Not used but could contain interesting code for future needs

#def logoutAndCheckSocialDisconnect(request):
#    """Logs out user"""
#    ##if social logged
#    #    #disconnectWithRevoke
#    #    user_backends_data 
#    print "logoutAndCheckSocialDisconnect"
#    user = request.user
#    try:
#        socialHandler = user.social_auth.get(provider='google-plus')
#        #GE: this would require improvement if other social backends are added
#        backends = load_backends (settings.AUTHENTICATION_BACKENDS)         
#        googlePlusBackEnd = get_backend(backends, 'google-plus')     
#        #response = googlePlusBackEnd.disconnect(user, socialHandler.id)                                      
#        do_disconnect (googlePlusBackEnd, user, socialHandler.id)
#    except:
#        #GE: user.social_auth.get launches an exception "UserSocialAuth matching query does not exist.", I think I should find a more cleaner way to do this and avoid using try / except
#        #Initially I was comparing socialHandler not being None, but the exception was launched before
#        auth_logout(request)
#        return redirect('/')
