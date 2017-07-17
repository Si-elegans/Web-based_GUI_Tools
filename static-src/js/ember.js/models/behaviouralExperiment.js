App.BehaviouralExperiment = DS.Model.extend(App.savingMixin,{
	about: DS.attr('string'),
	public: DS.attr('boolean'),
	description: DS.attr('string'),
	created: DS.attr('string'),
	creator: DS.belongsTo('user', {async: true}),
	experimentDefinition: DS.belongsTo('experiment', {async: true}),
	environmentDefinition: DS.belongsTo('environment', {async: true}),
	users_with_access: DS.hasMany('user', {async: true}),
	public_set_date: DS.attr('date')
});