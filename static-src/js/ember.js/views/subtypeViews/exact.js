App.ExactView = Ember.View.extend({
		classNames:["col-sm-12", "wrap"],
		didInsertElement : function () {
			var eventController = this.get('controller');
			var self = this;
			var eventModel = this.get('controller.model');
			var data = this.get('controller.controllers.experiment.model.experimentDefinition');
			
			//description
			
			//time
			//this.get('controller.controllers.experiment.model.experimentDefinition').then(function (data) {
				var exactTimeSlider = new Slider('#exactTimeSlider', {
					range : false,
					max : new Number(data.get('experimentDuration')),
					step : 1,
					value : eventModel.get('eventTime'),
					formatter : function (value) {
						var currentModel = eventController.get('model');
						currentModel.set('eventTime', value);
						var secs = Math.round(value/100);
						return secs/10 + ' s';
					},
					id : 'exact-time-slider',
				});
				var items = data.get('interactionAtSpecificTime.content.currentState');
				for(var i = 0; i < items.length; i++){
					items[i].set('exactTimeSlider', exactTimeSlider);
				}
				eventController.set('exactTimeSlider', exactTimeSlider);
				self.set('exactTimeSlider', exactTimeSlider);
			//});
			var controller = App.__container__.lookup("controller:definition");
			var proxySend = jQuery.proxy(controller.send, controller);
			proxySend('setSelectedBox', "exact" + this.get('controller.model.id'));
		},
	});
