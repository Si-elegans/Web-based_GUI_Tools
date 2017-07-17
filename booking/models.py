import os
from django.db import models
from django.utils.encoding import smart_unicode
from spirit.models import User
from behaviouralExperimentDefinition.models import behaviourExperimentType_model
from datetime import datetime
import uuid
#from django.contrib.auth import get_user_model
#
#
#User = get_user_model()
from django.conf import settings
User = settings.AUTH_USER_MODEL

def generate_new_uuid():
    return str(uuid.uuid4())

# Create your models here.

class PE_results (models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    public = models.BooleanField (default = False, blank=True)
    public_set_date = models.DateTimeField (default=datetime.now)
    users_with_access = models.ManyToManyField (User, related_name='pe_results_accessable', through = 'share_pe_results')
    def __unicode__(self):
        try:
            reservation = self.reservation_for_pe_result
        except:
            reservation = 'Not reservation assigned'
        return "Pe_result: %s, Reservation: %s" % (self.uuid, reservation)
    def save(self, *args, **kwargs):
        if self.uuid is not None:
            try:
                orig = PE_results.objects.get(uuid=self.uuid)
                if orig.public != self.public:
                    self.public_set_date = datetime.now()
            except:  #If it is the first time that is being created then .get() fails and throws an exception
                pass
        super(PE_results, self).save(*args, **kwargs)

###
#Callback function to create folder names as Pe_results/1/ and so on. Used to filled the upload_to in the PE_results model
def get_upload_path(instance, filename):
    return os.path.join(
      "PE_results/%s" % instance.pe_result.uuid, filename)
####

class PE_results_files(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    pe_result = models.ForeignKey (PE_results,related_name='pe_results_files', blank=False)
    #file_order reflects each file saved for a reservation's PE_result
    file_order = models.BigIntegerField(blank=False)
    results_file = models.FileField (upload_to=get_upload_path,blank=False, default='')    
    created = models.DateTimeField(auto_now_add=True)    
    #GE: Added a creator role if he wants to delete results, no clear usage known right now       
    class Meta:
        ordering = ["created"]
        #null_together, the idea is to not allow to fill the same file sequence for a reservation
        unique_together = ("pe_result","file_order")        

    def __unicode__(self):
        PE_results_string = 'PE_results=>' + 'pe_result=>' + unicode(self.pe_result.uuid) +'_' + 'results_file=>' + unicode(self.results_file)  + unicode(self.created)
        return PE_results_string
    
class share_pe_results(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    user = models.ForeignKey(User)
    pe_results = models.ForeignKey (PE_results)    
    shared_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("user","pe_results")
    def __unicode__(self):
           return "id: %s_%s" % (self.user,self.pe_results.uuid)


class RB_results (models.Model):
    public = models.BooleanField (default = False, blank=True)
    public_set_date = models.DateTimeField (default=datetime.now)
    users_with_access = models.ManyToManyField (User, related_name='rb_results_accessable', through = 'share_rb_results')
    def __unicode__(self):
        return "Rb_result: %s" % (self.id, )
    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig = RB_results.objects.get(pk=self.pk)
            if orig.public != self.public:
                self.public_set_date = datetime.now()
        super(RB_results, self).save(*args, **kwargs)


class share_rb_results(models.Model):
    user = models.ForeignKey(User)
    rb_results = models.ForeignKey (RB_results)
    shared_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("user","rb_results")
    def __unicode__(self):
           return "id: %s_%s" % (self.user,self.rb_results)

class Reservation(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    sim_id = models.IntegerField(null=True) #To maintain correspondence between uuid and sim_id im can't handle uuid length
    #for sim_id, when migrations are applied, sim_id -s are filled as null, they need to be filled manually from 1,2,3, incrementally
    #GE: description should contain a brief description including behav exp conf and the model over whi is being tested
    description = models.TextField(max_length=1000, blank=True)
    experiment   = models.ForeignKey(behaviourExperimentType_model,related_name='ReservedExperiment')
    worm_conf = models.BigIntegerField(default = 0, null=False)
    #GE: experiment_id set to behavioural_experiment, but should be later set to experiment, containing both behavioural experiment and neuron model...     
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ManyToManyField(User, related_name='reservation_own')    
    #GE: We will be checking if creator is from the admin group to check its priority
    #GE: Does it make sense that an experiment is defined by a user and launched by another? Launched by the admin?
    pe_result = models.OneToOneField (PE_results,related_name='reservation_for_pe_result',blank=True, null = True)
    rb_result = models.OneToOneField (RB_results,related_name='reservation_for_rb_result',blank=True, null = True)
    #Booking timestamp, from when the simulation has been launched or resumed
    start_time = models.BigIntegerField(default = 0)
    resume_timestamp = models.BigIntegerField(default = 0)
    error_code = models.TextField(max_length=20, blank=True, default='')
    error_admin_updates = models.TextField(max_length=20, blank=True, default='')
    #GE: Should we consider this timestamp from when the SC has issued the start command to the IM? -  deduct the initialisation time 
    #In any case, time should be instantiated in the cloud
    
    
    WAITING = 'WAITING' #Added to the Queue
    WAITING_START='WAITING_START'
    CONFIGURING = 'CONFIGURING'
    CONFIGURING_INTERFACE_MANAGER = 'CONFIGURING_INTERFACE_MANAGER'
    CONFIGURING_PHYSICS_ENGINE = 'CONFIGURING_PHYSICS_ENGINE'  
    RUNNING = 'RUNNING' #Emulation Running
    PAUSED = 'PAUSED'# User debugging
    #We will change into RUNNING state once SC has send me that everything went fine with the IM and start command
    # has been sent to the IM
    WAITING_UPLOAD = 'WAITING_UPLOAD'
    WAITING_CONTEXT = 'WAITING_CONTEXT'    
    WAITING_RESUME = 'WAITING_RESUME' #Stopped because booking time finished, waiting to get another slot
    DONE = 'DONE'  #Experiment finished
    ABORTED = 'ABORTED'  #Experiment aborted
    ERROR = 'ERROR' #Error happened in the emulation system - labserver or IM layers
    
    POLLING_STATUS = ( 
        (WAITING,"WAITING"),
        (WAITING_START,"WAITING_START"),
        (CONFIGURING,"CONFIGURING"),
        (CONFIGURING_INTERFACE_MANAGER,"CONFIGURING_INTERFACE_MANAGER"),
        (CONFIGURING_PHYSICS_ENGINE,"CONFIGURING_PHYSICS_ENGINE"),        
        (RUNNING,"RUNNING"),
        (PAUSED ,"PAUSED"),
        (WAITING_UPLOAD,"WAITING_UPLOAD"),
        (WAITING_CONTEXT,"WAITING_CONTEXT"),
        (WAITING_RESUME,"WAITING_RESUME"),
        (DONE,"DONE"),
        (ABORTED,"ABORTED"),
        (ERROR, "ERROR"),
    )
    status = models.CharField(max_length=1000, blank=False, choices=POLLING_STATUS, default=WAITING)
    #GE: Check how to limit status to certain types ()
    
   
    #GE: timestamp might not be neccessary since SDCP is saved and when restored the emulation will continue from the 
    #timestamp_resume = models.BigIntegerField(default = 0)# Emulation timestamp from which to resume, only used when a simulation is stopped and resumed later
    #GE: Discuss with Pedro if he is considering unsigned long for timestamp or just long, since django by default does not have unsigned long
    #Thread explaining how to use unsigned long in django http://stackoverflow.com/questions/10678102/can-the-django-orm-store-an-unsigned-64-bit-integer-aka-ulong64-or-uint64-in-a 
    
    
    

    class Meta:
        ordering = ["created"]
        #GE: The Experiment and worm's model configuration should have only one reservation,
        #if the user requests the same experiment, the user should be provided with access to results
        #What if it is reserved but has no results yet?
        #For now allow users to define the same reservation more than once
        #unique_together = ("experiment","wormconf")
          

    def __unicode__(self):
        reservation_string = 'Reservation: ' + unicode(self.uuid) + ', STATUS: ' + unicode(self.status) +  ', BehavExp: ' +  unicode(self.experiment.uuid) +', Created: '+ unicode(self.created)
        return reservation_string




