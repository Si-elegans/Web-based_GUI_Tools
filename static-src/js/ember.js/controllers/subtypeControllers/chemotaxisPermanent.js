App.ChemotaxisPermanentController = Ember.ObjectController.extend({
	needs: ["experiment",'permanent','chemotaxisQuadrants1','chemotaxisQuadrants2','chemotaxisQuadrants4','osmoticRing','staticPointSource'],
	experimentDuration: function(){
		return this.get('controllers.experiment.experimentDuration');
    },
	isOsmotic: function(){
        if(this.get('model.chemicalCategory')=="OR"){
			return true;
		}
		else{
			return false;
		}
    }.property('model.chemicalCategory'),
	isQuadrants1: function(){
        if(this.get('model.chemicalCategory')=="CQ1"){
			return true;
		}
		else{
			return false;
		}
    }.property('model.chemicalCategory'),
	isQuadrants2: function(){
        if(this.get('model.chemicalCategory')=="CQ2"){
			return true;
		}
		else{
			return false;
		}
    }.property('model.chemicalCategory'),
	isQuadrants4: function(){
        if(this.get('model.chemicalCategory')=="CQ4"){
			return true;
		}
		else{
			return false;
		}
    }.property('model.chemicalCategory'),
	isStatic: function(){
        if(this.get('model.chemicalCategory')=="SPS"){
			return true;
		}
		else{
			return false;
		}
    }.property('model.chemicalCategory'),
	
	typeName: function(){
        if(this.get('model.chemicalCategory')=="OR"){
			return "Osmotic Ring";
		}
		else if(this.get('model.chemicalCategory')=="CQ1"){
			return "Chemical Quadrants 1";
		}
		else if(this.get('model.chemicalCategory')=="CQ2"){
			return "Chemical Quadrants 2";
		}
		else if(this.get('model.chemicalCategory')=="CQ4"){
			return "Chemical Quadrants 4";
		}
		else if(this.get('model.chemicalCategory')=="SPS"){
			return "Static Point Source";
		}
		else{
			return "error";
		}
    }.property('model.chemicalCategory'),
	
	updateType: function(){
        if(this.get('model.chemicalCategory')=="OR"){
			var mycontroller = App.__container__.lookup("controller:experiment");
			var proxySend = jQuery.proxy(mycontroller.send, mycontroller);
			proxySend('makePlateRing');
		}
		else if(this.get('model.chemicalCategory')=="CQ1"){
			var mycontroller = App.__container__.lookup("controller:experiment");
			var proxySend = jQuery.proxy(mycontroller.send, mycontroller);
			proxySend('makePlateQuad1');
		}
		else if(this.get('model.chemicalCategory')=="CQ2"){
			var mycontroller = App.__container__.lookup("controller:experiment");
			var proxySend = jQuery.proxy(mycontroller.send, mycontroller);
			proxySend('makePlateQuad2');
		}
		else if(this.get('model.chemicalCategory')=="CQ4"){
			var mycontroller = App.__container__.lookup("controller:experiment");
			var proxySend = jQuery.proxy(mycontroller.send, mycontroller);
			proxySend('makePlateQuad4');
		}
		else if(this.get('model.chemicalCategory')=="SPS"){
			var mycontroller = App.__container__.lookup("controller:experiment");
				var proxySend = jQuery.proxy(mycontroller.send, mycontroller);
				proxySend('makePlateQuad1');
		}
    }.observes('model.chemicalCategory'),
	
	setType: function(value){
        if(value=="OR"){
			var mycontroller = App.__container__.lookup("controller:experiment");
			var proxySend = jQuery.proxy(mycontroller.send, mycontroller);
			proxySend('makePlateRing');
		}
		else if(value=="CQ1"){
			var mycontroller = App.__container__.lookup("controller:experiment");
			var proxySend = jQuery.proxy(mycontroller.send, mycontroller);
			proxySend('makePlateQuad1');
		}
		else if(value=="CQ2"){
			var mycontroller = App.__container__.lookup("controller:experiment");
			var proxySend = jQuery.proxy(mycontroller.send, mycontroller);
			proxySend('makePlateQuad2');
		}
		else if(value=="CQ4"){
			var mycontroller = App.__container__.lookup("controller:experiment");
			var proxySend = jQuery.proxy(mycontroller.send, mycontroller);
			proxySend('makePlateQuad4');
		}
		else if(value=="SPS"){
			var mycontroller = App.__container__.lookup("controller:experiment");
				var proxySend = jQuery.proxy(mycontroller.send, mycontroller);
				proxySend('makePlateQuad1');
		}
    }

});
