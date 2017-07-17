App.Cube = DS.Model.extend( App.savingMixin, {

	side1Length: DS.attr('number'),
	side2Length: DS.attr('number'),
	depth: DS.attr('number')
});