Ember.TEMPLATES["experiment"] = Ember.Handlebars.template({"1":function(depth0,helpers,partials,data) {
  var stack1, buffer = '';
  data.buffer.push("	<div class=\"col-sm-4 wrap\" >\r\n");
  stack1 = helpers['if'].call(depth0, "hasToBeCloned", {"name":"if","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(2, data),"inverse":this.noop,"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  data.buffer.push("		<div class=\"color row wrap\">\r\n			<div class=\"col-sm-2 wrap\" >\r\n			</div>\r\n");
  stack1 = helpers['if'].call(depth0, "hasToBeCloned", {"name":"if","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(4, data),"inverse":this.program(6, data),"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  data.buffer.push("				\r\n			</div>\r\n		</div>\r\n	</div>\r\n");
  return buffer;
},"2":function(depth0,helpers,partials,data) {
  data.buffer.push("		<div class=\"color row\">This experiment cannot be modified, you can view it or clone it to modify</div>\r\n");
  },"4":function(depth0,helpers,partials,data) {
  var escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push("				<div class=\"col-sm-10 wrap\" >\r\n					<button ");
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "goToDefinitionClone", {"name":"action","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING"],"contexts":[depth0],"data":data})));
  data.buffer.push(" class=\"btn btn-turquesa\" style=\"margin: 5px\"> Clone </button>\r\n					<button ");
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "goToDefinitionView", {"name":"action","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING"],"contexts":[depth0],"data":data})));
  data.buffer.push(" class=\"btn btn-turquesa\" style=\"margin: 5px\"> View </button>\r\n				</div>\r\n");
  return buffer;
},"6":function(depth0,helpers,partials,data) {
  var escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push("				<div class=\"col-sm-10 wrap\" >\r\n					<button ");
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "goToDefinitionModify", {"name":"action","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING"],"contexts":[depth0],"data":data})));
  data.buffer.push(" class=\"btn btn-turquesa\" style=\"margin: 5px\"> Modify </button>\r\n				</div>\r\n");
  return buffer;
},"8":function(depth0,helpers,partials,data) {
  var helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push("<div class=\"col-sm-4 wrap color scrolly\" >\r\n<div class=\"row\">\r\n    <div class=\"col-sm-12\">\r\n        <div class=\" title\">Experiment</div>\r\n    </div>\r\n</div>\r\n<div class=\"row\">\r\n	<div class=\"col-sm-12\">\r\n		<div class=\"whitefont\">Description</div>\r\n	</div>\r\n</div>\r\n<div class=\"row\">\r\n	<div class=\"col-sm-12 block\">\r\n		<div>\r\n			");
  data.buffer.push(escapeExpression(((helpers.input || (depth0 && depth0.input) || helperMissing).call(depth0, {"name":"input","hash":{
    'value': ("model.description"),
    'class': (""),
    'id': ("experimentDescription")
  },"hashTypes":{'value': "ID",'class': "STRING",'id': "STRING"},"hashContexts":{'value': depth0,'class': depth0,'id': depth0},"types":[],"contexts":[],"data":data}))));
  data.buffer.push("\r\n		</div>\r\n	</div>\r\n</div>\r\n	");
  data.buffer.push(escapeExpression(((helpers.outlet || (depth0 && depth0.outlet) || helperMissing).call(depth0, "properties", {"name":"outlet","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING"],"contexts":[depth0],"data":data}))));
  data.buffer.push("\r\n	</div>\r\n");
  return buffer;
},"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push("<div class=\"col-sm-8 wrap\" >\r\n    <div id=\"visor\" class=\"row hvisor\">\r\n    </div>\r\n    ");
  data.buffer.push(escapeExpression(((helpers.outlet || (depth0 && depth0.outlet) || helperMissing).call(depth0, "timeline", {"name":"outlet","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING"],"contexts":[depth0],"data":data}))));
  data.buffer.push("\r\n	<div class=\"helpText1\" >\r\n	<b>Left Click:</b> rotate; <b>Center Click:</b> zoom in/out; <b>Center Scroll:</b> zoom in/out; <b>Right Click:</b> translate    \r\n\r\n	</div>\r\n	</div>\r\n");
  stack1 = helpers['if'].call(depth0, "showButtons", {"name":"if","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(1, data),"inverse":this.program(8, data),"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  data.buffer.push("\r\n<div class=\"modal fade\" id=\"modalWaiting\" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"myModalLabel\">\r\n	<div class=\"modal-dialog\" role=\"document\">\r\n		<div class=\"modal-content color saving\">\r\n			<div class=\"modal-header\">\r\n				<h4 class=\"modal-title\" id=\"myModalLabel\">Saving</h4>\r\n			</div>\r\n		</div>\r\n	</div>\r\n</div>\r\n\r\n<div class=\"modal fade\" id=\"modalSaved\" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"myModalLabel\">\r\n	<div class=\"modal-dialog\" role=\"document\">\r\n		<div class=\"modal-content color saving\">\r\n			<div class=\"modal-header\">\r\n				<h4 class=\"modal-title\" id=\"myModalLabel\">Saved</h4>\r\n			</div>\r\n			<div class=\"modal-footer\">\r\n				<button type=\"button\" class=\"btn btn-turquesa\" data-dismiss=\"modal\">OK</button>\r\n			</div>\r\n		</div>\r\n	</div>\r\n</div>\r\n\r\n<div class=\"modal fade\" id=\"modalNotPossible\" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"myModalLabel\">\r\n	<div class=\"modal-dialog\" role=\"document\">\r\n		<div class=\"modal-content color saving\">\r\n			<div class=\"modal-header\">\r\n				<h4 class=\"modal-title\" id=\"myModalLabel\">There already exists a permanent chemotaxis event</h4>\r\n			</div>\r\n			<div class=\"modal-footer\">\r\n				<button type=\"button\" class=\"btn btn-turquesa\" data-dismiss=\"modal\">OK</button>\r\n			</div>\r\n		</div>\r\n	</div>\r\n</div>\r\n\r\n<div class=\"modal fade\" id=\"modalCreating\" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"myModalLabel\">\r\n	<div class=\"modal-dialog\" role=\"document\">\r\n		<div class=\"modal-content color saving\">\r\n			<div class=\"modal-header\">\r\n				<h4 class=\"modal-title\" id=\"myModalLabel\">Creating</h4>\r\n			</div>\r\n		</div>\r\n	</div>\r\n</div>\r\n\r\n<div class=\"modal fade\" id=\"modalLoading\" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"myModalLabel\">\r\n	<div class=\"modal-dialog\" role=\"document\">\r\n		<div class=\"modal-content color saving\">\r\n			<div class=\"modal-header\">\r\n				<h4 class=\"modal-title\" id=\"myModalLabel\">Loading</h4>\r\n			</div>\r\n		</div>\r\n	</div>\r\n</div>");
  return buffer;
},"useData":true});