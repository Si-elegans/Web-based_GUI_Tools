App.DirectTouchController = Ember.ObjectController.extend({
	needs: ['mechanosensationExact','exact'],
	updateForce: function(){
		var slider = this.get('model.touchForceSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.appliedForce')));
		}
	}.observes('model.appliedForce'),
	updateLocationAngle: function(){
		var slider = this.get('model.touchLocationAngleSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.touchAngle')));
		}
	}.observes('model.touchAngle'),
	updateLocationLength: function(){
		var slider = this.get('model.touchLocationLengthSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.touchDistance')));
		}
	}.observes('model.touchDistance'),
	typeName: function(){
		if(this.get('model.directTouchInstrument')=="EB"){
			return 'Eyebrow';
		}
		else if(this.get('model.directTouchInstrument')=="VFH"){
			return 'Von Frey Hair';
		}
		else if(this.get('model.directTouchInstrument')=="PW"){
			return 'Platinium Wire';
		}
		else{
			return 'error';
		}
    }.property('model.directTouchInstrument'),
});
