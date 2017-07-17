App.ExactRoute = Ember.Route.extend({
  model: function(params) {
      //return this.store.find('interactionAtSpecificTime',params.event_id);
	  var array = this.modelFor('definition').get('interactionAtSpecificTime.content.currentState');
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
  actions:{
	didTransition: function(){
		/*var controller = this.get('controller');
		var eventController = this.get('controller.controllers.event');
		var model = this.get('controller.model');
		var exactTimeSlider = eventController.get('exactTimeSlider');
		console.log(exactTimeSlider);
		if(exactTimeSlider){
			this.get('controller.controllers.experiment.model.experimentDefinition').then(function (data) {
				exactTimeSlider.options.max = new Number(data.get('experimentDuration'));
				exactTimeSlider.setValue(model.get('eventTime'));
			});
		}
		controller.updateEventTime();*/
	}
  }
});