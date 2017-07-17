App.ObstacleLocationController = Ember.ObjectController.extend({
	needs: ['environment','experiment'],
	obstacles: function(){
		return this.get('controllers.environment.model.obstacle')
	}.property('controllers.environment.model.obstacle'),
	shapeName: function(){
		if(this.get('model.shape')=='CY'){
			return 'Cylinder';
		}
		else if(this.get('model.shape')=='CU'){
			return 'Cube';
		}
		else if(this.get('model.shape')=='HE'){
			return 'Hexagon';
		}
		else{
			return 'error';
		}
	}.property('model.shape'),
	distanceXId: function(){
		return "obstacleDistanceXSlider" + this.get('model.id');
	}.property('model.id'),
	distanceYId: function(){
		return "obstacleDistanceYSlider" + this.get('model.id');
	}.property('model.id'),
	stiffnessId: function(){
		return "obstacleStiffnessSlider" + this.get('model.id');
	}.property('model.id'),
	updateXDistance : function () {
		var slider = this.get('model.obstacleDistanceXSlider' + this.get('model.id'));
		if (slider) {
			if (slider.getValue() != this.get('model.xCoordFromPlateCentre')) {
				slider.setValue(parseFloat(this.get('model.xCoordFromPlateCentre')));
			}
		}
		var signals = this.get('controllers.experiment.signals');
		if(signals){
			signals.obstacleXChanged.dispatch(this.get('model.xCoordFromPlateCentre'),this.get('model.id'));
		}
	}
	.observes('model.xCoordFromPlateCentre'),
	updateYDistance : function () {
		var slider = this.get('model.obstacleDistanceYSlider' + this.get('model.id'));
		if (slider) {
			if (slider.getValue() != this.get('model.yCoorDFromPlateCentre')) {
				slider.setValue(parseFloat(this.get('model.yCoorDFromPlateCentre')));
			}
		}
		var signals = this.get('controllers.experiment.signals');
		if(signals){
			signals.obstacleYChanged.dispatch(this.get('model.yCoorDFromPlateCentre'),this.get('model.id'));
		}
	}
	.observes('model.yCoorDFromPlateCentre'),
	updateStiffness : function () {
		var slider = this.get('model.obstacleStiffnessSlider' + this.get('model.id'));
		if (slider) {
			if (slider.getValue() != this.get('model.Stiffness')) {
				slider.setValue(parseFloat(this.get('model.Stiffness')));
			}
		}
	}
	.observes('model.Stiffness'),
	isCylinder: function(){
		if(this.get('model.shape')=='CY'){
			return true;
		}
		else{
			return false;
		}
	}.property('model.shape'),
	isCube: function(){
		if(this.get('model.shape')=='CU'){
			return true;
		}
		else{
			return false;
		}
	}.property('model.shape'),
	isHexagon: function(){
		if(this.get('model.shape')=='HE'){
			return true;
		}
		else{
			return false;
		}
	}.property('model.shape'),
	actions: {
		removeObstacle: function(id){
			var experimentController = this.get('controllers.experiment');
			var proxySend = jQuery.proxy(experimentController.send, experimentController);
			proxySend('removeObstacle', id);
		}
	}
});
