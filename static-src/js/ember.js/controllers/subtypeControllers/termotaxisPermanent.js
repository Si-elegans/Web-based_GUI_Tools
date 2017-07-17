App.TermotaxisPermanentController = Ember.ObjectController.extend({
	needs: ["experiment",'permanent'],
    experimentDuration: function(){
		return this.get('controllers.experiment.experimentDuration');
    },
	
	typeName: function(){
        if(this.get('model.termotaxisType')=="LT"){
			return "Linear Thermal Gradient";
		}
		else{
			return "error";
		}
    }.property('model.termotaxisType'),

});
