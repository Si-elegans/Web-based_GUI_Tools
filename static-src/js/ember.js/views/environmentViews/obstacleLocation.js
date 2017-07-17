App.ObstacleLocationView = Ember.View.extend({
		didInsertElement : function () {
			var controller = this.get('controller');
			var self = this;
			var data = controller.get('model');
			var sliderId = '#obstacleDistanceXSlider' + data.get('id');
			if ($(sliderId).length) {
				var obstacleDistanceXSlider = new Slider(sliderId, {
						range : false,
						min: new Number(-100),
						max : new Number(100),
						step : 0.1,
						value : data.get('xCoordFromPlateCentre'),
						formatter : function (value) {
							var myModel = self.get('controller.model');
							if (myModel) {
								if (myModel.get('xCoordFromPlateCentre') != null) {
									myModel.set('xCoordFromPlateCentre', value);
								}
							}
							return value + " mm";
						},
						id : 'obstacle-xdistance-slider' + data.get('id'),
					});
				var items = controller.store.all('obstacleLocation');
				for (var i = 0; i < items.content.length; i++) {
					items.content[i].set('obstacleDistanceXSlider' + data.get('id'), obstacleDistanceXSlider);
				}
				controller.set('obstacleDistanceXSlider' + data.get('id'), obstacleDistanceXSlider);
				self.set('obstacleDistanceXSlider' + data.get('id'), obstacleDistanceXSlider);
			}

			var sliderId = '#obstacleDistanceYSlider' + data.get('id');
			if ($(sliderId).length) {
				var obstacleDistanceYSlider = new Slider(sliderId, {
						range : false,
						min: new Number(-100),
						max : new Number(100),
						step : 0.1,
						value : data.get('yCoorDFromPlateCentre'),
						formatter : function (value) {
							var myModel = self.get('controller.model');
							if (myModel) {
								if (myModel.get('yCoorDFromPlateCentre') != null) {
									myModel.set('yCoorDFromPlateCentre', value);
								}
							}
							return value + " mm";
						},
						id : 'obstacle-xdistance-slider' + data.get('id'),
					});
				for (var i = 0; i < items.content.length; i++) {
					items.content[i].set('obstacleDistanceYSlider' + data.get('id'), obstacleDistanceYSlider);
				}
				controller.set('obstacleDistanceYSlider' + data.get('id'), obstacleDistanceYSlider);
				self.set('obstacleDistanceYSlider' + data.get('id'), obstacleDistanceYSlider);
			}

			var sliderId = '#obstacleStiffnessSlider' + data.get('id');
			if ($(sliderId).length) {
				var obstacleStiffnessSlider = new Slider(sliderId, {
						range : false,
						max : new Number(255),
						step : 0.1,
						value : data.get('Stiffness'),
						formatter : function (value) {
							var myModel = self.get('controller.model');
							if (myModel) {
								if (myModel.get('Stiffness') != null) {
									myModel.set('Stiffness', value);
								}
							}
							return value + " N/m";
						},
						id : 'obstacle-stiffness-slider' + data.get('id'),
					});
				for (var i = 0; i < items.content.length; i++) {
					items.content[i].set('obstacleStiffnessSlider' + data.get('id'), obstacleStiffnessSlider);
				}
				controller.set('obstacleStiffnessSlider' + data.get('id'), obstacleStiffnessSlider);
				self.set('obstacleStiffnessSlider' + data.get('id'), obstacleStiffnessSlider);
			}
		},
	});
