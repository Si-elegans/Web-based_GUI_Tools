App.WormDatum = DS.Model.extend( App.savingMixin, {
    gender: DS.attr('string'),
    age: DS.attr('number'),
    stageOfLifeCycle: DS.attr('number'),
    timeOffFood: DS.attr('number')
});