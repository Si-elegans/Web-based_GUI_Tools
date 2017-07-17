from django.contrib import admin

from lems_ui.models import *

admin.site.register(LemsTypeTag)
admin.site.register(LemsModel)
admin.site.register(ParameterisedModel)
admin.site.register(Lems2FpgaJob)
admin.site.register(share_LemsModel)


def make_public(modeladmin, request, queryset):
    queryset.update(public=True)
make_public.short_description = "Mark public"
def make_private(modeladmin, request, queryset):
    queryset.update(public=False)
make_private.short_description = "Mark private"

class LemsElementAdmin(admin.ModelAdmin):
    actions = [make_public,make_private]

admin.site.register(LemsElement, LemsElementAdmin)
