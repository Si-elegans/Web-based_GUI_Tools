Ember.TEMPLATES["permanent"] = Ember.Handlebars.template({"1":function(depth0,helpers,partials,data) {
  var escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push("			<button ");
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "deleteEvent", {"name":"action","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING"],"contexts":[depth0],"data":data})));
  data.buffer.push(" class=\"btn btn-turquesa\" style=\"margin: 5px\">Delete This Event</button>\r\n");
  return buffer;
},"3":function(depth0,helpers,partials,data) {
  var helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push(escapeExpression(((helpers.render || (depth0 && depth0.render) || helperMissing).call(depth0, "mechanosensationPermanent", "mechanosensation", {"name":"render","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING","ID"],"contexts":[depth0,depth0],"data":data}))));
  data.buffer.push("\r\n");
  return buffer;
},"5":function(depth0,helpers,partials,data) {
  var helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push(escapeExpression(((helpers.render || (depth0 && depth0.render) || helperMissing).call(depth0, "phototaxisPermanent", "phototaxis", {"name":"render","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING","ID"],"contexts":[depth0,depth0],"data":data}))));
  data.buffer.push("\r\n");
  return buffer;
},"7":function(depth0,helpers,partials,data) {
  var helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push(escapeExpression(((helpers.render || (depth0 && depth0.render) || helperMissing).call(depth0, "chemotaxisPermanent", "chemotaxis", {"name":"render","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING","ID"],"contexts":[depth0,depth0],"data":data}))));
  data.buffer.push("\r\n");
  return buffer;
},"9":function(depth0,helpers,partials,data) {
  var helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push(escapeExpression(((helpers.render || (depth0 && depth0.render) || helperMissing).call(depth0, "galvanotaxisPermanent", "galvanotaxis", {"name":"render","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING","ID"],"contexts":[depth0,depth0],"data":data}))));
  data.buffer.push("\r\n");
  return buffer;
},"11":function(depth0,helpers,partials,data) {
  var helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push(escapeExpression(((helpers.render || (depth0 && depth0.render) || helperMissing).call(depth0, "termotaxisPermanent", "termotaxis", {"name":"render","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING","ID"],"contexts":[depth0,depth0],"data":data}))));
  data.buffer.push("\r\n");
  return buffer;
},"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push("<div class=\"row\">\r\n	<div class=\"col-sm-12\">\r\n		<div class=\"hcontrols\">\r\n");
  stack1 = helpers['if'].call(depth0, "isModifiable", {"name":"if","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(1, data),"inverse":this.noop,"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  data.buffer.push("		</div>\r\n	</div>\r\n</div>\r\n<div class=\"row\">\r\n	<div class=\"col-sm-12\">\r\n		<div class=\" title\">Description</div>\r\n	</div>\r\n</div>\r\n<div class=\"row\">\r\n	<div class=\"col-sm-12 block\">\r\n		<div>\r\n			");
  data.buffer.push(escapeExpression(((helpers.input || (depth0 && depth0.input) || helperMissing).call(depth0, {"name":"input","hash":{
    'value': ("model.description"),
    'class': (""),
    'id': ("permanentDescription")
  },"hashTypes":{'value': "ID",'class': "STRING",'id': "STRING"},"hashContexts":{'value': depth0,'class': depth0,'id': depth0},"types":[],"contexts":[],"data":data}))));
  data.buffer.push("\r\n		</div>\r\n	</div>\r\n</div>\r\n");
  stack1 = helpers['if'].call(depth0, "isMechano", {"name":"if","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(3, data),"inverse":this.noop,"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  stack1 = helpers['if'].call(depth0, "isPhoto", {"name":"if","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(5, data),"inverse":this.noop,"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  stack1 = helpers['if'].call(depth0, "isChemo", {"name":"if","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(7, data),"inverse":this.noop,"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  stack1 = helpers['if'].call(depth0, "isGalvano", {"name":"if","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(9, data),"inverse":this.noop,"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  stack1 = helpers['if'].call(depth0, "isTermo", {"name":"if","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(11, data),"inverse":this.noop,"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  return buffer;
},"useData":true});