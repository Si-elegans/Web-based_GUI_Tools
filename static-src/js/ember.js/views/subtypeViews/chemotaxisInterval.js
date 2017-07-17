App.ChemotaxisIntervalView = Ember.View.extend({
		//classNames:["col-sm-4", "wrap", "color", "scrolly"],
		didInsertElement : function () {
			var self = this;
			var controller = this.get('controller');
			var eventController = this.get('controller.controllers.event');
			var model = this.get('controller.model');
			var intervalSlider = new Slider('#intervalSlider', {
					formatter : function (value) {
						var aux = controller.get('controllers.experiment.model.experimentDefinition.interactionAtSpecificTime');
						aux.findBy('id', model.get('id'));
						model.set('eventTime', value);
						return 'Current value: ' + value;
					},
					id : 'mechano-interval-slider',

				});
			exactTimeSlider.options.step = 0.1;
			this.get('controller.controllers.experiment.model.experimentDefinition').then(function (data) {
				intervalSlider.options.max = new Number(data.get('experimentDuration'));
				intervalSlider.setValue(model.get('eventTime'));
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
