App.PlateConfiguration = DS.Model.extend( App.savingMixin, {
	lid: DS.attr('boolean'),
	dryness: DS.attr('number'),
	bottomMaterial: DS.attr('string'),
	shape: DS.attr('string'),
	Cylinder: DS.belongsTo('cylinder', {async: true}),
	Cube: DS.belongsTo('cube', {async: true}),
	Hexagon: DS.belongsTo('hexagon', {async: true}),
});