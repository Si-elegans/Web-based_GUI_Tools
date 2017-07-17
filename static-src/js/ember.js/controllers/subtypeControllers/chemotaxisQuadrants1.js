App.ChemotaxisQuadrants1Controller = Ember.ObjectController.extend({
	needs: ['chemotaxisPermanent','permanent'],
	updateConcentration: function(){
		var slider = this.get('model.quad1ConcentrationSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.quadrantChemicalConcentration')));
		}
	}.observes('model.quadrantChemicalConcentration'),
});
