App.TemperatureChangeInTimeView = Ember.View.extend({
		didInsertElement : function () {
			var intervalController = this.get('controller.controllers.interval');
			var self = this;
			var temperatureChangeController = this.get('controller');
			var intervalModel = intervalController.get('model');
			var data2 = this.get('controller.model.content');
			
			//initial Temperature
			var temperatureInitialSlider = new Slider('#temperatureInitialSlider', {
					range : false,
					max : new Number(100),
					step : 0.1,
					value : data2.get('initialTemperature'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('initialTemperature', value);
						}
						return value + 'ºC';
					},
					id : 'temperatureChangeInTime-initial-slider',
				});
			var items = intervalController.store.all('temperatureChangeInTime');
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('temperatureInitialSlider', temperatureInitialSlider);
			}
			intervalController.set('temperatureInitialSlider', temperatureInitialSlider);
			self.set('temperatureInitialSlider', temperatureInitialSlider);
			
			//final Temperature
			var temperatureFinalSlider = new Slider('#temperatureFinalSlider', {
					range : false,
					max : new Number(100),
					step : 0.1,
					value : data2.get('finalTemperature'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('finalTemperature', value);
						}
						return value + 'ºC';
					},
					id : 'temperatureChangeInTime-final-slider',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('temperatureFinalSlider', temperatureFinalSlider);
			}
			intervalController.set('temperatureFinalSlider', temperatureFinalSlider);
			self.set('temperatureFinalSlider', temperatureFinalSlider);
			
		},
		templateName : "temperatureChangeInTime",
	});
