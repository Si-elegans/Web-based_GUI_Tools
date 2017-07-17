App.VisualizationGraphController = Ember.ObjectController.extend({
    needs: ["experiment"],
    experiment: Ember.computed.alias("controllers.experiment"),
    actions: {
    }
});
