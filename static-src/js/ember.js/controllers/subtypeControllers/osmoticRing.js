App.OsmoticRingController = Ember.ObjectController.extend({
	needs: ['chemotaxisPermanent','permanent'],
	updateConcentration: function(){
		var slider = this.get('model.osmoticConcentrationSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.chemicalConcentration')));
		}
	}.observes('model.chemicalConcentration'),
	
	updateInternal: function(){
		var slider = this.get('model.osmoticInternalSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.internalRadius')));
		}
	}.observes('model.internalRadius'),
	
	updateExternal: function(){
		var slider = this.get('model.osmoticExternalSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.externalRadius')));
		}
	}.observes('model.externalRadius'),
	
});
