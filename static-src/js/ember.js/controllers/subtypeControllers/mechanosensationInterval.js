App.MechanosensationIntervalController = Ember.ObjectController.extend({
	needs: ["experiment",'interval'],
    templateName: function(){
	
        if(this.get('model.experimentCategory')=="MS"){
			return 'mechanosensationExact';
		}
		else{
			return 'subtypeTemplates/exactChemo';
		}
    }.property('ExperimentCategory'),
	experimentDuration: function(){
		return this.get('controllers.experiment.experimentDuration');
    },
});
