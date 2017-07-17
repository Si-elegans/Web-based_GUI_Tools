App.CylinderView = Ember.View.extend({
		didInsertElement : function () {
			var controller = this.get('controller');
			var self = this;
			var data = controller.get('model');
			var sliderId = '#cylinderLengthSlider' + data.get('id');
			if ($(sliderId).length) {
				var cylinderLengthSlider = new Slider(sliderId, {
						range : false,
						max : new Number(50),
						step : 0.1,
						value : data.get('length'),
						formatter : function (value) {
							var myModel = self.get('controller.model');
							if (myModel) {
								if (myModel.get('length') != null) {
									myModel.set('length', value);
								}
							}
							return value + " mm";
						},
						id : 'cylinder-lenght-slider' + data.get('id'),
					});
				var items = controller.store.all('cylinder')
					for (var i = 0; i < items.content.length; i++) {
						items.content[i].set('cylinderLengthSlider' + data.get('id'), cylinderLengthSlider);
					}
					controller.set('cylinderLengthSlider' + data.get('id'), cylinderLengthSlider);
				self.set('cylinderLengthSlider' + data.get('id'), cylinderLengthSlider);
			}

			var sliderId = '#cylinderRadiusSlider' + data.get('id');
			if ($(sliderId).length) {
				var cylinderRadiusSlider = new Slider(sliderId, {
						range : false,
						max : new Number(100),
						step : 0.1,
						value : data.get('radius'),
						formatter : function (value) {
							var myModel = self.get('controller.model');
							if (myModel) {
								if (myModel.get('radius') != null) {
									myModel.set('radius', value);
								}
							}
							return value + " mm";
						},
						id : 'cylinder-radius-slider' + data.get('id'),
					});
				for (var i = 0; i < items.content.length; i++) {
					items.content[i].set('cylinderRadiusSlider' + data.get('id'), cylinderRadiusSlider);
				}
				controller.set('cylinderRadiusSlider' + data.get('id'), cylinderRadiusSlider);
				self.set('cylinderRadiusSlider' + data.get('id'), cylinderRadiusSlider);
			}
		},
	});
