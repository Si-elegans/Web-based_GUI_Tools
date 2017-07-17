App.MechanosensationExactController = Ember.ObjectController.extend({
	needs: ["experiment",'exact'],
	experimentDuration: function(){
		return this.get('controllers.experiment.experimentDuration');
    },
	isTouch: function(){
        if(this.get('model.interactionType')=="DWT"){
			return true;
		}
		else{
			return false;
		}
    }.property('model.interactionType'),
	isPlate: function(){
        if(this.get('model.interactionType')=="PT"){
			return true;
		}
		else{
			return false;
		}
    }.property('model.interactionType'),
	typeName: function(){
        if(this.get('model.interactionType')=="PT"){
			return "Plate Tap";
		}
		else if(this.get('model.interactionType')=="DWT"){
			return "Direct Touch";
		}
		else{
			return "error";
		}
    }.property('model.interactionType'),
});
