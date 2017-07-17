App.MechanosensationExact = DS.Model.extend( App.savingMixin, {
	description: DS.attr('string'),
	interactionType: DS.attr('string'),
	directTouch: DS.belongsTo('directTouch', {async: true}),
	plateTap: DS.belongsTo('plateTap', {async: true})
});