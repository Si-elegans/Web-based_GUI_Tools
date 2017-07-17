App.DynamicDropTestController = Ember.ObjectController.extend({
	needs: ['mechanosensationExact','exact'],
	updateConcentration: function(){
		var slider = this.get('model.ddtConcentrationSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.chemicalConcentration')));
		}
	}.observes('model.chemicalConcentration'),
	
	updateDropQuantity: function(){
		var slider = this.get('model.ddtDropSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.dropQuantity')));
		}
	}.observes('model.dropQuantity'),
	
	updateXPosition: function(){
		var slider = this.get('model.ddtXaxisSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.xCoordFromPlateCentre')));
		}
	}.observes('model.xCoordFromPlateCentre'),
	
	updateYPosition: function(){
		var slider = this.get('model.ddtYaxisSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.yCoordFromPlateCentre')));
		}
	}.observes('model.yCoordFromPlateCentre'),
});
