App.WormStatusController = Ember.ObjectController.extend({
		needs: ['experiment'],
		updateXDistance : function () {
			var slider = this.get('model.wormDistanceXSlider');
			if (slider) {
				if (slider.getValue() != this.get('model.xCoordFromPlateCentre')) {
					slider.setValue(parseFloat(this.get('model.xCoordFromPlateCentre')));
				}
			}
			var signals = this.get('controllers.experiment.signals');
			if(signals){
				signals.wormXChanged.dispatch(this.get('model.xCoordFromPlateCentre'));
			}
		}
		.observes('model.xCoordFromPlateCentre'),
		updateYDistance : function () {
			var slider = this.get('model.wormDistanceYSlider');
			if (slider) {
				if (slider.getValue() != this.get('model.yCoorDFromPlateCentre')) {
					slider.setValue(parseFloat(this.get('model.yCoorDFromPlateCentre')));
				}
			}
			var signals = this.get('controllers.experiment.signals');
			if(signals){
				signals.wormYChanged.dispatch(this.get('model.yCoorDFromPlateCentre'));
			}
		}
		.observes('model.yCoorDFromPlateCentre'),
		updateAngle : function () {
			var slider = this.get('model.wormAngleSlider');
			if (slider) {
				if (slider.getValue() != this.get('model.angleRelativeXaxis')) {
					slider.setValue(parseFloat(this.get('model.angleRelativeXaxis')));
				}
			}
			var signals = this.get('controllers.experiment.signals');
			if(signals){
				signals.wormAngleChanged.dispatch(this.get('model.angleRelativeXaxis'));	
			}
		}
		.observes('model.angleRelativeXaxis'),
		
		actions: {
			actionUpdateXDistance: function(){
				this.updateXDistance();
			},
			actionUpdateYDistance: function(){
				this.updateYDistance();
			},
			actionUpdateAngle: function(){
				this.updateAngle();
			},
		},
	});
