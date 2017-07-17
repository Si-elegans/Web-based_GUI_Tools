App.ElectricShockController = Ember.ObjectController.extend({
	needs: ['galvanotaxisInterval','interval'],
	
	updateDuration: function(){
		var slider = this.get('model.shockDurationSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.shockDuration')));
		}
	}.observes('model.shockDuration'),
	
	updateFrequency: function(){
		var slider = this.get('model.shockFrequencySlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.shockFrequency')));
		}
	}.observes('model.shockFrequency'),
	
	updateAmplitude: function(){
		var slider = this.get('model.shockAmplitudeSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.amplitude')));
		}
	}.observes('model.amplitude'),
});
