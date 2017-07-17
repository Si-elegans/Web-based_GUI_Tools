App.PlateTapController = Ember.ObjectController.extend({
	needs: ['phototaxisExact','exact'],
	updateForce: function(){
		var slider = this.get('model.plateForceSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.appliedForce')));
		}
	}.observes('model.appliedForce'),
});
