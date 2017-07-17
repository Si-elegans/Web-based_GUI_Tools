App.PhototaxisExact = DS.Model.extend( App.savingMixin, {
	description: DS.attr('string'),
	phototaxisType: DS.attr('string'),
	pointSourceLightConf: DS.belongsTo('pointSourceLight', {async: true}),
});