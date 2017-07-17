# This is to be used in the CloudServer deployment,
# it currently has all the urls for lems_ui, cenet, results_viewer, rtw_ui
from django.conf.urls import patterns, include, url

import lems_ui.views
import cenet.views
import results_viewer.views
import rtw_ui.views
import worm_conf.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djlems.views.home', name='home'),
    # url(r'^djlems/', include('djlems.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^$', lems_ui.views.home),

    url(r'^home/', lems_ui.views.home),

    url(r'^load_file/', lems_ui.views.load_file),

    url(r'^neuron_model/$', lems_ui.views.comp_type_view),
    url(r'^neuron_model/(?P<model_name>[\w|\W]+)/$', lems_ui.views.comp_type_view, name='neuron_model_by_name'),
    url(r'^neuron_model_delete/(?P<model_name>[\w|\W]+)/$', lems_ui.views.delete_neuron_model),

    url(r'^syn_model/$', lems_ui.views.synapse_model),
    url(r'^syn_model/(?P<model_name>[\w|\W]+)/$', lems_ui.views.synapse_model),

    url(r'^hier_details/$', lems_ui.views.hier_details),

    url(r'^type_hierarchy/', lems_ui.views.type_hierarchy),
    url(r'^get_descendants/', lems_ui.views.get_descendants),
    url(r'^get_descendantscomponents/', lems_ui.views.get_descendantscomponents),
    url(r'^component_hierarchy/', lems_ui.views.component_hierarchy),

    url(r'^element_list/', lems_ui.views.element_list),
    url(r'^element_list_custom/', lems_ui.views.element_list_custom),

    url(r'^comp_details/', lems_ui.views.comp_details),
    url(r'^save_model/', lems_ui.views.save_model),
    url(r'^get_model/', lems_ui.views.get_model),
    url(r'^model_to_lems_xml/', lems_ui.views.model_to_lems_xml),
    url(r'^save_component_to_lems_xml/', lems_ui.views.save_component_to_lems_xml),

    url(r'^model_list/', lems_ui.views.model_list),

    url(r'^sched_job/', lems_ui.views.sched_job),

    url(r'^save_comp/$', lems_ui.views.save_comp),
    url(r'^new_comp/$', lems_ui.views.new_comp),
    url(r'^new_comp/(?P<parent_name>[\w|\W]+)/$', lems_ui.views.new_comp),

    ## cenet urls
    ## TODO: these should be moved to a separate urls file
    url(r'^cenet/net_to_lems_xml/', cenet.views.net_to_lems_xml),

    url(r'^network_model_delete/(?P<net_name>[\w|\W]+)/$', cenet.views.delete_network_model),
    url(r'^cenet/$', cenet.views.config_net),
    url(r'^cenet/(?P<net_name>[\w|\W]+)/$', cenet.views.config_net , name = 'worm_conf_details'),

    url(r'^save_net/', cenet.views.save_net),

    url(r'^syn_conns/$', cenet.views.syn_conns),
    url(r'^syn_conns_all/$', cenet.views.syn_conns_all),
    url(r'^syn_conns/(?P<neuron>\w+)/', cenet.views.syn_conns),
    url(r'^getConnectionMap/(?P<neuron>\w+)/', cenet.views.getConnectionMap),

    url(r'^dashboard/', cenet.views.dashboard),


    #results viewer urls
    ## TODO: these should be moved to a separate urls file
    url(r'^results_viewer/', results_viewer.views.results_viewer, name='result_viewer'),

    url(r'^results_viewer_ind/', results_viewer.views.results_viewer_ind),


    #rtw viewer
    url(r'^rtw_ui/dashboard/', rtw_ui.views.view_RTW_dashboard),
    url(r'^rtw_ui/(?P<rtw_id>[\w|\W ]+)/', rtw_ui.views.rtw_ui, name='rtw_by_name'),
    url(r'^rtw_ui/', rtw_ui.views.rtw_ui),
    url(r'^rtw_save_conf/', rtw_ui.views.save_conf),
    url(r'^rtw_get_net/(?P<net_id>\w+)/', rtw_ui.views.get_net),
    url(r'^rtw_get_net/', rtw_ui.views.get_net),
    url(r'^delete_rtw_model/(?P<model_name>[\w|\W]+)/$', rtw_ui.views.delete_rtw_model),



    url(r'^worm_conf_per_user/', worm_conf.views.worm_conf_per_user, name='worm_conf_per_user'),
    url(r'^worm_conf_get_details/(?P<worm_conf>\w+)/', worm_conf.views.worm_conf_get_details),

    url(r'^worm_conf_get_intialisation/(?P<worm_conf>\w+)/', worm_conf.views.worm_conf_get_intialisation),

    url(r'^worm_conf_get_bitfile/(?P<worm_conf>\w+)/(?P<neuron_id>\w+)/', worm_conf.views.worm_conf_get_bitfile),
    url(r'^worm_conf_get_muscle_bitfile/(?P<worm_conf>\w+)/(?P<neuron_id>\w+)/', worm_conf.views.worm_conf_get_muscle_bitfile),

    url(r'^worm_conf_get_metadatafile/(?P<worm_conf>\w+)/(?P<neuron_id>\w+)/', worm_conf.views.worm_conf_get_metadatafile),
    url(r'^worm_conf_get_dmdfile/(?P<worm_conf>\w+)/(?P<dmd_id>\w+)/', worm_conf.views.worm_conf_get_dmdfile),

    # Used to initialise neuron list and connectome in db
    #url(r'^djlems/load_neurons/', cenet.views.load_neurons),
    #url(r'^djlems/load_syns/', cenet.views.load_syns),
)

