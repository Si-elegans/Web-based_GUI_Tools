App.MechanosensationPermanentView = Ember.View.extend({
		//classNames:["col-sm-4", "wrap", "color", "scrolly"],
		didInsertElement : function () {
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
