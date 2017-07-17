App.IntervalView = Ember.View.extend({
    classNames:["col-sm-12", "wrap"],
  didInsertElement: function() {
        var eventController = this.get('controller');
			var self = this;
			var eventModel = this.get('controller.model');
			var data = this.get('controller.controllers.experiment.model.experimentDefinition');
			//this.get('controller.controllers.experiment.model.experimentDefinition').then(function (data) {
				var intervalTimeSlider = new Slider('#intervalTimeSlider', {
					range : true,
					value: [eventModel.get('eventStartTime'), eventModel.get('eventStopTime')],
					max : data.get('experimentDuration'),
					step : 1,
					formatter : function (value) {
						if(value.length && value.length > 1){
							var currentModel = eventController.get('model');
							currentModel.set('eventStartTime', value[0]);
							currentModel.set('eventStopTime', value[1]);
						}
						var secs1 = Math.round(value[0]/100);
						var secs2 = Math.round(value[1]/100);
						return secs1/10 + ' s - ' + secs2/10 + ' s';
					},
					id : 'interval-time-slider',
				});
				var items = data.get('interactionAtSpecificTime.content.currentState');
				for(var i = 0; i < items.length; i++){
					items[i].set('intervalTimeSlider', intervalTimeSlider);
				}
				eventController.set('intervalTimeSlider', intervalTimeSlider);
				self.set('intervalTimeSlider', intervalTimeSlider);
			//});
			var controller = App.__container__.lookup("controller:definition");
			var proxySend = jQuery.proxy(controller.send, controller);
			proxySend('setSelectedBox', "inter" + this.get('controller.model.id'));
  },
          
            
});