App.OsmoticRing = DS.Model.extend( App.savingMixin, {
	chemicalConcentration: DS.attr('number'),
	internalRadius: DS.attr('number'),
	externalRadius: DS.attr('number'),
  ringChemical: DS.belongsTo('chemical', {async: true})
});