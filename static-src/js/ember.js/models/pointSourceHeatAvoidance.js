App.PointSourceHeatAvoidance = DS.Model.extend( App.savingMixin, {
	temperature: DS.attr('number'),
	heatPointDistance: DS.attr('number'),
});