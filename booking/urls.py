"""URLs module"""
try:
    from django.conf.urls import patterns, url
except ImportError:
    # Django < 1.4
    from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('booking.views',    
    #Make a new reservation
    url(r'^reserve$', 'reserve', name='reserve'),
    url(r'^share_PE_results$', 'share_PE_results', name='share_PE_results'),
    url(r'^view_PE_results$', 'view_PE_results', name='view_PE_results'),
    url(r'^view_integrated_results$', 'view_integrated_results', name='view_integrated_results'),
    url(r'^share_RB_results$', 'share_RB_results', name='share_RB_results'),
    url(r'^view_RB_results$', 'view_RB_results', name='view_RB_results'),
    url(r'^share_NeuronModels$', 'share_NeuronModels', name='share_NeuronModels'),
    url(r'^neuronModel_make_public$', 'neuronModel_make_public', name='neuronModel_make_public'),
    url(r'^networkModel_make_public$', 'networkModel_make_public', name='networkModel_make_public'),

    url(r'^view_NeuralNetworks$', 'view_NeuralNetworks', name='view_NeuralNetworks'),
    url(r'^share_NetworkModels$', 'share_NetworkModels', name='share_NetworkModels'),
    url(r'^view_RTWs$', 'view_RTWs', name='view_RTWs'),


    url(r'^view_NeuronModels$', 'view_NeuronModels', name='view_NeuronModels'),

    url(r'^emulation_started_IM$', 'emulation_started_IM', name='emulation_started_IM'),
    url(r'^abort_experiment$', 'abort_experiment', name='abort_experiment'),
    url(r'^errors_review$', 'errors_review', name='errors_review'),
    url(r'^error_report$', 'error_report', name='error_report'),

    url(r'^pe_result_make_public$', 'pe_result_make_public', name='pe_result_make_public'),
    url(r'^rb_result_make_public$', 'rb_result_make_public', name='rb_result_make_public'),
    url(r'^experiment_context_stored$', 'experiment_context_stored', name='experiment_context_stored'),
    url(r'^experiment_ended$', 'experiment_ended', name='experiment_ended'),        
    url(r'^experimentReview/(?P<pe_result_uuid>[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})/$', 'experimentReview', name='experimentReview'),
    url(r'^jointExperimentReview/(?P<pe_result_uuid>[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})/$', 'jointExperimentReview', name='jointExperimentReview'),
    
    #Query the status of a reservation
    
    #url(r'^status/', 'status',
    #    name='complete'),
    #
    
    #
    
)
