App.PointSourceHeatAvoidanceView = Ember.View.extend({
		didInsertElement : function () {
			var intervalController = this.get('controller.controllers.interval');
			var self = this;
			var avoidanceController = this.get('controller');
			var intervalModel = intervalController.get('model');
			var data2 = this.get('controller.model.content');
			
			//temperature
			var avoidanceTemperatureSlider = new Slider('#avoidanceTemperatureSlider', {
					range : false,
					max : new Number(100),
					step : 0.1,
					value : data2.get('temperature'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('temperature', value);
						}
						return value + 'ºC';
					},
					id : 'avoidance-temperature-slider',
				});
			var items = intervalController.store.all('pointSourceHeatAvoidance');
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('avoidanceTemperatureSlider', avoidanceTemperatureSlider);
			}
			intervalController.set('avoidanceTemperatureSlider', avoidanceTemperatureSlider);
			self.set('avoidanceTemperatureSlider', avoidanceTemperatureSlider);
			
			//distance
			var avoidanceDistanceSlider = new Slider('#avoidanceDistanceSlider', {
					range : false,
					max : new Number(1),
					step : 0.01,
					value : data2.get('heatPointDistance'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('heatPointDistance', value);
						}
						return value + ' mm';
					},
					id : 'avoidance-distance-slider',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('avoidanceDistanceSlider', avoidanceDistanceSlider);
			}
			intervalController.set('avoidanceDistanceSlider', avoidanceDistanceSlider);
			self.set('avoidanceDistanceSlider', avoidanceDistanceSlider);
			
		},
		templateName : "pointSourceHeatAvoidance",
	});
