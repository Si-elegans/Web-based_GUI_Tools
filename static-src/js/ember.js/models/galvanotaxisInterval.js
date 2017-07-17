App.GalvanotaxisInterval = DS.Model.extend( App.savingMixin, {
	description: DS.attr('string'),
	galvanotaxisType: DS.attr('string'),
	electricShockConf: DS.belongsTo('electricShock', {async: true}),
});