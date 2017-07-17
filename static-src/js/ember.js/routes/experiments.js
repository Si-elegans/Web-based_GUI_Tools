App.ExperimentsRoute = Ember.Route.extend({
  model: function(params) {
	return this.store.find('behaviouralExperiment');
  }
});