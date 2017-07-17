App.VisualizationTimelineView = Ember.View.extend({
    classNames: ["row"],
    templateName: "visualizationTimeline",
    didInsertElement: function () {
        var visActions = [];
        this.get('controller.controllers.experiment.model.experimentDefinition').then(function (data) {
            var options = {
                editable: false,
                selectable: false,
                height: '12em',
                showMajorLabels: false,
                moveable: false,
                start: new Number(0),
                end: new Number(data.get('experimentDuration'))
            };
            data.get('interactionAtSpecificTime').then(function (interactionTimes) {
                interactionTimes.forEach(function (item) {
                    var action = {
                        'id': item.get('id'),
                        'start': new Number(item.get('eventTime')),
                        'content': new String(item.get('idx')),
                        'type': 'box',
                        'eventType': 'exact'
                    }
                    visActions[visActions.length] = action;
                });

                var data = new vis.DataSet(visActions);


                // specify options

                // create the timeline
                var timelineContainer = this.$("#mytimeline");
                var timeline = new vis.Timeline(timelineContainer[0], data, options);
                timeline.on('select', function (properties) {
                    if (properties.items.length > 0) {
                        var controller = App.__container__.lookup("controller:definition");
                        var proxySend = jQuery.proxy(controller.send, controller);
                        proxySend('changeToEvent', this.itemsData._getItem(properties.items[0]));
                    }
                    //this.transitionTo()
                });
            });
        });
    }


});