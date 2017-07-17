App.PointSourceLightController = Ember.ObjectController.extend({
	needs: ['phototaxisExact','interval'],
	
	updateWavelength: function(){
		var slider = this.get('model.pointLightWavelengthSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.waveLength')));
		}
	}.observes('model.waveLength'),
	
	updateIntensity: function(){
		var slider = this.get('model.pointLightIntensitySlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.intensity')));
		}
	}.observes('model.intensity'),
	
	updateDistance: function(){
		var slider = this.get('model.pointLightLightingDistanceSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.lightingPointDistance')));
		}
	}.observes('model.lightingPointDistance'),
	
	updateBeam: function(){
		var slider = this.get('model.pointLightBeamSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.lightBeamRadius')));
		}
	}.observes('model.lightBeamRadius'),
});
