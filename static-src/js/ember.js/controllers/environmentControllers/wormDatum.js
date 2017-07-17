App.WormDatumController = Ember.ObjectController.extend({
	needs:['wormStatus','environment'],
	typeName: function(){
        if(this.get('model.gender')=="FH"){
			return "Hermaphrodite";
		}
		else if(this.get('model.gender')=="M"){
			return "Male";
		}
		else{
			return "error";
		}
    }.property('model.gender'),
	updateAge : function () {
		var slider = this.get('model.wormAgeSlider');
		if (slider) {
			if (slider.getValue() != this.get('model.age')) {
				slider.setValue(parseFloat(this.get('model.age')));
			}
		}
	}
	.observes('model.age'),
	updateStageOfLifeCycle : function () {
		var slider = this.get('model.wormStageOfLifeCycleSlider');
		if (slider) {
			if (slider.getValue() != this.get('model.stageOfLifeCycle')) {
				slider.setValue(parseFloat(this.get('model.stageOfLifeCycle')));
			}
		}
	}
	.observes('model.stageOfLifeCycle'),
	updateTimeOffFood : function () {
		var slider = this.get('model.wormTimeOffFoodSlider');
		if (slider) {
			if (slider.getValue() != this.get('model.timeOffFood')) {
				slider.setValue(parseFloat(this.get('model.timeOffFood')));
			}
		}
	}
	.observes('model.timeOffFood'),
	});
