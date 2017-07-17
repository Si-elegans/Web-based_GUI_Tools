App.Crowding = DS.Model.extend( App.savingMixin, {
	wormsInPlate: DS.attr('number'),
	wormsDistributionInPlate: DS.attr('string')
});