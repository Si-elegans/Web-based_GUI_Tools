App.GalvanotaxisIntervalController = Ember.ObjectController.extend({
	needs: ["experiment",'interval'],
	experimentDuration: function(){
		return this.get('controllers.experiment.experimentDuration');
    },
	typeName: function(){
        if(this.get('model.galvanotaxisType')=="ES"){
			return 'Electric Shock';
		}
		else{
			return 'error';
		}
    }.property('model.galvanotaxisType'),
});
