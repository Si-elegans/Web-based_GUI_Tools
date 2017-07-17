App.EnvironmentController = Ember.ObjectController.extend({
    needs: ["experiment","definition"],
	
	updateTemp : function () {
		var timeline = this.get('timeline'); //reset seconds, before setting milliseconds
		if (timeline) {
			timeline.options.end = new Number(this.get('model.envTemp'));
			timeline.range.end = this.get('model.envTemp');
			timeline.redraw();
		}
	}
	.observes('model.envTemp'),
		
    actions:{
        setEditor: function(params){
        },
		
		gotoExperiment: function(){
			var self = this;
			this.transitionToRoute('experiment').then(function(){
				self.transitionToRoute('definition');
			});
			this.set('controllers.definition.isRerender',true);
		},
		
		addObstacle: function(){
			var self = this;
			var experimentController = this.get('controllers.experiment');
			var store = this.get('store');
			var e = document.getElementById("createObstacleType");
			var obstacleType = e.options[e.selectedIndex].text;
			if(obstacleType=="Cube"){
				var aux = store.createRecord("cube", {
					side1Length: 1,
					side2Length: 1,
					depth: 1,
				});
				aux.save().then(function(item){
					var aux2 = store.createRecord("obstacleLocation", {
						xCoordFromPlateCentre: 0,
						yCoorDFromPlateCentre: 0,
						angleRelativeXaxis: 0,
						Stiffness: 0,
						shape: "CU",
						Cylinder: null,
						Cube: item,
						Hexagon: null,
						Hair: null,
					});
					aux2.save().then(function(item2){
						self.get('model._data.obstacle').pushObject(item2);
						var proxySend = jQuery.proxy(experimentController.send, experimentController);
						proxySend('savingModelDidUpdate', self.get('model'));
						proxySend('addCube',item2.get('id'));
						var model = self.get('model.obstacle');
						model.addObject(item2);
					});
				});
			}
			else if(obstacleType=="Cylinder"){
				var aux = store.createRecord("cylinder", {
					length: 1,
					radius: 1,
				});
				aux.save().then(function(item){
					var aux2 = store.createRecord("obstacleLocation", {
						xCoordFromPlateCentre: 0,
						yCoorDFromPlateCentre: 0,
						angleRelativeXaxis: 0,
						Stiffness: 0,
						shape: "CY",
						Cylinder: item,
						Cube: null,
						Hexagon: null,
						Hair: null,
					});
					aux2.save().then(function(item2){
						self.get('model._data.obstacle').pushObject(item2);
						var proxySend = jQuery.proxy(experimentController.send, experimentController);
						proxySend('savingModelDidUpdate', self.get('model'));
						proxySend('addCylinder',item2.get('id'));
						var model = self.get('model.obstacle');
						model.addObject(item2);
					});
				});
			}
			else if(obstacleType=="Hexagonal"){
				var aux = store.createRecord("hexagon", {
					sideLength: 1,
					depth: 1,
				});
				aux.save().then(function(item){
					var aux2 = store.createRecord("obstacleLocation", {
						xCoordFromPlateCentre: 0,
						yCoorDFromPlateCentre: 0,
						angleRelativeXaxis: 0,
						Stiffness: 0,
						shape: "HE",
						Cylinder: null,
						Cube: null,
						Hexagon: item,
						Hair: null,
					});
					aux2.save().then(function(item2){
						self.get('model._data.obstacle').pushObject(item2);
						var proxySend = jQuery.proxy(experimentController.send, experimentController);
						proxySend('savingModelDidUpdate', self.get('model'));
						proxySend('addPrism',item2.get('id'));
						var model = self.get('model.obstacle');
						model.addObject(item2);
					});
				});
			}
		}
    }
});
