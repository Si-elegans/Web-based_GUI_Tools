App.ChemotaxisQuadrants2 = DS.Model.extend( App.savingMixin, {
	quadrant_1_ChemicalConcentration: DS.attr('number'),
	quadrant_2_ChemicalConcentration: DS.attr('number'),
	quadrant_1_Chemical: DS.belongsTo('chemical', {async: true}),
	quadrant_2_Chemical: DS.belongsTo('chemical', {async: true}),
	
	quadrantBarrierChemicalConcentration: DS.attr('number'),
	quadrantBarrierChemical: DS.belongsTo('chemical', {async: true}),
});