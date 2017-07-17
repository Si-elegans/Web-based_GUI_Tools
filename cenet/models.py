import datetime

from django.db import models
from django.db.models import Q
#from django.contrib.auth.models import User

from django.conf import settings
User = settings.AUTH_USER_MODEL

from lems_ui.models import get_curator_name


#
# Commonly used searches for CENetwork objects
#
def get_owned_nets(user):
    return CENetwork.objects.filter(Q(owner=user)).order_by('name')


def get_curated_nets():
    return CENetwork.objects.filter(Q(owner__username=get_curator_name()))\
                            .order_by('name')


def get_public_nets(model_type):
    return CENetwork.objects.filter(Q(public=True)).order_by('name')


def get_shared_nets(user):
    # TODO: this should be a deferred query instead of two queries
    shared_ids = share_CENetwork.objects.filter(user=user)\
                                        .values_list('ceNetwork', flat=True)

    return CENetwork.objects.filter(id__in=shared_ids)\
                            .order_by('name')


class Neuron(models.Model):
    name = models.CharField(max_length=256)
    data_source = models.CharField(max_length=256)
    info_url = models.CharField(max_length=256, blank=True)

    # fpga_id
    fpga_id = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class SynapticConn(models.Model):
    origin = models.ForeignKey(Neuron, related_name="conns_out")
    target = models.ForeignKey(Neuron, related_name="conns_in")

    type = models.CharField(max_length=256)
    num_conns = models.IntegerField(default=1)
    neurotransmitter = models.CharField(max_length=256)

    data_source = models.CharField(max_length=256)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.origin.name + " -> " + self.target.name + " [" +
                       str(self.num_conns) + "]" + " : " + self.neurotransmitter)

class CENetwork(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User)
    json = models.TextField()
    public = models.BooleanField(default=False)

    # status field
    # "Under Development" for when not used by rtw_conf
    # "Ready for Synthesis" for when used by rtw_conf
    # "Synthesis in Progress" for when used by rtw_conf
    # "Synthesis Complete" for when used by rtw_conf
    # "Synthesis Error" for when used by rtw_conf
    status = models.CharField(max_length=64)

    jobid = models.CharField(max_length=64,default="")
    lems2fpga_message = models.TextField(default=False)
    updated = models.DateTimeField(auto_now=True,default=datetime.datetime.now())

    muscleModel =  models.IntegerField(default=1)

    def __unicode__(self):
        return unicode(str(self.id) + " : " + self.name)

class share_CENetwork(models.Model):
    user = models.ForeignKey(User)
    ceNetwork = models.ForeignKey (CENetwork)
    shared_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("user","ceNetwork")
    def __unicode__(self):
           return "id: %s_%s" % (self.user,self.ceNetwork)

