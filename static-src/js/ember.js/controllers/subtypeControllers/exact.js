App.ExactController = Ember.ObjectController.extend({
	needs: ["experiment",'phototaxisExact'],
	isModifiable : true,
    templateName: function(){
        if(this.get('model.experimentCategory')=="MS"){
			return 'mechanosensationExact';
		}
		else if(this.get('model.experimentCategory')=="TT"){
			return 'termotaxisExact';
		}
		else if(this.get('model.experimentCategory')=="CT"){
			return 'chemotaxisExact';
		}
		else if(this.get('model.experimentCategory')=="GT"){
			return 'galvanotaxisExact';
		}
		else if(this.get('model.experimentCategory')=="PT"){
			return 'phototaxisExact';
		}
		else{
			return 'error';
		}
    }.property('model.experimentCategory'),
	experimentDuration: function(){
		return this.get('controllers.experiment.experimentDuration');
    },
	
	updateEventDescription: function(){
		var controller = App.__container__.lookup("controller:definition");
		var proxySend = jQuery.proxy(controller.send, controller);
		proxySend('updateTimelineBoxName', "exact" + this.get('model.id'), this.get('model.description'));
	}.observes('model.description'),
	
	updateEventTime: function(){
		var slider = this.get('model.exactTimeSlider');
		if(slider){
			slider.setValue(parseFloat(this.get('model.eventTime')));
			slider.options.value = parseFloat(this.get('model.eventTime'));
			var controller = App.__container__.lookup("controller:definition");
			var proxySend = jQuery.proxy(controller.send, controller);
			proxySend('updateTimelineBoxTime', "exact" + this.get('model.id'), parseFloat(this.get('model.eventTime')));
		}
	}.observes('model.eventTime'),
	isMechano: function(){
		if(this.get('model.experimentCategory')=="MS"){
			return true;
		}
		else{
			return false;
		}
	}.property('model.experimentCategory'),
	isPhoto: function(){
		if(this.get('model.experimentCategory')=="PT"){
			return true;
		}
		else{
			return false;
		}
	}.property('model.experimentCategory'),
	isGalvano: function(){
		if(this.get('model.experimentCategory')=="GT"){
			return true;
		}
		else{
			return false;
		}
	}.property('model.experimentCategory'),
	isChemo: function(){
		if(this.get('model.experimentCategory')=="CT"){
			return true;
		}
		else{
			return false;
		}
	}.property('model.experimentCategory'),
	isTermo: function(){
		if(this.get('model.experimentCategory')=="TT"){
			return true;
		}
		else{
			return false;
		}
	}.property('model.experimentCategory'),
	actions:{
		deleteEvent : function () {
			var url = window.location.href;
			var aux = url.lastIndexOf("/");
			var type = url.slice(aux - 5, aux);
			var index = url.slice(aux + 1, url.length);
			var store = this.store;
			if (type == "exact") {
				var controller = App.__container__.lookup("controller:definition");
				var proxySend = jQuery.proxy(controller.send, controller);
				proxySend('deleteBox', "exact" + index);
				store.find('interactionAtSpecificTime', index).then(function (event) {
					event.destroyRecord(); // => DELETE to /posts/2
				});
			} else if (type == "erval") {
				var controller = App.__container__.lookup("controller:definition");
				var proxySend = jQuery.proxy(controller.send, controller);
				proxySend('deleteBox', "inter" + index);
				store.find('interactionFromt0tot1', index).then(function (event) {
					event.destroyRecord(); // => DELETE to /posts/2
				});
			}
			
			else if (type == "anent") {
				var controller = App.__container__.lookup("controller:definition");
				var proxySend = jQuery.proxy(controller.send, controller);
				proxySend('deleteBox', "perma" + index);
				store.find('experimentWideConf', index).then(function (event) {
					event.destroyRecord(); // => DELETE to /posts/2
				});
			}

			this.transitionToRoute('definition');
		},
	},
});
