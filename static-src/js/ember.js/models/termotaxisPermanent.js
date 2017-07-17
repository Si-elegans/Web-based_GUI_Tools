App.TermotaxisPermanent = DS.Model.extend( App.savingMixin, {
	description: DS.attr('string'),
	termotaxisType: DS.attr('string'),
	linearThermalGradient: DS.belongsTo('linearThermalGradient', {async: true}),
});