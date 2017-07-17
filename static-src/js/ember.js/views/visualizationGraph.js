App.VisualizationGraphView = Ember.View.extend({
    classNames: ["row"],
    didInsertElement: function () {
        var name = "#voltage" + this.get('controller.model.name');
        var chart = dc.seriesChart(name);
        var ndx, runDimension, runGroup;
        var voltages = this.get('controller.model.voltages');
        ndx = crossfilter(voltages);
        runDimension = ndx.dimension(function (d) {
            return [+d.Expt, +d.Run];
        });
        runGroup = runDimension.group().reduceSum(function (d) {
            return +d.Speed;
        });
        chart
                .width(null)
                .height(80)
                .chart(function (c) {
                    return dc.lineChart(c).interpolate('basis');
                })
                .x(d3.scale.linear().domain([0, 20]))
                .y(d3.scale.linear().domain([0, 90]))
                .brushOn(false)
                .clipPadding(10)
                .elasticY(true)
                .dimension(runDimension)
                .group(runGroup)
                .mouseZoomable(false)
                .seriesAccessor(function (d) {
                    return "Expt: " + d.key[0];
                })
                .keyAccessor(function (d) {
                    return +d.key[1];
                })
                .valueAccessor(function (d) {
                    return +d.value;
                })
                .legend(dc.legend().x(350).y(350).itemHeight(13).gap(5).horizontal(1).legendWidth(140).itemWidth(70));
        chart.yAxis().tickFormat(function (d) {
            //return d3.format(',d')(d + 100);
            return "";
        });
        chart.margins().left += 10;
        dc.renderAll();
    }


});