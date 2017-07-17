App.ChemotaxisExact = DS.Model.extend( App.savingMixin, {
	description: DS.attr('string'),
	chemotaxisType: DS.attr('string'),
	dynamicDropTestConf: DS.belongsTo('dynamicDropTest', {async: true}),
});