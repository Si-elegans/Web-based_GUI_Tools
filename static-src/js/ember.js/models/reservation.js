App.Reservation = DS.Model.extend( App.savingMixin, {

	start_time: DS.attr('number'),
	resume_timestamp: DS.attr('number'),
	status: DS.attr('string'),
  creator: DS.belongsTo('user', {async: true}),
  experiment: DS.belongsTo('behaviouralExperiment', {async: true})
});