App.DynamicDropTestView = Ember.View.extend({
		didInsertElement : function () {
			var exactController = this.get('controller.controllers.exact');
			var self = this;
			var pointController = this.get('controller');
			var exactModel = exactController.get('model');
			var data2 = this.get('controller.model.content');
			
			//concentration slider
			var ddtConcentrationSlider = new Slider('#ddtConcentrationSlider', {
					range : false,
					min : new Number(1),
					max : new Number(1000),
					step : 0.1,
					value : data2.get('chemicalConcentration'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('chemicalConcentration', value);
						}
						return value + ' mM';
					},
					id : 'dynamicDropTest-concentration-slider',
				});
			var items = exactController.store.all('dynamicDropTest');
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('ddtConcentrationSlider', ddtConcentrationSlider);
			}
			exactController.set('ddtConcentrationSlider', ddtConcentrationSlider);
			self.set('ddtConcentrationSlider', ddtConcentrationSlider);
			
			//drop quantity
			var ddtDropSlider = new Slider('#ddtDropSlider', {
					range : false,
					max : new Number(100),
					step : 0.1,
					value : data2.get('dropQuantity'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('dropQuantity', value);
						}
						return value + ' l';
					},
					id : 'dynamicDropTest-drop-slider',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('ddtDropSlider', ddtDropSlider);
			}
			exactController.set('ddtDropSlider', ddtDropSlider);
			self.set('ddtDropSlider', ddtDropSlider);
			
			//X axis
			var ddtXaxisSlider = new Slider('#ddtXaxisSlider', {
					range : false,
					max : new Number(100),
					step : 0.1,
					value : data2.get('xCoordFromPlateCentre'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('xCoordFromPlateCentre', value);
						}
						return value + ' mm';
					},
					id : 'dynamicDropTest-Xaxis-slider',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('ddtXaxisSlider', ddtXaxisSlider);
			}
			exactController.set('ddtXaxisSlider', ddtXaxisSlider);
			self.set('ddtXaxisSlider', ddtXaxisSlider);
			
			//y axis
			var ddtYaxisSlider = new Slider('#ddtYaxisSlider', {
					range : false,
					max : new Number(100),
					step : 0.1,
					value : data2.get('yCoordFromPlateCentre'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('yCoordFromPlateCentre', value);
						}
						return value + ' mm';
					},
					id : 'dynamicDropTest-Yaxis-slider',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('ddtYaxisSlider', ddtYaxisSlider);
			}
			exactController.set('ddtYaxisSlider', ddtYaxisSlider);
			self.set('ddtYaxisSlider', ddtYaxisSlider);
			
		},
		templateName : "dynamicDropTest",
	});
