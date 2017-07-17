App.TermotaxisIntervalController = Ember.ObjectController.extend({
	needs: ["experiment",'interval'],
    experimentDuration: function(){
		return this.get('controllers.experiment.experimentDuration');
    },

	isPoint: function(){
        if(this.get('model.termotaxisType')=="PS"){
			return true;
		}
		else{
			return false;
		}
    }.property('model.termotaxisType'),
	
	isTemperature: function(){
        if(this.get('model.termotaxisType')=="TC"){
			return true;
		}
		else{
			return false;
		}
    }.property('model.termotaxisType'),
	
	typeName: function(){
        if(this.get('model.termotaxisType')=="PS"){
			return "Point Source Heat Avoidance";
		}
		else if(this.get('model.termotaxisType')=="TC"){
			return "Temperature Change in Time";
		}
		else{
			return "error";
		}
    }.property('model.termotaxisType'),
});
