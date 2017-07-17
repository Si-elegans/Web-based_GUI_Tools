App.MechanosensationIntervalView = Ember.View.extend({
		//classNames:["col-sm-4", "wrap", "color", "scrolly"],
		didInsertElement : function () {
			var self = this;
			var controller = this.get('controller');
			var eventController = this.get('controller.controllers.interval');
			var eventModel = this.get('controller.controllers.interval.model');
			this.get('controller.controllers.experiment.model.experimentDefinition').then(function (data) {
				var intervalSlider = new Slider('#intervalSlider', {
					range : true,
					max : new Number(data.get('experimentDuration')),
					step : 0.1,
					value : [eventModel.get('eventStartTime'), eventModel.get('eventStopTime')],
					formatter : function (value) {
						if(value.length > 1){
							eventModel.set('eventStartTime', value[0]);
							eventModel.set('eventStopTime', value[1]);
						}
						return 'Current value: ' + value;
					},
					id : 'mechano-interval-slider',
				});
				eventController.set('intervalSlider',intervalSlider);
			});
			var forceSlider = new Slider('#forceSlider', {
					formatter : function (value) {
						return 'Current value: ' + value;
					}
				});
			var locationLengthSlider = new Slider('#locationLengthSlider', {
					formatter : function (value) {
						return 'Current value: ' + value;
					}
				});
			var locationAngleSlider = new Slider('#locationAngleSlider', {
					formatter : function (value) {
						return 'Current value: ' + value;
					}
				});
		},
	});
