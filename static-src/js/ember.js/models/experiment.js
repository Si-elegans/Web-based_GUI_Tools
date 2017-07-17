App.Experiment = DS.Model.extend( App.savingMixin, {
	description: DS.attr('string'),
    experimentDuration: DS.attr('number'),
	interactionAtSpecificTime: DS.hasMany('interactionAtSpecificTime', {async: true}),
	interactionFromt0tot1: DS.hasMany('interactionFromt0tot1', {async: true}),
	experimentWideConf: DS.hasMany('experimentWideConf', {async: true})
});