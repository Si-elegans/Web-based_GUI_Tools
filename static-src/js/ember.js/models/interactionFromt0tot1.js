App.InteractionFromt0tot1 = DS.Model.extend( App.savingMixin, {
	eventStartTime: DS.attr('number'),
    eventStopTime: DS.attr('number'),
	experimentCategory: DS.attr('string'),
	description: DS.attr('string'),
	mechanosensation: DS.belongsTo('mechanosensationInterval', {async: true}),
	chemotaxis: DS.belongsTo('chemotaxisInterval', {async: true}),
	termotaxis: DS.belongsTo('termotaxisInterval', {async: true}),
	galvanotaxis: DS.belongsTo('galvanotaxisInterval', {async: true}),
	phototaxis: DS.belongsTo('phototaxisInterval', {async: true}),
});