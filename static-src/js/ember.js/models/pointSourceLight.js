App.PointSourceLight = DS.Model.extend( App.savingMixin, {
	waveLength: DS.attr('number'),
	intensity: DS.attr('number'),
	lightingPointDistance: DS.attr('number'),
	lightBeamRadius: DS.attr('number'),
});