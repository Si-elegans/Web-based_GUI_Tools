from social.backends.google import GooglePlusAuth
from django.core.files.base import ContentFile
import urllib2


def saveAvatar(backend, user, response, *args, **kwargs):
    if isinstance(backend, GooglePlusAuth):
        if response.get('image') and response['image'].get('url'):            
            url = response['image'].get('url')
            ext = url.split('.')[-1]            
            user.avatar.save(
               '{0}_social.jpg'.format(user.username),
               ContentFile(urllib2.urlopen(url).read()),
               save=False
            )            
            user.save()