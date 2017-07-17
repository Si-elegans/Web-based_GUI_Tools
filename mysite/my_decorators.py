from functools import wraps
from lxml import etree
import logging
from django.http import HttpResponse
logger = logging.getLogger(__name__)


#I only use this decorator with REST calls so if failed I respond with an XML
def http_basic_auth(func):
    @wraps(func)
    def _decorator(request, *args, **kwargs):
        from django.contrib.auth import authenticate, login
        if request.META.has_key('HTTP_AUTHORIZATION'):
            authmeth, auth = request.META['HTTP_AUTHORIZATION'].split(' ', 1)
            if authmeth.lower() == 'basic':
                auth = auth.strip().decode('base64')
                username, password = auth.split(':', 1)
                user = authenticate(username=username, password=password)
                if user:
                    request.user = user
                    return func(request, *args, **kwargs)
        # Either they did not provide an authorization head er or
        # something in the authorization attempt failed. Send an XML with
        # <root><response>0</response><msg>Basic http authentication failed</msg></root>S
        #
        #
        #XML Response
        ##############
        # create XML 1
        root = etree.Element('root')
        #root.append(etree.Element('child'))
        # another child with text
        child = etree.Element('response')
        child.text = '0'
        root.append(child)
        child = etree.Element('msg')
        child.text = 'Basic http authentication failed'
        root.append(child)    
        # pretty string
        s = etree.tostring(root, pretty_print=True)
        logger.debug('0-Basic http authentication failed')
        #Before Django 1.7 mimetype was used, take into account for future implementations
        return HttpResponse(s, content_type='application/xml')                        
    return _decorator


