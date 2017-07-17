App.TemperatureChangeInTimeController = Ember.ObjectController.extend({
	needs: ['termotaxisInterval','interval'],
	
	updateInitial: function(){
		var slider = this.get('model.temperatureInitialSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.initialTemperature')));
		}
	}.observes('model.initialTemperature'),
	
	updateFinal: function(){
		var slider = this.get('model.temperatureFinalSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.finalTemperature')));
		}
	}.observes('model.finalTemperature'),
	
});
