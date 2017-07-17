App.CrowdingView = Ember.View.extend({
		didInsertElement : function () {
			var controller = this.get('controller');
			var self = this;
			var data = this.get('controller.model.content');
			
			//slider for worm number (not implemented yet)
			/*var crowdingWormsSlider = new Slider('#crowdingWormsSlider', {
					range : false,
					max : new Number(255),
					step : 0.1,
					value : data.get('wormsInPlate'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('wormsInPlate', value);
						}
						return value + ' worms';
					},
					id : 'crowding-worms-slider',
				});
			var items = controller.store.all('crowding')
				for (var i = 0; i < items.content.length; i++) {
					items.content[i].set('crowdingWormsSlider', crowdingWormsSlider);
				}
				controller.set('crowdingWormsSlider', crowdingWormsSlider);
			self.set('crowdingWormsSlider', crowdingWormsSlider);*/
		},
	});
