App.PlateConfigurationView = Ember.View.extend({
		didInsertElement : function () {
			var controller = this.get('controller');
			var self = this;
			var data = this.get('controller.model.content');
			
			//not implemented yet
			/*var plateDrynessAgeSlider = new Slider('#plateDrynessAgeSlider', {
					range : false,
					max : new Number(255),
					step : 0.1,
					value : data.get('dryness'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('dryness', value);
						}
						return value + '%';
					},
					id : 'plate-dryness-slider',
				});
			var items = controller.store.all('plateConfiguration')
				for (var i = 0; i < items.content.length; i++) {
					items.content[i].set('plateDrynessAgeSlider', plateDrynessAgeSlider);
				}
				controller.set('plateDrynessAgeSlider', plateDrynessAgeSlider);
			self.set('plateDrynessAgeSlider', plateDrynessAgeSlider);*/
			/*$('#lidTrue').click(function () {
				self.set('controller.model.lid', true);
			});
			$('#lidFalse').click(function () {
				self.set('controller.model.lid', false);
			});
			$('#materialAgar').click(function () {
				self.set('controller.model.bottomMaterial', 'A');
			});
			$('#materialGelatin').click(function () {
				self.set('controller.model.bottomMaterial', 'G');
			});
			$('#materialWater').click(function () {
				self.set('controller.model.bottomMaterial', 'W');
			});*/
			$('#shapeCylinder').click(function () {
				self.set('controller.model.shape', 'CY');
			});
			$('#shapeCube').click(function () {
				self.set('controller.model.shape', 'CU');
			});
			$('#shapeHexagon').click(function () {
				self.set('controller.model.shape', 'HE');
			});
		},

	});
