from itertools import chain

from django.db import models
from django.db.models import Q

#from django.contrib.auth.models import User, Group

from django.conf import settings

CURATOR_USERNAME = 'galway'

# this is a string
User = settings.AUTH_USER_MODEL

# this should be moved to an enum inside the LemsModel class
class MODEL_TYPES:
    NEURON = 0; SYN = 1; NET = 2


### UTILITY METHODS ###

# curator accessors
def is_curator(user):
    # username checks should be case-insensitive
    if user.username.lower() == get_curator_name().lower():
        return True
    return False


def get_curator_name():
    return CURATOR_USERNAME


#
# Commonly used searches for LemsModel objects
#
def get_lems_models(user, model_type):
    return LemsModel.objects.filter(Q(owner=user))\
                            .filter(Q(model_type=model_type)).order_by('name')


def get_curated_lems_models(model_type):
    return LemsModel.objects.filter(Q(owner__username=get_curator_name()))\
                            .filter(Q(public=True))\
                            .filter(Q(model_type=model_type)).order_by('name')


# We don't include curated models in get_public...
def get_public_lems_models(model_type):
    return LemsModel.objects.filter(Q(public=True))\
                            .filter(~Q(owner__username=get_curator_name()))\
                            .filter(Q(model_type=model_type)).order_by('name')


def get_shared_lems_models(user, model_type):
    # TODO: this should be a deferred query instead of two queries
    shared_ids = share_LemsModel.objects.filter(user=user).\
                                         values_list('lemsModel', flat=True)

    return LemsModel.objects.filter(id__in=shared_ids).\
                             filter(Q(model_type=model_type)).order_by('name')


# All models a user can access
def all_available_models(user, model_type):

    # 1. models, synapses or nets owned by this user
    # 2. also all owned by curator
    # 3. also all shared with everybody
    # 4. also select any shared specifically with this user

    # 1. user's models
    objs = get_lems_models(user, model_type)

    # 2. curator's models ?should we check if user=curator?
    objs = list(chain(objs, get_curated_lems_models(model_type)))

    # 3. shared with everyone
    objs = list(chain(objs, get_public_lems_models(model_type)))

    # 4. shared specifically with this user
    objs = list(chain(objs, get_shared_lems_models(user, model_type)))

    return objs


def all_available_param_models(user, model_type):
    objs = all_available_models(user, model_type)
    param_models = ParameterisedModel.objects.filter(model__in=objs)

    return param_models


### MODEL CLASSES ###

class LemsTypeTag(models.Model):
    tag = models.CharField(max_length=256)

    def __unicode__(self):
        return self.tag

class LemsElement(models.Model):
    name = models.CharField(max_length=256)
    lems_elem = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User)
    public = models.BooleanField(default=False)
    xml = models.TextField()
    component_data = models.TextField(default=False)
    dynamics_text = models.TextField(blank=True, null=True)
    from_file = models.CharField(max_length=256)
    tags = models.ManyToManyField(LemsTypeTag, blank=True)
    extends = models.CharField(max_length=256, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        name = ''
        if self.name:
            name = ' : ' + self.name
        else:
            name = ' : ' + self.xml

        description = ''
        if self.description:
            description = ' : ' + self.description

        return unicode(self.lems_elem + name + description)

class LemsModel(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User)
    public = models.BooleanField(default=False)
    json = models.TextField()

    model_type = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.name + ' : ' +  self.owner.__unicode__())

class share_LemsModel(models.Model):
    user = models.ForeignKey(User)
    lemsModel = models.ForeignKey (LemsModel)
    shared_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("user","lemsModel")
    def __unicode__(self):
           return "id: %s_%s" % (self.user,self.lemsModel)


class ParameterisedModel(models.Model):
    model = models.ForeignKey(LemsModel)

    json_data = models.TextField()

    def __unicode__(self):
        return unicode(self.model.name)


class Lems2FpgaJob(models.Model):
    owner = models.ForeignKey(User)
    lems_model = models.ForeignKey(LemsModel)

    # underscore separated synaptic model ids (LemsModel)
    syn_ids = models.TextField(null=True, blank=True)

    # 0=jlems, 1=isim, 2=fpga
    sim_type = models.PositiveIntegerField(null=False, blank=False)

    # 0=Waiting, 1=Running, 2=Success, 3=Fail
    status = models.PositiveIntegerField(null=False, blank=False)

    lems2fpga_code = models.PositiveIntegerField(null=True, blank=True)
    lems2fpga_message = models.TextField(null=True, blank=True)
    lems2fpga_job_id = models.TextField(null=True, blank=True)

    out_of_date = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def sim_type_str(self):
        sim_type_strs = ['jlems', 'isim', 'fpga']
        return sim_type_strs[self.sim_type]

    def status_str(self):
        status_strs = ['Waiting', 'Running', 'Success', 'Failed']
        return status_strs[self.status]

    def __unicode__(self):
        return unicode(self.lems_model.name + " ; sim: " + str(self.sim_type) + 
                       " ; status: " + str(self.status) + " ; user: " + str(self.owner))

