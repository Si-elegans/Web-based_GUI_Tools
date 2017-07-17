App.ElectricShock = DS.Model.extend( App.savingMixin, {
	amplitude: DS.attr('number'),
	shockDuration: DS.attr('number'),
	shockFrequency: DS.attr('number'),
});