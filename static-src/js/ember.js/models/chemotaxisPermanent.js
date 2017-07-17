App.ChemotaxisPermanent = DS.Model.extend( App.savingMixin, {
	description: DS.attr('string'),
	chemicalCategory: DS.attr('string'),
	osmoticRing: DS.belongsTo('osmoticRing', {async: true}),
	staticPointSourceConf: DS.belongsTo('staticPointSource', {async: true}),
	chemotaxisQuadrants1: DS.belongsTo('chemotaxisQuadrants1', {async: true}),
	chemotaxisQuadrants2: DS.belongsTo('chemotaxisQuadrants2', {async: true}),
	chemotaxisQuadrants4: DS.belongsTo('chemotaxisQuadrants4', {async: true}),
});