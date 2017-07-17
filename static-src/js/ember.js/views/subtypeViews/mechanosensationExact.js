App.MechanosensationExactView = Ember.View.extend({
		//classNames:["col-sm-4", "wrap", "color", "scrolly"],
		didInsertElement : function () {
			var self = this;
			var store = this.get('controller.store');
			$('#mechanoTouch').click(function(){
				if(self.get('controller.model.directTouch.content')){
					self.set('controller.model.interactionType','DWT');
				}
				else{
					var aux = store.createRecord("directTouch", {
						appliedForce : 0,
						directTouchInstrument: "VFH",
						touchDistance: 0,
						touchAngle: 0,
					});
					self.set('controller.model.directTouch',aux);
					self.set('controller.model.interactionType','DWT');
				}
			});
			$('#mechanoPlate').click(function(){
				if(self.get('controller.model.plateTap.content')){
					self.set('controller.model.interactionType','PT');
				}
				else{
					var aux = store.createRecord("plateTap", {
						appliedForce : 0,
					});
					self.set('controller.model.plateTap',aux);
					self.set('controller.model.interactionType','PT');
				}
			});
		},
		templateName: 'mechanosensationExact',
		
	});
