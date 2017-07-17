App.CrowdingController = Ember.ObjectController.extend({
	updateWorms : function () {
		var slider = this.get('model.crowdingWormsSlider');
		if (slider) {
			if (slider.getValue() != this.get('model.wormsInPlate')) {
				slider.setValue(parseFloat(this.get('model.wormsInPlate')));
			}
		}
	}
	.observes('model.wormsInPlate'),
});
