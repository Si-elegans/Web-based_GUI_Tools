from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern
from django_notify.urls import get_pattern as get_notify_pattern
from django.contrib import auth

from spirit.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Uncomment this for gunicorn deployment
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'siteLogic.views.home', name='home'),
    url(r'^about/$', 'siteLogic.views.about_us', name='about_us'),
    url(r'^thank-you/$', 'siteLogic.views.thankyou', name='thankyou'),
    url(r'^dashboard', 'siteLogic.views.dashboard', name='dashboard'),
    url(r'^login/$', 'siteLogic.views.login', name='login'),
    #url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'homepage.html'},  name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'},  name='logout'),    
    #url(r'^logout', 'siteLogic.views.logout', name='logout'),
    url(r'^neuronModelDefinition$', 'siteLogic.views.neuronModelDefinition', name='neuronModelDefinition'),
    url(r'^neuronModelLibrary$', 'siteLogic.views.neuronModelLibrary', name='neuronModelLibrary'),
    url(r'^neuronNetworkDefinition$', 'siteLogic.views.neuronNetworkDefinition', name='neuronNetworkDefinition'),
    url(r'^neuronNetworkLibrary$', 'siteLogic.views.neuronNetworkLibrary', name='neuronNetworkLibrary'),       
    url(r'^disconnectSocial$', 'siteLogic.views.disconnectSocial', name='disconnectSocial'),    
    url(r'^forum', include('spirit.urls', namespace="spirit", app_name="spirit")),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^accounts/',include('registration.backends.default.urls')),
    url(r'^restAPI/',include('restAPI.urls')),
    url(r'^ajaxDRFTest$', 'siteLogic.views.ajaxDRFTest', name='ajaxDRFTest'),
    url(r'^support$', 'siteLogic.views.support', name='support'),
    url(r'^support-without-login$', 'siteLogic.views.support_without_login', name='support-without-login'),
    url(r'^booking/', include ('booking.urls')),
    url(r'^behaviouralExperimentDefinition/', include ('behaviouralExperimentDefinition.urls')),

    url(r'^djlems/', include ('lems_ui.urls')),
    
    url(r'^user/password/reset/$', 
        password_reset, 
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="password_reset"),
    url(r'^user/password/reset/done/$',
        password_reset_done),
    #url(r'^user/password/reset/(?P<uidb36>[-\w]+)/(?P<token>[-\w]+)/$',
    #    password_reset_confirm, 
    #   {'post_reset_redirect' : '/user/password/done/'}),
    #url(r'^user/password/reset/confirm/$', 
    #    password_reset_confirm),       
    url(r'^user/password/reset/complete/$', 
        password_reset_complete),
    
    
  

    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
           
)
urlpatterns += patterns('',
    (r'^notifications/', get_nyt_pattern()),
    (r'^notify/', get_notify_pattern()),    
    (r'^wiki/', get_wiki_pattern())
)

# Comment this if for gunicorn deployment
"""
if settings.DEBUG:
    urlpatterns += static (settings.STATIC_URL,
                           document_root=settings.STATIC_ROOT)
    urlpatterns += static (settings.MEDIA_URL,
                           document_root=settings.MEDIA_ROOT)
"""

# Uncomment this for gunicorn deployment
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('', (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT}))
