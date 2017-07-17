from django.contrib import admin
from django.utils.translation import ugettext as _

from django_nyt import models
from django_nyt import settings


class SettingsAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    list_display = ('user', 'interval',)


class SubscriptionAdmin(admin.ModelAdmin):
    raw_id_fields = ('settings',)
    list_display = ('display_user', 'notification_type', 'display_interval',)

    def display_user(self, instance):
        return instance.settings.user
    display_user.short_description = _("user")

    def display_interval(self, instance):
        return instance.settings.interval
    display_interval.short_description = _("interval")


if settings.ENABLE_ADMIN:
    admin.site.register(models.NotificationType)
    admin.site.register(models.Notification)
    admin.site.register(models.Settings, SettingsAdmin)
    admin.site.register(models.Subscription, SubscriptionAdmin)