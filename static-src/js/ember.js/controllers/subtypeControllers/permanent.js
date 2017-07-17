App.PermanentController = Ember.ObjectController.extend({
	needs: ["experiment"],
	isModifiable : true,
    templateName: function(){
        if(this.get('model.experimentCategory')=="MS"){
			return 'mechanosensationInterval';
		}
		else if(this.get('model.experimentCategory')=="TT"){
			return 'termotaxisInterval';
		}
		else if(this.get('model.experimentCategory')=="CT"){
			return 'chemotaxisInterval';
		}
		else if(this.get('model.experimentCategory')=="GT"){
			return 'galvanotaxisInterval';
		}
		else if(this.get('model.experimentCategory')=="PT"){
			return 'phototaxisInterval';
		}
		else{
			return 'error';
		}
    }.property('experimentCategory'),
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
	
	updateEventDescription: function(){
		var controller = App.__container__.lookup("controller:definition");
		var proxySend = jQuery.proxy(controller.send, controller);
		proxySend('updateTimelineBoxName', "perma" + this.get('model.id'), this.get('model.description'));
	}.observes('model.description'),
	
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

		this.transitionToRoute('event');
	},
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
