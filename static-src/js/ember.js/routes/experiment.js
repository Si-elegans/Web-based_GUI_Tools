App.ExperimentRoute = Ember.Route.extend({
  model: function(params) {
	return this.store.find('behaviouralExperiment', params.experiment_id);
  },
});