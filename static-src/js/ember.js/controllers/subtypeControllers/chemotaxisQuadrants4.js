App.ChemotaxisQuadrants4Controller = Ember.ObjectController.extend({
	needs: ['chemotaxisPermanent','permanent'],
	updateConcentration1: function(){
		var slider = this.get('model.quad4ConcentrationSlider1');
		if(slider){
			slider.setValue(parseFloat(this.get('model.quadrant_1_ChemicalConcentration')));
		}
	}.observes('model.quadrant_1_ChemicalConcentration'),
	
	updateConcentration2: function(){
		var slider = this.get('model.quad4ConcentrationSlider2');
		if(slider){
			slider.setValue(parseFloat(this.get('model.quadrant_2_ChemicalConcentration')));
		}
	}.observes('model.quadrant_2_ChemicalConcentration'),
	
	updateConcentration3: function(){
		var slider = this.get('model.quad4ConcentrationSlider3');
		if(slider){
			slider.setValue(parseFloat(this.get('model.quadrant_3_ChemicalConcentration')));
		}
	}.observes('model.quadrant_3_ChemicalConcentration'),
	
	updateConcentration4: function(){
		var slider = this.get('model.quad4ConcentrationSlider4');
		if(slider){
			slider.setValue(parseFloat(this.get('model.quadrant_4_ChemicalConcentration')));
		}
	}.observes('model.quadrant_4_ChemicalConcentration'),
	
	updateBarrierConcentration: function(){
		var slider = this.get('model.quad4BarrierConcentrationSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.quadrantBarrierChemicalConcentration')));
		}
	}.observes('model.quadrantBarrierChemicalConcentration'),
});
