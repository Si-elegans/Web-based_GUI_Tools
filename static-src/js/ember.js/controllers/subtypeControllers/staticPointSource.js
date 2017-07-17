App.StaticPointSourceController = Ember.ObjectController.extend({
	needs: ['chemotaxisPermanent','permanent'],
	updateConcentration: function(){
		var slider = this.get('model.spsConcentrationSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.chemicalConcentration')));
		}
	}.observes('model.chemicalConcentration'),
	
	updateDropQuantity: function(){
		var slider = this.get('model.spsDropSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.dropQuantity')));
		}
	}.observes('model.dropQuantity'),
	
	updateXPosition: function(){
		var slider = this.get('model.spsXaxisSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.xCoordFromPlateCentre')));
		}
	}.observes('model.xCoordFromPlateCentre'),
	
	updateYPosition: function(){
		var slider = this.get('model.spsYaxisSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.yCoordFromPlateCentre')));
		}
	}.observes('model.yCoordFromPlateCentre'),
});