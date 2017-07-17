App.LinearThermalGradientController = Ember.ObjectController.extend({
	needs: ['termotaxisPermanent','permanent'],
	
	updateLeft: function(){
		var slider = this.get('model.gradientLeftSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.temperatureLeftHorizontal')));
		}
	}.observes('model.temperatureLeftHorizontal'),
	
	updateRight: function(){
		var slider = this.get('model.gradientRightSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.temperatureRightHorizonal')));
		}
	}.observes('model.temperatureRightHorizonal'),
});
