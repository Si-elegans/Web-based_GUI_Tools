App.ChemotaxisExactController = Ember.ObjectController.extend({
	needs: ["experiment",'exact'],
	experimentDuration: function(){
		return this.get('controllers.experiment.experimentDuration');
    },
	
	typeName: function(){
        if(this.get('model.chemotaxisType')=="DDT"){
			return "Dynamic Drop Test";
		}
		else{
			return "error";
		}
    }.property('model.interactionType'),
});
