App.CubeView = Ember.View.extend({
		didInsertElement : function () {
			var controller = this.get('controller');
			var self = this;
			var data = controller.get('model');
			var sliderId = '#cubeSide1Slider' + data.get('id');
			if ($(sliderId).length) {
				var cubeSide1Slider = new Slider(sliderId, {
						range : false,
						max : new Number(200),
						step : 0.1,
						value : data.get('side1Length'),
						formatter : function (value) {
							var myModel = self.get('controller.model');
							if (myModel) {
								if (myModel.get('side1Length') != null) {
									myModel.set('side1Length', value);
								}
							}
							return value + " mm";
						},
						id : 'cube-side1-slider' + data.get('id'),
					});
				var items = controller.store.all('cube');
				for (var i = 0; i < items.content.length; i++) {
					items.content[i].set('cubeSide1Slider' + data.get('id'), cubeSide1Slider);
				}
				controller.set('cubeSide1Slider' + data.get('id'), cubeSide1Slider);
				self.set('cubeSide1Slider' + data.get('id'), cubeSide1Slider);
			}

			var sliderId = '#cubeSide2Slider' + data.get('id');
			if ($(sliderId).length) {
				var cubeSide2Slider = new Slider(sliderId, {
						range : false,
						max : new Number(200),
						step : 0.1,
						value : data.get('side2Length'),
						formatter : function (value) {
							var myModel = self.get('controller.model');
							if (myModel) {
								if (myModel.get('side2Length') != null) {
									myModel.set('side2Length', value);
								}
							}
							return value + " mm";
						},
						id : 'cube-side2-slider' + data.get('id'),
					});
				for (var i = 0; i < items.content.length; i++) {
					items.content[i].set('cubeSide2Slider' + data.get('id'), cubeSide2Slider);
				}
				controller.set('cubeSide2Slider' + data.get('id'), cubeSide2Slider);
				self.set('cubeSide2Slider' + data.get('id'), cubeSide2Slider);
			}

			var sliderId = '#cubeDepthSlider' + data.get('id');
			if ($(sliderId).length) {
				var cubeDepthSlider = new Slider(sliderId, {
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
						id : 'cube-depth-slider' + data.get('id'),
					});
				for (var i = 0; i < items.content.length; i++) {
					items.content[i].set('cubeDepthSlider' + data.get('id'), cubeDepthSlider);
				}
				controller.set('cubeDepthSlider' + data.get('id'), cubeDepthSlider);
				self.set('cubeDepthSlider' + data.get('id'), cubeDepthSlider);
			}
		},
	});
