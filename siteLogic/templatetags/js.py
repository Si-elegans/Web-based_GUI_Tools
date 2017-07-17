from django.utils.safestring import mark_safe
from django.template import Library
import json

register = Library()


@register.filter(is_safe=True)
def js(obj):
    json_result = json.dumps( [{'email': o.email ,'first_name': o.first_name,
                                   'last_name': o.last_name, 'id': o.pk} for o in obj] )
    #data = serializers.serialize("json", obj,fields=('first_name','last_name', 'username'))    
    return mark_safe(json_result)