App.EnvironmentRoute = Ember.Route.extend({
  model: function(params) {
	  return this.modelFor('experiment').get('environmentDefinition');
  },
  renderTemplate: function() {
    this.render( {into: 'experiment', outlet: 'properties'});
  },
});