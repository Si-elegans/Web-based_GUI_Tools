App.DirectTouch = DS.Model.extend( App.savingMixin, {
	directTouchInstrument: DS.attr('string'),
	touchDistance: DS.attr('number'),
	touchAngle: DS.attr('number'),
	appliedForce: DS.attr('number'),
});