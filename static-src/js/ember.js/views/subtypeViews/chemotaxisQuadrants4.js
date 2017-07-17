App.ChemotaxisQuadrants4View = Ember.View.extend({
		willInsertElement: function(){
			$('#modalLoading').modal('show');
		},
		didInsertElement : function () {
			var permanentController = this.get('controller.controllers.permanent');
			var self = this;
			var quad1Controller = this.get('controller');
			var permanentModel = permanentController.get('model');
			var data2 = this.get('controller.model.content');
			
			//chemical 1 concentration slider
			var quad4ConcentrationSlider1 = new Slider('#quad4ConcentrationSlider1', {
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
					id : 'chemotaxisQuadrants4-concentration-slider1',
				});
			var items = permanentController.store.all('chemotaxisQuadrants4');
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('quad4ConcentrationSlider1', quad4ConcentrationSlider1);
			}
			permanentController.set('quad4ConcentrationSlider1', quad4ConcentrationSlider1);
			self.set('quad4ConcentrationSlider1', quad4ConcentrationSlider1);
			
			//chemical 2 concentration slider
			var quad4ConcentrationSlider2 = new Slider('#quad4ConcentrationSlider2', {
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
					id : 'chemotaxisQuadrants4-concentration-slider2',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('quad4ConcentrationSlider2', quad4ConcentrationSlider2);
			}
			permanentController.set('quad4ConcentrationSlider2', quad4ConcentrationSlider2);
			self.set('quad4ConcentrationSlider2', quad4ConcentrationSlider2);
			
			//chemical 3 concentration slider
			var quad4ConcentrationSlider3 = new Slider('#quad4ConcentrationSlider3', {
					range : false,
					min : new Number(1),
					max : new Number(1000),
					step : 0.1,
					value : data2.get('quadrant_3_ChemicalConcentration'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('quadrant_3_ChemicalConcentration', value);
						}
						return value + ' mM';
					},
					id : 'chemotaxisQuadrants4-concentration-slider3',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('quad4ConcentrationSlider3', quad4ConcentrationSlider3);
			}
			permanentController.set('quad4ConcentrationSlider3', quad4ConcentrationSlider3);
			self.set('quad4ConcentrationSlider3', quad4ConcentrationSlider3);
			
			//chemical 4 concentration slider
			var quad4ConcentrationSlider4 = new Slider('#quad4ConcentrationSlider4', {
					range : false,
					min : new Number(1),
					max : new Number(1000),
					step : 0.1,
					value : data2.get('quadrant_4_ChemicalConcentration'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('quadrant_4_ChemicalConcentration', value);
						}
						return value + ' mM';
					},
					id : 'chemotaxisQuadrants4-concentration-slider4',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('quad4ConcentrationSlider4', quad4ConcentrationSlider4);
			}
			permanentController.set('quad4ConcentrationSlider4', quad4ConcentrationSlider4);
			self.set('quad4ConcentrationSlider4', quad4ConcentrationSlider4);
			
			//barrier chemical concentration slider
			var quad4BarrierConcentrationSlider = new Slider('#quad4BarrierConcentrationSlider', {
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
					id : 'chemotaxisQuadrants4-barrier-slider',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('quad4BarrierConcentrationSlider', quad4BarrierConcentrationSlider);
			}
			permanentController.set('quad4BarrierConcentrationSlider', quad4BarrierConcentrationSlider);
			self.set('quad4BarrierConcentrationSlider', quad4BarrierConcentrationSlider);
			$('#modalLoading').modal('hide');
		},
		templateName : "chemotaxisQuadrants4",
	});
