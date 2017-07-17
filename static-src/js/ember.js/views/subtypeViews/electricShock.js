App.ElectricShockView = Ember.View.extend({
		didInsertElement : function () {
			var intervalController = this.get('controller.controllers.interval');
			var self = this;
			var shockController = this.get('controller');
			var intervalModel = intervalController.get('model');
			var data2 = this.get('controller.model.content');
			
			//shock Duration Slider
			var shockDurationSlider = new Slider('#shockDurationSlider', {
					range : false,
					max : new Number(100),
					step : 1,
					value : data2.get('shockDuration'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('shockDuration', value);
						}
						return value + ' ms';
					},
					id : 'shock-Duration-slider',
				});
			var items = intervalController.store.all('electricShock');
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('shockDurationSlider', shockDurationSlider);
			}
			intervalController.set('shockDurationSlider', shockDurationSlider);
			self.set('shockDurationSlider', shockDurationSlider);
			
			//shock Amplitude Slider
			var shockAmplitudeSlider = new Slider('#shockAmplitudeSlider', {
					range : false,
					max : new Number(100),
					step : 0.1,
					value : data2.get('amplitude'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('amplitude', value);
						}
						return value + ' nA';
					},
					id : 'shock-amplitude-slider',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('shockAmplitudeSlider', shockAmplitudeSlider);
			}
			intervalController.set('shockAmplitudeSlider', shockAmplitudeSlider);
			self.set('shockAmplitudeSlider', shockAmplitudeSlider);
			
			//shock Frequency Slider
			var shockFrequencySlider = new Slider('#shockFrequencySlider', {
					range : false,
					max : new Number(100),
					step : 0.01,
					value : data2.get('shockFrequency'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('shockFrequency', value);
						}
						return value + ' Hz';
					},
					id : 'shock-frequency-slider',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('shockFrequencySlider', shockFrequencySlider);
			}
			intervalController.set('shockFrequencySlider', shockFrequencySlider);
			self.set('shockFrequencySlider', shockFrequencySlider);
			
			
		},
		templateName : "electricShock",
	});
