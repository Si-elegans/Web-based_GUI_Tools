App.CubeController = Ember.ObjectController.extend({
	needs: ['environment', 'experiment'],
	side1Id: function(){
		return "cubeSide1Slider" + this.get('model.id');
	}.property('model.id'),
	side2Id: function(){
		return "cubeSide2Slider" + this.get('model.id');
	}.property('model.id'),
	depthId: function(){
		return "cubeDepthSlider" + this.get('model.id');
	}.property('model.id'),
	updateSide1 : function () {
		var slider = this.get('model.cubeSide1Slider' + this.get('model.id'));
		if (slider) {
			if (slider.getValue() != this.get('model.side1Length')) {
				slider.setValue(parseFloat(this.get('model.side1Length')));
			}
		}
		var signals = this.get('controllers.experiment.signals');
		if(signals){
			signals.cubeSide1Changed.dispatch(this.get('model.side1Length'),this.get('parentController.model.id'));
		}
	}
	.observes('model.side1Length'),
	updateSide2 : function () {
		var slider = this.get('model.cubeSide2Slider' + this.get('model.id'));
		if (slider) {
			if (slider.getValue() != this.get('model.side2Length')) {
				slider.setValue(parseFloat(this.get('model.side2Length')));
			}
		}
		var signals = this.get('controllers.experiment.signals');
		if(signals){
			signals.cubeSide2Changed.dispatch(this.get('model.side2Length'),this.get('parentController.model.id'));
		}
	}
	.observes('model.side2Length'),
	updateDepth : function () {
		var slider = this.get('model.cubeDepthSlider' + this.get('model.id'));
		if (slider) {
			if (slider.getValue() != this.get('model.depth')) {
				slider.setValue(parseFloat(this.get('model.depth')));
			}
		}
		var signals = this.get('controllers.experiment.signals');
		if(signals){
			signals.cubeDepthChanged.dispatch(this.get('model.depth'),this.get('parentController.model.id'));
		}
	}
	.observes('model.depth'),
	
});
