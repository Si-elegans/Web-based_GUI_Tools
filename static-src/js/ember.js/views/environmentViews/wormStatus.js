App.WormStatusView = Ember.View.extend({
		classNames : [],
		didInsertElement : function () {
			var controller = this.get('controller');
			var self = this;
			var data = this.get('controller.model.content');
			var wormDistanceXSlider = new Slider('#wormDistanceXSlider', {
					range : false,
					min: new Number(-100),
					max : new Number(100),
					step : 0.1,
					value : data.get('xCoordFromPlateCentre'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('xCoordFromPlateCentre', value);
						}
						return value + ' mm';
					},
					id : 'worm-xdistance-slider',
				});
			var items = controller.store.all('wormStatus');
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('wormDistanceXSlider', wormDistanceXSlider);
			}
			controller.set('wormDistanceXSlider', wormDistanceXSlider);
			self.set('wormDistanceXSlider', wormDistanceXSlider);

			var wormDistanceYSlider = new Slider('#wormDistanceYSlider', {
					range : false,
					min: new Number(-100),
					max : new Number(100),
					step : 0.1,
					value : data.get('yCoorDFromPlateCentre'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('yCoorDFromPlateCentre', value);
						}
						return value + ' mm';
					},
					id : 'worm-ydistance-slider',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('wormDistanceYSlider', wormDistanceYSlider);
			}
			controller.set('wormDistanceYSlider', wormDistanceYSlider);
			self.set('wormDistanceYSlider', wormDistanceYSlider);

			var wormAngleSlider = new Slider('#wormAngleSlider', {
					range : false,
					max : new Number(6.28),
					step : 0.01,
					value : data.get('angleRelativeXaxis'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('angleRelativeXaxis', value);
						}
						return value + ' rad';
					},
					id : 'worm-angle-slider',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('wormAngleSlider', wormAngleSlider);
			}
			controller.set('wormAngleSlider', wormAngleSlider);
			self.set('wormAngleSlider', wormAngleSlider);
		},
	});
