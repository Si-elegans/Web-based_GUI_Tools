App.DefinitionView = Ember.View.extend({
		classNames : ["row"],
		didInsertElement : function () {
			var visActions = [];
			var self = this;
			this.get('controller.controllers.experiment.model.experimentDefinition').then(function (data) {
				var options = {
					editable : false,
					snap : function (date, scale, step) {
						var hour = 100;
						return Math.round(date / hour) * hour;
					},
					height : '12em',
					showMajorLabels : false,
					moveable : false,
					start : new Number(0),
					end : new Number(data.get('experimentDuration')),
					onMove : function (item, callback) {
						var controller = App.__container__.lookup("controller:exact");
						var model = controller.get('model');
						model.set('eventTime', item.start);
					},
				};
				data.get('interactionAtSpecificTime').then(function (interactionTimes) {
					interactionTimes.forEach(function (item) {
						var action = {
							'id' : "exact" + item.get('id'),
							'start' : new Number(item.get('eventTime')),
							'content' : item.get('description'),
							'type' : 'box',
							'eventType' : 'exact',
							'eventSubType' : new String(item.get('experimentCategory')),
						}
						visActions[visActions.length] = action;
					});

					data.get('interactionFromt0tot1').then(function (interactionIntervals) {
						interactionIntervals.forEach(function (item) {
							var action = {
								'id' : "inter" + item.get('id'),
								'start' : new Number(item.get('eventStartTime')),
								'end' : new Number(item.get('eventStopTime')),
								'content' : item.get('description'),
								'eventType' : 'interval',
								'eventSubType' : new String(item.get('experimentCategory')),
							}
							visActions[visActions.length] = action;
						});
						data.get('experimentWideConf').then(function (permanents) {
							permanents.forEach(function (item) {
								var action = {
									'id' : "perma" + item.get('id'),
									'start' : -100000000000000,
									'end' : 100000000000000,
									'content' :  item.get('description'),
									'eventType' : 'permanent',
									'eventSubType' : new String(item.get('experimentCategory')),
								}
								visActions[visActions.length] = action;
							});
							var data = new vis.DataSet(visActions);

							// specify options

							// create the timeline
							var timelineContainer = this.$("#mytimeline");
							var timeline = new vis.Timeline(timelineContainer[0], data, options);
							var definitionController = self.get('controller');
							definitionController.set('timeline', timeline);
							timeline.on('select', function (properties) {
								if (properties.items.length > 0) {
									var controller = App.__container__.lookup("controller:definition");
									var proxySend = jQuery.proxy(controller.send, controller);
									proxySend('changeToEvent', this.itemsData._getItem(properties.items[0]));
								}
							});
							if(self.get('controller.selectedBox')){
								timeline.setSelection(self.get('controller.selectedBox'));
							}
						});
					});
				});
			});
		}
	});
