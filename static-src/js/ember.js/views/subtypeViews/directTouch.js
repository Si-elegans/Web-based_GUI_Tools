App.DirectTouchView = Ember.View.extend({
		didInsertElement : function () {
			var exactController = this.get('controller.controllers.exact');
			var self = this;
			var pointController = this.get('controller');
			var exactModel = exactController.get('model');
			var data2 = this.get('controller.model.content');
					var touchForceSlider = new Slider('#touchForceSlider', {
							range : false,
							min : new Number(10),
							max : new Number(100),
							step : 0.1,
							value : data2.get('appliedForce'),
							formatter : function (value) {
								var myModel = self.get('controller.model');
								if (myModel) {
									myModel.set('appliedForce', value);
								}
								return value + ' µN';
							},
							id : 'touch-force-slider',
						});
					var items = exactController.store.all('directTouch');
					for (var i = 0; i < items.content.length; i++) {
						items.content[i].set('touchForceSlider', touchForceSlider);
					}
					
					exactController.set('touchForceSlider', touchForceSlider);
					self.set('touchForceSlider', touchForceSlider);

					var touchLocationAngleSlider = new Slider('#touchLocationAngleSlider', {
							range : false,
							max : new Number(360),
							step : 1,
							value : data2.get('touchAngle'),
							formatter : function (value) {
								var myModel = self.get('controller.model');
								if (myModel) {
									myModel.set('touchAngle', value);
								}
								return value + ' º';
							},
							id : 'mechano-locationangle-slider',
						});
						
					
					for (var i = 0; i < items.content.length; i++) {
						items.content[i].set('touchLocationAngleSlider', touchLocationAngleSlider);
					}
					
					exactController.set('touchLocationAngleSlider', touchLocationAngleSlider);
					self.set('touchLocationAngleSlider', touchLocationAngleSlider);

					var touchLocationLengthSlider = new Slider('#touchLocationLengthSlider', {
							range : false,
							max : new Number(1),
							step : 0.01,
							value : data2.get('touchDistance'),
							formatter : function (value) {
								var myModel = self.get('controller.model');
								if (myModel) {
									myModel.set('touchDistance', value);
								}
								return value + ' mm';
							},
							id : 'mechano-locationlength-slider',
						});

					
					for (var i = 0; i < items.content.length; i++) {
						items.content[i].set('touchLocationLengthSlider', touchLocationLengthSlider);
					}
					
					exactController.set('touchLocationLengthSlider', touchLocationLengthSlider);
					self.set('touchLocationLengthSlider', touchLocationLengthSlider);


			$('#directEyebrow').click(function () {
				self.set('controller.model.directTouchInstrument', 'EB');
			});
			$('#directVonfrey').click(function () {
				self.set('controller.model.directTouchInstrument', 'VFH');
			});
			$('#directPlatinium').click(function () {
				self.set('controller.model.directTouchInstrument', 'PW');
			});
		},
		templateName : "directTouch",
	});
