App.PlateTapView = Ember.View.extend({
		didInsertElement : function () {
			var exactController = this.get('controller.controllers.exact');
			var self = this;
			var pointController = this.get('controller');
			var exactModel = exactController.get('model');
			var data2 = this.get('controller.model.content');
			var plateForceSlider = new Slider('#plateForceSlider', {
					range : false,
					max : new Number(1),
					step : 0.01,
					value : data2.get('appliedForce'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('appliedForce', value);
						}
						return value + ' mN';
					},
					id : 'plateTap-force-slider',
				});
			var items = exactController.store.all('plateTap');
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('plateForceSlider', plateForceSlider);
			}
		exactController.set('plateForceSlider', plateForceSlider);
		self.set('plateForceSlider', plateForceSlider);
	},
		templateName : "plateTap",
});
