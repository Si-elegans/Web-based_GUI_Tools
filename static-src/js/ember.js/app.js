App = Ember.Application.create({
    rootElement: '#ember-app',
	currentPath: '',
});


App.Router.map(function() {
  this.resource('experiments',{path:'/experiments'});
  this.resource('experiment', { path: '/experiment/:experiment_id'},function() {
	this.resource('definition', function() {
	    this.resource('environment', { path: 'environment'});
		this.resource('exact',{path:'exact/:event_id'});
		this.resource('interval',{path:'interval/:event_id'});
		this.resource('permanent',{path:'permanent/:event_id'});
	});
	this.resource('visualization');
  });
});

App.ApplicationController = Ember.Controller.extend({
  updateCurrentPath: function() {
    App.set('currentPath', this.get('currentPath'));
  }.observes('currentPath'),
  init: function () {
    this._super();
    Ember.run.schedule("afterRender",this,function() {
      this.send("updatePlateShape");
    });
  },
  actions: {
    updatePlateShape: function() {
    }
  },
});

/*Ember.Application.initializer({
  name: "store",

  initialize: function(container, application) {
    container.register('store:main', App.Store, { singleton: true });
  }
});

Ember.Application.initializer({
  name: "injectStore",
  before: "store",

  initialize: function(container, application) {
    application.inject('RESTAdapter', 'store', 'store:main');
  }
});*/
