App.PointSourceLightView = Ember.View.extend({
		didInsertElement : function () {
			var intervalController = this.get('controller.controllers.interval');
			var self = this;
			var pointLightController = this.get('controller');
			var intervalModel = intervalController.get('model');
			var data2 = this.get('controller.model.content');
			
			//waveLength
			var pointLightWavelengthSlider = new Slider('#pointLightWavelengthSlider', {
					range : false,
					min : new Number(250),
					max : new Number(750),
					step : 1,
					value : data2.get('waveLength'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('waveLength', value);
						}
						return value + ' nm';
					},
					id : 'pointligth-wavelength-slider',
				});
			var items = intervalController.store.all('plateTap');
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('pointLightWavelengthSlider', pointLightWavelengthSlider);
			}
			intervalController.set('pointLightWavelengthSlider', pointLightWavelengthSlider);
			self.set('pointLightWavelengthSlider', pointLightWavelengthSlider);
			
			//intensity
			var pointLightIntensitySlider = new Slider('#pointLightIntensitySlider', {
					range : false,
					min: new Number(0)
					max : new Number(1000),
					step : 0.1,
					value : data2.get('intensity'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('intensity', value);
						}
						return value + ' cd';
					},
					id : 'pointligth-intensity-slider',
				});
			var items = intervalController.store.all('plateTap');
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('pointLightIntensitySlider', pointLightIntensitySlider);
			}
			intervalController.set('pointLightIntensitySlider', pointLightIntensitySlider);
			self.set('pointLightIntensitySlider', pointLightIntensitySlider);
			
			//lightingPointDistance
			var pointLightLightingDistanceSlider = new Slider('#pointLightLightingDistanceSlider', {
					range : false,
					max : new Number(1),
					step : 0.01,
					value : data2.get('lightingPointDistance'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('lightingPointDistance', value);
						}
						return value + ' mm';
					},
					id : 'pointligth-lightingPointDistance-slider',
				});
			var items = intervalController.store.all('plateTap');
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('pointLightLightingDistanceSlider', pointLightLightingDistanceSlider);
			}
			intervalController.set('pointLightLightingDistanceSlider', pointLightLightingDistanceSlider);
			self.set('pointLightLightingDistanceSlider', pointLightLightingDistanceSlider);
			
			//lightBeamRadius
			var pointLightBeamSlider = new Slider('#pointLightBeamSlider', {
					range : false,
					max : new Number(1),
					step : 0.01,
					value : data2.get('lightBeamRadius'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('lightBeamRadius', value);
						}
						return value + ' mm';
					},
					id : 'pointligth-lightBeamRadius-slider',
				});
			var items = intervalController.store.all('plateTap');
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('pointLightBeamSlider', pointLightBeamSlider);
			}
			intervalController.set('pointLightBeamSlider', pointLightBeamSlider);
			self.set('pointLightBeamSlider', pointLightBeamSlider);
		},
		templateName : "pointSourceLight",
	});
