App.CylinderController = Ember.ObjectController.extend({
	needs: ['environment', 'experiment'],
	lengthId: function(){
		return "cylinderLengthSlider" + this.get('model.id');
	}.property('model.id'),
	radiusId: function(){
		return "cylinderRadiusSlider" + this.get('model.id');
	}.property('model.id'),
	updateLength : function () {
		var slider = this.get('model.cylinderLengthSlider' + this.get('model.id'));
		if (slider) {
			if (slider.getValue() != this.get('model.length')) {
				slider.setValue(parseFloat(this.get('model.length')));
			}
		}
		var signals = this.get('controllers.experiment.signals');
		if(signals){
			signals.cylinderLengthChanged.dispatch(this.get('model.length'),this.get('parentController.model.id'));
		}
	}
	.observes('model.length'),
	updateRadius : function () {
		var slider = this.get('model.cylinderRadiusSlider' + this.get('model.id'));
		if (slider) {
			if (slider.getValue() != this.get('model.radius')) {
				slider.setValue(parseFloat(this.get('model.radius')));
			}
		}
		var signals = this.get('controllers.experiment.signals');
		if(signals){
			signals.cylinderRadiusChanged.dispatch(this.get('model.radius'),this.get('parentController.model.id'));
		}
	}
	.observes('model.radius'),
});
