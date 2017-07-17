App.InteractionAtSpecificTime = DS.Model.extend(App.savingMixin,{
	eventTime: DS.attr('number'),
	experimentCategory: DS.attr('string'),
	description: DS.attr('string'),
	mechanosensation: DS.belongsTo('mechanosensationExact', {async: true}),
	chemotaxis: DS.belongsTo('chemotaxisExact', {async: true}),
	termotaxis: DS.belongsTo('termotaxisExact', {async: true}),
	galvanotaxis: DS.belongsTo('galvanotaxisExact', {async: true}),
	phototaxis: DS.belongsTo('phototaxisExact', {async: true}),
	
});