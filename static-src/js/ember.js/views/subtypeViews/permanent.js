App.PermanentView = Ember.View.extend({
    classNames:["col-sm-12", "wrap"],
  didInsertElement: function() {
        var eventController = this.get('controller');
			var self = this;
			var eventModel = this.get('controller.model');
			//});
			var controller = App.__container__.lookup("controller:definition");
			var proxySend = jQuery.proxy(controller.send, controller);
			proxySend('setSelectedBox', "perma" + this.get('controller.model.id'));
  },
          
            
});