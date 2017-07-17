from django.contrib import admin

from cenet.models import *

admin.site.register(CENetwork)
admin.site.register(Neuron)
admin.site.register(SynapticConn)
admin.site.register(share_CENetwork)
