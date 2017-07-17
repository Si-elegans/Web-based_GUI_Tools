App.ChemotaxisQuadrants2View = Ember.View.extend({
		willInsertElement: function(){
			$('#modalLoading').modal('show');
		},
		didInsertElement : function () {
			var permanentController = this.get('controller.controllers.permanent');
			var self = this;
			var quad2Controller = this.get('controller');
			var permanentModel = permanentController.get('model');
			var data2 = this.get('controller.model.content');
			
			//chemical 1 concentration slider
			var quad2ConcentrationSlider1 = new Slider('#quad2ConcentrationSlider1', {
					range : false,
					min : new Number(1),
					max : new Number(1000),
					step : 0.1,
					value : data2.get('quadrant_1_ChemicalConcentration'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('quadrant_1_ChemicalConcentration', value);
						}
						return value + ' mM';
					},
					id : 'chemotaxisQuadrants2-concentration-slider1',
				});
			var items = permanentController.store.all('chemotaxisQuadrants2');
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('quad2ConcentrationSlider1', quad2ConcentrationSlider1);
			}
			permanentController.set('quad2ConcentrationSlider1', quad2ConcentrationSlider1);
			self.set('quad2ConcentrationSlider1', quad2ConcentrationSlider1);
			
			//chemical 2 concentration slider
			var quad2ConcentrationSlider2 = new Slider('#quad2ConcentrationSlider2', {
					range : false,
					min : new Number(1),
					max : new Number(1000),
					step : 0.1,
					value : data2.get('quadrant_2_ChemicalConcentration'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('quadrant_2_ChemicalConcentration', value);
						}
						return value + ' mM';
					},
					id : 'chemotaxisQuadrants2-concentration-slider2',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('quad2ConcentrationSlider2', quad2ConcentrationSlider2);
			}
			permanentController.set('quad2ConcentrationSlider2', quad2ConcentrationSlider2);
			self.set('quad2ConcentrationSlider2', quad2ConcentrationSlider2);
			
			//barrier chemical concentration slider
			var quad2BarrierConcentrationSlider = new Slider('#quad2BarrierConcentrationSlider', {
					range : false,
					min : new Number(1),
					max : new Number(1000),
					step : 0.1,
					value : data2.get('quadrantBarrierChemicalConcentration'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('quadrantBarrierChemicalConcentration', value);
						}
						return value + ' mM';
					},
					id : 'chemotaxisQuadrants2-barrier-slider',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('quad2BarrierConcentrationSlider', quad2BarrierConcentrationSlider);
			}
			permanentController.set('quad2BarrierConcentrationSlider', quad2BarrierConcentrationSlider);
			self.set('quad2BarrierConcentrationSlider', quad2BarrierConcentrationSlider);
			$('#modalLoading').modal('hide');
		},
		templateName : "chemotaxisQuadrants2",
	});
