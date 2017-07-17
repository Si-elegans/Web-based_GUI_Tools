App.WormDatumView = Ember.View.extend({
		classNames : [],
		didInsertElement : function () {
			var controller = this.get('controller');
			var self = this;
			var data2 = this.get('controller.model.content');
			
			//not implemented yet
			/*var wormAgeSlider = new Slider('#wormAgeSlider', {
					range : false,
					max : new Number(255),
					step : 0.1,
					value : data2.get('age'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('age', value);
						}
						return value + ' h';
					},
					id : 'worm-age-slider',
				});
			var items = controller.store.all('wormDatum')
				for (var i = 0; i < items.content.length; i++) {
					items.content[i].set('wormAgeSlider', wormAgeSlider);
				}
				controller.set('wormAgeSlider', wormAgeSlider);
			self.set('wormAgeSlider', wormAgeSlider);

			var wormStageOfLifeCycleSlider = new Slider('#wormStageOfLifeCycleSlider', {
					range : false,
					max : new Number(255),
					step : 0.1,
					value : data2.get('stageOfLifeCycle'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('stageOfLifeCycle', value);
						}
						return 'Current value: ' + value;
					},
					id : 'worm-StageOfLifeCycle-slider',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('wormStageOfLifeCycleSlider', wormStageOfLifeCycleSlider);
			}
			controller.set('wormStageOfLifeCycleSlider', wormStageOfLifeCycleSlider);
			self.set('wormStageOfLifeCycleSlider', wormStageOfLifeCycleSlider);

			var wormTimeOffFoodSlider = new Slider('#wormTimeOffFoodSlider', {
					range : false,
					max : new Number(255),
					step : 0.1,
					value : data2.get('timeOffFood'),
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('timeOffFood', value);
						}
						return value + ' min';
					},
					id : 'worm-xdistance-slider',
				});
			for (var i = 0; i < items.content.length; i++) {
				items.content[i].set('wormTimeOffFoodSlider', wormTimeOffFoodSlider);
			}
			controller.set('wormTimeOffFoodSlider', wormTimeOffFoodSlider);
			self.set('wormTimeOffFoodSlider', wormTimeOffFoodSlider);

			$('#genderHermaphrodite').click(function () {
				self.set('controller.model.gender', 'FH');
			});
			$('#genderMale').click(function () {
				self.set('controller.model.gender', 'M');
			});*/
		},
	});
