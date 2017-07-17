App.StaticPointSource = DS.Model.extend( App.savingMixin, {
	dropQuantity: DS.attr('number'),
	chemicalConcentration: DS.attr('number'),
	xCoordFromPlateCentre: DS.attr('number'),
	yCoordFromPlateCentre: DS.attr('number'),
	chemical: DS.belongsTo('chemical', {async: true}),
});