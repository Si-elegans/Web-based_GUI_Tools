App.PointSourceHeatAvoidanceController = Ember.ObjectController.extend({
	needs: ['termotaxisInterval','interval'],
	
	updateTemperature: function(){
		var slider = this.get('model.avoidanceTemperatureSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.temperature')));
		}
	}.observes('model.temperature'),
	
	updateDistance: function(){
		var slider = this.get('model.avoidanceDistanceSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.heatPointDistance')));
		}
	}.observes('model.heatPointDistance'),
	
});
