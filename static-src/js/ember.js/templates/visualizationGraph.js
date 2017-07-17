Ember.TEMPLATES["visualizationGraph"] = Ember.Handlebars.template({"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push("<div class=\"col-sm-1\">\r\n    ");
  data.buffer.push(escapeExpression(((helpers.divName || (depth0 && depth0.divName) || helperMissing).call(depth0, "neuron.name", {"name":"divName","hash":{},"hashTypes":{},"hashContexts":{},"types":["ID"],"contexts":[depth0],"data":data}))));
  data.buffer.push("\r\n</div>\r\n<div class=\"col-sm-11\">\r\n    ");
  data.buffer.push(escapeExpression(((helpers.voltageName || (depth0 && depth0.voltageName) || helperMissing).call(depth0, "neuron.name", {"name":"voltageName","hash":{},"hashTypes":{},"hashContexts":{},"types":["ID"],"contexts":[depth0],"data":data}))));
  data.buffer.push("\r\n</div>\r\n");
  return buffer;
},"useData":true});