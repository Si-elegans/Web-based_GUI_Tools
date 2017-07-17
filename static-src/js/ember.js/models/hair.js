App.Hair = DS.Model.extend( App.savingMixin, {

	length: DS.attr('number'),
	radius: DS.attr('number'),
	foldAngle: DS.attr('number')
});