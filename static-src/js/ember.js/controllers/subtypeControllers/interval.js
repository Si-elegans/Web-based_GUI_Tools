App.IntervalController = Ember.ObjectController.extend({
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
		proxySend('updateTimelineBoxName', "inter" + this.get('model.id'), this.get('model.description'));
	}.observes('model.description'),
	
	eventInterval: function(){
		var str = '"[' + this.get('model.eventStartTime') + ',' + this.get('model.eventStartTime') + ']"';
		return str;
	}.property('model.eventStartTime').property('model.eventStopTime'),

	
	updateEventStartTime: function(){
		var slider = this.get('intervalTimeSlider');
		if(slider){
			slider.setValue([parseFloat(this.get('model.eventStartTime')),parseFloat(this.get('model.eventStopTime'))]);
			slider.options.value[0]=parseFloat(this.get('model.eventStartTime'));
			slider.options.value[1]=parseFloat(this.get('model.eventStopTime'));
			var controller = App.__container__.lookup("controller:definition");
			var proxySend = jQuery.proxy(controller.send, controller);
			proxySend('updateTimelineBoxStart', "inter" + this.get('model.id'), parseFloat(this.get('model.eventStartTime')));
		}
	}.observes('model.eventStartTime'),
	updateEventStopTime: function(){
		var slider = this.get('intervalTimeSlider');
		if(slider){
			slider.setValue([parseFloat(this.get('model.eventStartTime')),parseFloat(this.get('model.eventStopTime'))]);
			slider.options.value[0]=parseFloat(this.get('model.eventStartTime'));
			slider.options.value[1]=parseFloat(this.get('model.eventStopTime'));
			var controller = App.__container__.lookup("controller:definition");
			var proxySend = jQuery.proxy(controller.send, controller);
			proxySend('updateTimelineBoxStop', "inter" + this.get('model.id'), parseFloat(this.get('model.eventStopTime')));
		}
	}.observes('model.eventStopTime'),
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

		this.transitionToRoute('definition');
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
