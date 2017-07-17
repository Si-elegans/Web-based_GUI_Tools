Ember.TEMPLATES["mechanosensationExact"] = Ember.Handlebars.template({"1":function(depth0,helpers,partials,data) {
  var helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push(escapeExpression(((helpers.render || (depth0 && depth0.render) || helperMissing).call(depth0, "directTouch", "directTouch", {"name":"render","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING","ID"],"contexts":[depth0,depth0],"data":data}))));
  data.buffer.push("\r\n");
  return buffer;
},"3":function(depth0,helpers,partials,data) {
  var helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push(escapeExpression(((helpers.render || (depth0 && depth0.render) || helperMissing).call(depth0, "plateTap", "plateTap", {"name":"render","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING","ID"],"contexts":[depth0,depth0],"data":data}))));
  data.buffer.push("\r\n");
  return buffer;
},"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, buffer = '';
  data.buffer.push("<div class=\"row\">\r\n    <div class=\"col-sm-12\">\r\n        <div class=\" title\">Experiment type</div>\r\n    </div>\r\n</div>\r\n<div class=\"row\">\r\n    <div class=\"col-sm-12 block\"> \r\n        <div class=\"btn-group\">\r\n            <button type=\"button\" class=\"btn btn-default dropdown-toggle\" data-toggle=\"dropdown\" aria-expanded=\"false\">\r\n                ");
  stack1 = helpers._triageMustache.call(depth0, "typeName", {"name":"_triageMustache","hash":{},"hashTypes":{},"hashContexts":{},"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  data.buffer.push("<span class=\"caret\"></span>\r\n            </button>\r\n            <ul class=\"dropdown-menu\" role=\"menu\">\r\n                <li id=\"mechanoTouch\" class=\"btn\">Direct Touch</li>\r\n				<li id=\"mechanoPlate\" class=\"btn\">Plate Tap</li>\r\n            </ul>\r\n        </div>\r\n    </div>\r\n</div>\r\n");
  stack1 = helpers['if'].call(depth0, "isTouch", {"name":"if","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(1, data),"inverse":this.noop,"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  stack1 = helpers['if'].call(depth0, "isPlate", {"name":"if","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(3, data),"inverse":this.noop,"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  return buffer;
},"useData":true});