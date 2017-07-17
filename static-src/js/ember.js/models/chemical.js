App.Chemical = DS.Model.extend( App.savingMixin, {
	chemical_name: DS.attr('string'),
	isVolatile: DS.attr('boolean'),
	volatilitySpeed: DS.attr('number'),
	diffusionCoefficient: DS.attr('number'),
});