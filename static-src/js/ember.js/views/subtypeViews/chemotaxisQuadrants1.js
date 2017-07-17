App.ChemotaxisQuadrants1View = Ember.View.extend({
		willInsertElement: function(){
			$('#modalLoading').modal('show');
		},
		didInsertElement : function () {
			var permanentController = this.get('controller.controllers.permanent');
			var self = this;
			var quad1Controller = this.get('controller');
			var permanentModel = permanentController.get('model');
			var data2 = this.get('controller.model.content');
			var quad1ConcentrationSlider = new Slider('#quad1ConcentrationSlider', {
					range : false,
					min : new Number(1),
					max : new Number(1000),
					step : 0.1,
					value : data2.get('quadrantChemicalConcentration'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('quadrantChemicalConcentration', value);
						}
						return value + ' mM';
					},
					id : 'chemotaxisQuadrants1-concentration-slider',
				});
			var items = permanentController.store.all('chemotaxisQuadrants1');
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('quad1ConcentrationSlider', quad1ConcentrationSlider);
			}
			permanentController.set('quad1ConcentrationSlider', quad1ConcentrationSlider);
			self.set('quad1ConcentrationSlider', quad1ConcentrationSlider);
			$('#modalLoading').modal('hide');
		},
		templateName : "chemotaxisQuadrants1",
	});
