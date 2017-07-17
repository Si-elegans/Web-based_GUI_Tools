App.PlateConfigurationController = Ember.ObjectController.extend({
    lidName: function(){
        if(this.get('model.lid')==true){
			return "true";
		}
		else if(this.get('model.lid')==false){
			return "false";
		}
		else{
			return "error";
		}
    }.property('model.lid'),
	shapeName: function(){
        if(this.get('model.shape')=="CY"){
			return "Cylinder";
		}
		else if(this.get('model.shape')=="CU"){
			return "Cube";
		}
		else if(this.get('model.shape')=="HE"){
			return "Hexagon";
		}
		else{
			return "error";
		}
    }.property('model.shape'),
	materialName: function(){
        if(this.get('model.bottomMaterial')=="W"){
			return "Water";
		}
		else if(this.get('model.bottomMaterial')=="A"){
			return "Agar";
		}
		else if(this.get('model.bottomMaterial')=="G"){
			return "Gelatin";
		}
		else{
			return "error";
		}
    }.property('model.bottomMaterial'),
	updateDryness : function () {
		var slider = this.get('model.plateDrynessAgeSlider');
		if (slider) {
			if (slider.getValue() != this.get('model.dryness')) {
				slider.setValue(parseFloat(this.get('model.dryness')));
			}
		}
	}
	.observes('model.dryness'),
	
	updateShape: function(){
        if(this.get('model.shape')=="CY"){
			var mycontroller = App.__container__.lookup("controller:experiment");
			var proxySend = jQuery.proxy(mycontroller.send, mycontroller);
			proxySend('makePlateCylinder');
		}
		else if(this.get('model.shape')=="CU"){				
			var mycontroller = App.__container__.lookup("controller:experiment");
			var proxySend = jQuery.proxy(mycontroller.send, mycontroller);
			proxySend('makePlateCube');
		}
		else if(this.get('model.shape')=="HE"){
			var mycontroller = App.__container__.lookup("controller:experiment");
			var proxySend = jQuery.proxy(mycontroller.send, mycontroller);
			proxySend('makePlateHexagon');
		}
    }.observes('model.shape'),
	
	setShape: function(value){
        if(value=="CY"){
			var mycontroller = App.__container__.lookup("controller:experiment");
			var proxySend = jQuery.proxy(mycontroller.send, mycontroller);
			proxySend('makePlateCylinder');
		}
		else if(value=="CU"){				
			var mycontroller = App.__container__.lookup("controller:experiment");
			var proxySend = jQuery.proxy(mycontroller.send, mycontroller);
			proxySend('makePlateCube');
		}
		else if(value=="HE"){
			var mycontroller = App.__container__.lookup("controller:experiment");
			var proxySend = jQuery.proxy(mycontroller.send, mycontroller);
			proxySend('makePlateHexagon');
		}
    },
});
