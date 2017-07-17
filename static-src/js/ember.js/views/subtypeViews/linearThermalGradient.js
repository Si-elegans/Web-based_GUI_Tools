App.LinearThermalGradientView = Ember.View.extend({
		didInsertElement : function () {
			var permanentController = this.get('controller.controllers.permanent');
			var self = this;
			var linearController = this.get('controller');
			var permanentModel = permanentController.get('model');
			var data2 = this.get('controller.model.content');
			
			//left edge slider
			var gradientLeftSlider = new Slider('#gradientLeftSlider', {
					range : false,
					max : new Number(100),
					step : 0.1,
					value : data2.get('temperatureLeftHorizontal'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('temperatureLeftHorizontal', value);
						}
						return value + 'ºC';
					},
					id : 'linearThermalGradient-left-slider1',
				});
			var items = permanentController.store.all('linearThermalGradient');
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('gradientLeftSlider', gradientLeftSlider);
			}
			permanentController.set('gradientLeftSlider', gradientLeftSlider);
			self.set('gradientLeftSlider', gradientLeftSlider);
			
			//right edge slider
			var gradientRightSlider = new Slider('#gradientRightSlider', {
					range : false,
					max : new Number(100),
					step : 0.1,
					value : data2.get('temperatureRightHorizonal'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('temperatureRightHorizonal', value);
						}
						return value + 'ºC';
					},
					id : 'linearThermalGradient-right-slider1',
				});
			var items = permanentController.store.all('linearThermalGradient');
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('gradientRightSlider', gradientRightSlider);
			}
			permanentController.set('gradientRightSlider', gradientRightSlider);
			self.set('gradientRightSlider', gradientRightSlider);
		},
		templateName : "linearThermalGradient",
	});
