App.Definition2View = Ember.View.extend({
		classNames : ["wrap", 'row'],
		rerenderDefinition2: function(){
			if(this.get('controller.isRerender')){
				this.rerender();
				this.set('controller.isRerender',false);
			}
		}.observes('controller.isRerender'),
		
		didInsertElement : function () {
			var self = this;
			var duration = this.get('controller.model.experimentDuration');
			var experimentDurationSlider = new Slider('#experimentDurationSlider', {
					range : false,
					max : new Number(100000),
					step : 1,
					value : duration,
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('experimentDuration', value);
						}
						var secs = Math.round(value/100);
						return secs/10 + ' s';
					},
					id : 'experiment-duration-slider',
				});
		},
	});
