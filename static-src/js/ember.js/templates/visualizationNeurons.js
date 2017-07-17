Ember.TEMPLATES["visualizationNeurons"] = Ember.Handlebars.template({"1":function(depth0,helpers,partials,data) {
  var stack1, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push("            <button  ");
  data.buffer.push(escapeExpression(helpers['bind-attr'].call(depth0, {"name":"bind-attr","hash":{
    'class': ("neuron.isSpiking:btn-naranja:btn-turquesa3")
  },"hashTypes":{'class': "STRING"},"hashContexts":{'class': depth0},"types":[],"contexts":[],"data":data})));
  data.buffer.push(" ");
  data.buffer.push(escapeExpression(helpers['bind-attr'].call(depth0, {"name":"bind-attr","hash":{
    'id': ("neuron.name")
  },"hashTypes":{'id': "STRING"},"hashContexts":{'id': depth0},"types":[],"contexts":[],"data":data})));
  data.buffer.push(">");
  stack1 = helpers._triageMustache.call(depth0, "neuron.name", {"name":"_triageMustache","hash":{},"hashTypes":{},"hashContexts":{},"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  data.buffer.push("</button>\r\n");
  return buffer;
},"3":function(depth0,helpers,partials,data) {
  var stack1, buffer = '';
  stack1 = helpers['if'].call(depth0, "neuron.selected", {"name":"if","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(4, data),"inverse":this.noop,"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  return buffer;
},"4":function(depth0,helpers,partials,data) {
  var helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push("  <div class=\"\">\r\n    ");
  data.buffer.push(escapeExpression(((helpers.collapse1 || (depth0 && depth0.collapse1) || helperMissing).call(depth0, "neuron.name", {"name":"collapse1","hash":{},"hashTypes":{},"hashContexts":{},"types":["ID"],"contexts":[depth0],"data":data}))));
  data.buffer.push("\r\n    ");
  data.buffer.push(escapeExpression(((helpers.collapse2 || (depth0 && depth0.collapse2) || helperMissing).call(depth0, "neuron", {"name":"collapse2","hash":{},"hashTypes":{},"hashContexts":{},"types":["ID"],"contexts":[depth0],"data":data}))));
  data.buffer.push("\r\n  </div>\r\n");
  return buffer;
},"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, buffer = '';
  data.buffer.push("<div class=\"row\">\r\n    <div class=\"col-sm-12\">\r\n        <div class=\" title\">Neurons and muscles</div>\r\n    </div>\r\n</div>\r\n<div class=\"row\">\r\n    <div class=\"col-sm-12\">\r\n        <div class=\"neurons\">\r\n");
  stack1 = helpers.each.call(depth0, "neuron", "in", "neurons", {"name":"each","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(1, data),"inverse":this.noop,"types":["ID","ID","ID"],"contexts":[depth0,depth0,depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  data.buffer.push("        </div>\r\n    </div>\r\n</div>\r\n<div class=\"panel-group\" id=\"accordion\" role=\"tablist\" aria-multiselectable=\"true\">\r\n");
  stack1 = helpers.each.call(depth0, "neuron", "in", "neurons", {"name":"each","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(3, data),"inverse":this.noop,"types":["ID","ID","ID"],"contexts":[depth0,depth0,depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  data.buffer.push("</div>");
  return buffer;
},"useData":true});