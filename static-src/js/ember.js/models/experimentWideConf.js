App.ExperimentWideConf = DS.Model.extend( App.savingMixin, {
	eventTime: DS.attr('number'),
	experimentCategory: DS.attr('string'),
	description: DS.attr('string'),
	mechanosensation: DS.belongsTo('mechanosensationPermanent', {async: true}),
	chemotaxis: DS.belongsTo('chemotaxisPermanent', {async: true}),
	termotaxis: DS.belongsTo('termotaxisPermanent', {async: true}),
	galvanotaxis: DS.belongsTo('galvanotaxisPermanent', {async: true}),
	phototaxis: DS.belongsTo('phototaxisExact', {async: true}),
});