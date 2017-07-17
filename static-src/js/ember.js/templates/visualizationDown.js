Ember.TEMPLATES["visualizationDown"] = Ember.Handlebars.template({"1":function(depth0,helpers,partials,data) {
  var escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push("                <button ");
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "changeIsInTimeline", {"name":"action","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING"],"contexts":[depth0],"data":data})));
  data.buffer.push(" class=\"btn btn-turquesa\" style=\"margin: 5px\"> Voltages </button>\r\n");
  return buffer;
},"3":function(depth0,helpers,partials,data) {
  var escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push("                <button ");
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "changeIsInTimeline", {"name":"action","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING"],"contexts":[depth0],"data":data})));
  data.buffer.push(" class=\"btn btn-turquesa\" style=\"margin: 5px\"> Timeline </button>\r\n");
  return buffer;
},"5":function(depth0,helpers,partials,data) {
  var escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push("            ");
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "visualizationTimeline", {"name":"view","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING"],"contexts":[depth0],"data":data})));
  data.buffer.push("\r\n");
  return buffer;
},"7":function(depth0,helpers,partials,data) {
  var stack1, buffer = '';
  data.buffer.push("            <div class=\"col-sm-12 htimelinebox scrolly\">\r\n");
  stack1 = helpers.each.call(depth0, "neuron", "in", "neurons", {"name":"each","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(8, data),"inverse":this.noop,"types":["ID","ID","ID"],"contexts":[depth0,depth0,depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  data.buffer.push("            </div>\r\n");
  return buffer;
},"8":function(depth0,helpers,partials,data) {
  var stack1, buffer = '';
  stack1 = helpers['if'].call(depth0, "neuron.selected", {"name":"if","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(9, data),"inverse":this.noop,"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  return buffer;
},"9":function(depth0,helpers,partials,data) {
  var helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push("                <div class=\"row\">\r\n                    ");
  data.buffer.push(escapeExpression(((helpers.render || (depth0 && depth0.render) || helperMissing).call(depth0, "visualizationGraph", "neuron", {"name":"render","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING","ID"],"contexts":[depth0,depth0],"data":data}))));
  data.buffer.push("\r\n                </div>\r\n");
  return buffer;
},"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push("<div class=\"col-sm-12 wrap\">\r\n    <div class=\"row\">\r\n        <div class=\"col-sm-12 wrap\">\r\n            <div class=\"hcontrols row\">\r\n");
  stack1 = helpers['if'].call(depth0, "isInTimeline", {"name":"if","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(1, data),"inverse":this.program(3, data),"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  data.buffer.push("                <button ");
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "playAnimation", {"name":"action","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING"],"contexts":[depth0],"data":data})));
  data.buffer.push(" class=\"glyphicon glyphicon-play btn btn-turquesa2\"></button>\r\n                <button class=\"glyphicon glyphicon-stop btn btn-turquesa2\"></button>\r\n                <img src=\"static/data/vel50.png\"></img>\r\n                <img src=\"static/data/opa10.png\"></img>\r\n            </div>\r\n        </div>\r\n    </div>\r\n    <div class=\"row translucent\">\r\n");
  stack1 = helpers['if'].call(depth0, "isInTimeline", {"name":"if","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(5, data),"inverse":this.program(7, data),"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  data.buffer.push("    </div>\r\n    <canvas id=\"timelineCanvas\" class=\"timelineCanvas\"></canvas>\r\n</div>\r\n");
  return buffer;
},"useData":true});