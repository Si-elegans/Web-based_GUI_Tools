App.PermanentRoute = Ember.Route.extend({
  model: function(params) {
          var array = this.modelFor('definition').get('experimentWideConf.content.currentState');
	  for(var i = 0; i < array.length; i++){
		if(array[i].id == params.event_id){
			return array[i];
		}
	  }
  },
  renderTemplate: function() {
	this._super();
    this.render( {into: 'definition2', outlet: 'properties2'});
  },
});