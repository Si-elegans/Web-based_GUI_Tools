App.HexagonView = Ember.View.extend({
		didInsertElement : function () {
			var controller = this.get('controller');
			var self = this;
			var data = controller.get('model');
			var sliderId = '#hexagonSideSlider' + data.get('id');
			if ($(sliderId).length) {
				var hexagonSideSlider = new Slider(sliderId, {
						range : false,
						max : new Number(100),
						step : 0.1,
						value : data.get('sideLength'),
						formatter : function (value) {
							var myModel = self.get('controller.model');
							if (myModel) {
								if (myModel.get('sideLength') != null) {
									myModel.set('sideLength', value);
								}
							}
							return value + " mm";
						},
						id : 'hexagon-side-slider' + data.get('id'),
					});
				var items = controller.store.all('hexagon')
					for (var i = 0; i < items.content.length; i++) {
						items.content[i].set('hexagonSideSlider' + data.get('id'), hexagonSideSlider);
					}
					controller.set('hexagonSideSlider' + data.get('id'), hexagonSideSlider);
				self.set('hexagonSideSlider' + data.get('id'), hexagonSideSlider);
			}

			var sliderId = '#hexagonDepthSlider' + data.get('id');
			if ($(sliderId).length) {
				var hexagonDepthSlider = new Slider(sliderId, {
						range : false,
						max : new Number(50),
						step : 0.1,
						value : data.get('depth'),
						formatter : function (value) {
							var myModel = self.get('controller.model');
							if (myModel) {
								if (myModel.get('depth') != null) {
									myModel.set('depth', value);
								}
							}
							return value + " mm";
						},
						id : 'hexagon-depth-slider' + data.get('id'),
					});
				for (var i = 0; i < items.content.length; i++) {
					items.content[i].set('hexagonDepthSlider' + data.get('id'), hexagonDepthSlider);
				}
				controller.set('hexagonDepthSlider' + data.get('id'), hexagonDepthSlider);
				self.set('hexagonDepthSlider' + data.get('id'), hexagonDepthSlider);
			}
		},
	});
