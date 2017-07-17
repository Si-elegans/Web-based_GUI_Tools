from django.db import models

from cenet.models  import CENetwork, Neuron

from django.conf import settings
User = settings.AUTH_USER_MODEL


class RTW_CONF(models.Model):
    name = models.CharField(max_length=256)
    owner = models.ForeignKey(User)
    public = models.BooleanField(default=False)
    network = models.ForeignKey(CENetwork)

    json = models.TextField()
    metadata_init = models.TextField(default="")
    metadata_rtw = models.TextField(default="")


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(str(self.pk) + ' : ' + self.name + ' : ' + self.network.name + ' : ' +  self.owner.__unicode__())



class RTW(models.Model):
    neuron = models.ForeignKey(Neuron)
    variable = models.CharField(max_length=256)
    startTime = models.FloatField()
    endTime = models.FloatField()
    samplingInterval = models.FloatField()

