"""URLs module"""
try:
    from django.conf.urls import patterns, url
except ImportError:
    # Django < 1.4
    from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('behaviouralExperimentDefinition.views',
    url(r'^experimentDefinition_Selection$', 'experimentDefinition_Selection', name='experimentDefinition_Selection'),
    url(r'^experimentDefinition$', 'experimentDefinition', name='experimentDefinition'),
    url(r'^behaviourExperimentClone$', 'clone_behavExp', name='clone_behavExp'),
    url(r'^behavExp_has_reservation$', 'behavExp_has_reservation', name='behavExp_has_reservation'),
    url(r'^worm_conf_per_user$', 'worm_conf_per_user', name='worm_conf_per_user'),    
    url(r'^behavExp_make_public$', 'behavExp_make_public', name='behavExp_make_public'),    
    url(r'^fillExperimentBehaviour$', 'fillExperimentBehaviour', name='fillExperimentBehaviour'),
    url(r'^shareExperimentBehaviour$', 'shareExperimentBehaviour', name='shareExperimentBehaviour'),        
    
    #Query the status of a reservation
    
    #url(r'^status/', 'status',
    #    name='complete'),
    #
    
    #
    
)
