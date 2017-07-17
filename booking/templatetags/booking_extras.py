from django import template
from django.core.urlresolvers import reverse
from booking.models import Reservation
from rtw_ui.models import RTW_CONF
import logging

logger = logging.getLogger(__name__)
register = template.Library()

@register.simple_tag
def get_reservation_attr(uuid, attr):
    # print "uuid:" + str (uuid) + ", attr:" + str (attr)
    try:
        obj = getattr(Reservation.objects.get(pk=uuid), attr)
    except:
        obj = ''
    return obj

@register.simple_tag
def get_RTWCONF_url(worm_conf):
    try:
        # print 'worm_conf', worm_conf
        obj = RTW_CONF.objects.get(pk=int(worm_conf))
        # TODO: Future ask NUIG to change rtw_id to rtw_name on the urls.py, is rather a name
        url = reverse('rtw_by_name', kwargs={'rtw_id': obj.name})
    except:
        logger.error("Booking-Templatetags (get_RTWCONF_url) - worm_conf:" + str(worm_conf) + ", does not correspond to any RTW_WONF object, check reservations using it")
        url = ''
    return url

@register.simple_tag
def get_RTWCONF_name(worm_conf):
    try:
        # print 'worm_conf', worm_conf
        obj = RTW_CONF.objects.get(pk=int(worm_conf))
        name = obj.name
    except:
        logger.error(
            "Booking-Templatetags (get_RTWCONF_name) - worm_conf:" + str(worm_conf) + ", does not correspond to any RTW_WONF object, check reservations using it")
        name = ''
    # print 'name', name
    return name

@register.simple_tag
def get_cenet_url(worm_conf):
    try:
        obj = RTW_CONF.objects.get(pk=int(worm_conf))
        # TODO: Future ask NUIG to change net_name to net_id on the urls.py, is rather an id
        url = reverse('worm_conf_details', kwargs={'net_name': obj.network.pk})
    except:
        logger.error(
            "Booking-Templatetags (get_cenet_url) - worm_conf:" + str(worm_conf) + ", does not correspond to any RTW_WONF object, check reservations using it")
        url = ''
    return url

@register.simple_tag
def get_cenet_id(worm_conf):
    try:
        obj = RTW_CONF.objects.get(pk=int(worm_conf))
        id = obj.network.pk
    except:
        logger.error(
            "Booking-Templatetags (get_cenet_name) - worm_conf:" + str(worm_conf) + ", does not correspond to any RTW_WONF object, check reservations using it")
        id = ''
    return id
