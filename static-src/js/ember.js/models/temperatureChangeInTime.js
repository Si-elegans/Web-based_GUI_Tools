App.TemperatureChangeInTime = DS.Model.extend( App.savingMixin, {
	initialTemperature: DS.attr('number'),
    finalTemperature: DS.attr('number'),
});