App.Environment = DS.Model.extend( App.savingMixin, {
		description: DS.attr('string'),
		wormStatus: DS.belongsTo('wormStatus', {async: true}),
        plateConfiguration: DS.belongsTo('plateConfiguration', {async: true}),
		crowding: DS.belongsTo('crowding', {async: true}),
        obstacle: DS.hasMany('obstacleLocation', {async: true}),
		envTemp: DS.attr('number')
});