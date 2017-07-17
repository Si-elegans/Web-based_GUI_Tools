App.TermotaxisIntervalView = Ember.View.extend({
		//classNames:["col-sm-4", "wrap", "color", "scrolly"],
		didInsertElement : function () {
			var self = this;
			var store = this.get('controller.store');
			$('#termoPoint').click(function(){
				if(self.get('controller.model.pointSourceHeatAvoidance.content')){
					self.set('controller.model.termotaxisType','PS');
				}
				else{
					var aux2 = store.createRecord("pointSourceHeatAvoidance",{
						temperature: 0,
						heatPointDistance: 0,
					});
					aux2.save().then(function(item){
						var avoidanceItems = store.all('pointSourceHeatAvoidance');
						if (self.get('controllers.pointSourceHeatAvoidance.avoidanceTemperatureSlider')) {
							for (var i = 0; i < avoidanceItems.content.length; i++) {
								avoidanceItems.content[i].set('avoidanceTemperatureSlider', self.get('controllers.pointSourceHeatAvoidance.avoidanceTemperatureSlider'));
							}
						}
						if (self.get('controllers.pointSourceHeatAvoidance.avoidanceDistanceSlider')) {
							for (var i = 0; i < avoidanceItems.content.length; i++) {
								avoidanceItems.content[i].set('avoidanceDistanceSlider', self.get('controllers.pointSourceHeatAvoidance.avoidanceDistanceSlider'));
							}
						}
						if (self.get('controllers.pointSourceHeatAvoidance.avoidanceAngleSlider')) {
							for (var i = 0; i < avoidanceItems.content.length; i++) {
								avoidanceItems.content[i].set('avoidanceAngleSlider', self.get('controllers.pointSourceHeatAvoidance.avoidanceAngleSlider'));
							}
						}
						self.set('controller.model.pointSourceHeatAvoidance',item);
						self.set('controller.model.termotaxisType','PS');
					});
				}
			});
			$('#termoTemperature').click(function(){
				if(self.get('controller.model.temperatureChangeInTime.content')){
					self.set('controller.model.termotaxisType','TC');
				}
				else{
					var aux2 = store.createRecord("temperatureChangeInTime",{
						initialTemperature: 0,
						finalTemperature: 0,
					});
					aux2.save().then(function(item){
						var temperatureItems = store.all('temperatureChangeInTime');
						if (self.get('controllers.temperatureChangeInTime.temperatureInitialSlider')) {
							for (var i = 0; i < temperatureItems.content.length; i++) {
								temperatureItems.content[i].set('temperatureInitialSlider', self.get('controllers.temperatureChangeInTime.temperatureInitialSlider'));
							}
						}
						if (self.get('controllers.temperatureChangeInTime.temperatureFinalSlider')) {
							for (var i = 0; i < temperatureItems.content.length; i++) {
								temperatureItems.content[i].set('temperatureFinalSlider', self.get('controllers.temperatureChangeInTime.temperatureFinalSlider'));
							}
						}
						self.set('controller.model.temperatureChangeInTime',item);
						self.set('controller.model.termotaxisType','TC');
					});
				}
			});
		},
	});
