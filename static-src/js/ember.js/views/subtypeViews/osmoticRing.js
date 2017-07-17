App.OsmoticRingView = Ember.View.extend({
	willInsertElement: function(){
			$('#modalLoading').modal('show');
		},
		didInsertElement : function () {
			var permanentController = this.get('controller.controllers.permanent');
			var self = this;
			var osmoticController = this.get('controller');
			var permanentModel = permanentController.get('model');
			var data2 = this.get('controller.model.content');
			
			//concentration slider
			var osmoticConcentrationSlider = new Slider('#osmoticConcentrationSlider', {
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
					id : 'osmotic-concentration-slider',
				});
			var items = permanentController.store.all('osmoticRing');
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('osmoticConcentrationSlider', osmoticConcentrationSlider);
			}
			permanentController.set('osmoticConcentrationSlider', osmoticConcentrationSlider);
			self.set('osmoticConcentrationSlider', osmoticConcentrationSlider);
			
			//internal radius slider
			var osmoticInternalSlider = new Slider('#osmoticInternalSlider', {
					range : false,
					max : new Number(100),
					step : 0.1,
					value : data2.get('internalRadius'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('internalRadius', value);
						}
						return value + ' mm';
					},
					id : 'osmotic-internal-slider',
				});
			var items = permanentController.store.all('osmoticRing');
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('osmoticInternalSlider', osmoticInternalSlider);
			}
			permanentController.set('osmoticInternalSlider', osmoticInternalSlider);
			self.set('osmoticInternalSlider', osmoticInternalSlider);
			
			//external radius slider
			var osmoticExternalSlider = new Slider('#osmoticExternalSlider', {
					range : false,
					max : new Number(100),
					step : 0.1,
					value : data2.get('externalRadius'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('externalRadius', value);
						}
						return value + ' mm';
					},
					id : 'osmotic-external-slider',
				});
			var items = permanentController.store.all('osmoticRing');
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('osmoticExternalSlider', osmoticExternalSlider);
			}
			permanentController.set('osmoticExternalSlider', osmoticExternalSlider);
			self.set('osmoticExternalSlider', osmoticExternalSlider);
			$('#modalLoading').modal('hide');
		},
		templateName : "osmoticRing",
	});
