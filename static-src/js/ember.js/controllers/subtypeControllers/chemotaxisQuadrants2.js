App.ChemotaxisQuadrants2Controller = Ember.ObjectController.extend({
	needs: ['chemotaxisPermanent','permanent'],
	updateConcentration1: function(){
		var slider = this.get('model.quad2ConcentrationSlider1');
		if(slider){
			slider.setValue(parseFloat(this.get('model.quadrant_1_ChemicalConcentration')));
		}
	}.observes('model.quadrant_1_ChemicalConcentration'),
	
	updateConcentration2: function(){
		var slider = this.get('model.quad2ConcentrationSlider2');
		if(slider){
			slider.setValue(parseFloat(this.get('model.quadrant_2_ChemicalConcentration')));
		}
	}.observes('model.quadrant_2_ChemicalConcentration'),
	
	updateBarrierConcentration: function(){
		var slider = this.get('model.quad2BarrierConcentrationSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.quadrantBarrierChemicalConcentration')));
		}
	}.observes('model.quadrantBarrierChemicalConcentration'),
});
