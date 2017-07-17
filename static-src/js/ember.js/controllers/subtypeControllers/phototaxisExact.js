App.PhototaxisExactController = Ember.ObjectController.extend({
	needs: ["experiment",'exact'],
	experimentDuration: function(){
		return this.get('controllers.experiment.experimentDuration');
    },
	typeName: function(){
        if(this.get('model.phototaxisType')=="PSL"){
			return 'Point Source Light';
		}
		else{
			return 'error';
		}
    }.property('model.phototaxisType'),
	isPoint: function(){
        if(this.get('model.phototaxisType')=="PSL"){
			return true;
		}
		else{
			return false;
		}
    }.property('model.phototaxisType'),
});
