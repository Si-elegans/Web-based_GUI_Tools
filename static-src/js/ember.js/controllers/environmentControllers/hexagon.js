App.HexagonController = Ember.ObjectController.extend({
	needs: ['environment','experiment'],
	depthId: function(){
		return "hexagonDepthSlider" + this.get('model.id');
	}.property('model.id'),
	sideId: function(){
		return "hexagonSideSlider" + this.get('model.id');
	}.property('model.id'),
	updateSide : function () {
		var slider = this.get('model.hexagonSideSlider' + this.get('model.id'));
		if (slider) {
			if (slider.getValue() != this.get('model.sideLength')) {
				slider.setValue(parseFloat(this.get('model.sideLength')));
			}
		}
		var signals = this.get('controllers.experiment.signals');
		if(signals){
			signals.prismSideChanged.dispatch(this.get('model.sideLength'),this.get('parentController.model.id'));
		}
	}
	.observes('model.sideLength'),
	updateDepth : function () {
		var slider = this.get('model.hexagonDepthSlider' + this.get('model.id'));
		if (slider) {
			if (slider.getValue() != this.get('model.depth')) {
				slider.setValue(parseFloat(this.get('model.depth')));
			}
		}
		var signals = this.get('controllers.experiment.signals');
		if(signals){
			signals.prismDepthChanged.dispatch(this.get('model.depth'),this.get('parentController.model.id'));
		}
	}
	.observes('model.depth'),
});
