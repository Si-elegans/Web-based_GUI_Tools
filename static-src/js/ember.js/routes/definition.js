App.DefinitionRoute = Ember.Route.extend({
  renderTemplate: function() {
	this._super();
    this.render('definition', {outlet: 'timeline', controller: 'definition', view: 'definition'});
	this.render( 'definition2', {outlet: 'properties', controller: 'definition', view: 'definition2'});
  },
  model: function(params) {
      return this.modelFor('experiment').get('experimentDefinition');
  },
});