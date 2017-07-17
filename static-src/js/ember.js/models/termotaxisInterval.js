App.TermotaxisInterval = DS.Model.extend( App.savingMixin, {
	description: DS.attr('string'),
	termotaxisType: DS.attr('string'),
	temperatureChangeInTime: DS.belongsTo('temperatureChangeInTime', {async: true}),
	pointSourceHeatAvoidance: DS.belongsTo('pointSourceHeatAvoidance', {async: true}),
});