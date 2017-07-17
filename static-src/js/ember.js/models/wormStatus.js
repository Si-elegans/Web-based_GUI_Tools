App.WormStatus = DS.Model.extend( App.savingMixin, {
	xCoordFromPlateCentre: DS.attr('number'),
	yCoorDFromPlateCentre: DS.attr('number'),
	angleRelativeXaxis: DS.attr('number'),
	wormData: DS.belongsTo('wormDatum', {async: true})
});