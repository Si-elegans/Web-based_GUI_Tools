App.ChemotaxisQuadrants1 = DS.Model.extend( App.savingMixin, {
	quadrantChemicalConcentration: DS.attr('number'),
	quadrantChemical: DS.belongsTo('chemical', {async: true}),
});