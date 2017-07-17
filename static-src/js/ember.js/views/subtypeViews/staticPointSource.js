App.StaticPointSourceView = Ember.View.extend({
	willInsertElement: function(){
			$('#modalLoading').modal('show');
		},
		didInsertElement : function () {
			var permanentController = this.get('controller.controllers.permanent');
			var self = this;
			var spsController = this.get('controller');
			var permanentModel = permanentController.get('model');
			var data2 = this.get('controller.model.content');
			
			//concentration slider
			var spsConcentrationSlider = new Slider('#spsConcentrationSlider', {
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
					id : 'staticPointSource-concentration-slider',
				});
			var items = permanentController.store.all('staticPointSource');
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('spsConcentrationSlider', spsConcentrationSlider);
			}
			permanentController.set('spsConcentrationSlider', spsConcentrationSlider);
			self.set('spsConcentrationSlider', spsConcentrationSlider);
			
			//drop quantity
			var spsDropSlider = new Slider('#spsDropSlider', {
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
					id : 'staticPointSource-drop-slider',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('spsDropSlider', spsDropSlider);
			}
			permanentController.set('spsDropSlider', spsDropSlider);
			self.set('spsDropSlider', spsDropSlider);
			
			//X axis
			var spsXaxisSlider = new Slider('#spsXaxisSlider', {
					range : false,
					min : new Number(-100),
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
					id : 'staticPointSource-Xaxis-slider',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('spsXaxisSlider', spsXaxisSlider);
			}
			permanentController.set('spsXaxisSlider', spsXaxisSlider);
			self.set('spsXaxisSlider', spsXaxisSlider);
			
			//y axis
			var spsYaxisSlider = new Slider('#spsYaxisSlider', {
					range : false,
					min : new Number(-100),
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
					id : 'staticPointSource-Yaxis-slider',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('spsYaxisSlider', spsYaxisSlider);
			}
			permanentController.set('spsYaxisSlider', spsYaxisSlider);
			self.set('spsYaxisSlider', spsYaxisSlider);
			$('#modalLoading').modal('hide');
		},
		templateName : "staticPointSource",
	});
