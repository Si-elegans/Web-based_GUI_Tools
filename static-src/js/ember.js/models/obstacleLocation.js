App.ObstacleLocation = DS.Model.extend( App.savingMixin, {
	xCoordFromPlateCentre: DS.attr('number'),
	yCoorDFromPlateCentre: DS.attr('number'),
	angleRelativeXaxis: DS.attr('number'),
	Stiffness: DS.attr('number'),
	shape: DS.attr('string'),
	Cylinder: DS.belongsTo('cylinder', {async: true}),
	Cube: DS.belongsTo('cube', {async: true}),
	Hexagon: DS.belongsTo('hexagon', {async: true}),
	Hair: DS.belongsTo('hair', {async: true}),
});