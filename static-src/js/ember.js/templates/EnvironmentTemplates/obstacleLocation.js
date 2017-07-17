Ember.TEMPLATES["obstacleLocation"] = Ember.Handlebars.template({"1":function(depth0,helpers,partials,data) {
  var helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push(escapeExpression(((helpers.render || (depth0 && depth0.render) || helperMissing).call(depth0, "cylinder", "Cylinder", {"name":"render","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING","ID"],"contexts":[depth0,depth0],"data":data}))));
  data.buffer.push("\r\n");
  return buffer;
},"3":function(depth0,helpers,partials,data) {
  var helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push(escapeExpression(((helpers.render || (depth0 && depth0.render) || helperMissing).call(depth0, "cube", "Cube", {"name":"render","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING","ID"],"contexts":[depth0,depth0],"data":data}))));
  data.buffer.push("\r\n");
  return buffer;
},"5":function(depth0,helpers,partials,data) {
  var helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push(escapeExpression(((helpers.render || (depth0 && depth0.render) || helperMissing).call(depth0, "hexagon", "Hexagon", {"name":"render","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING","ID"],"contexts":[depth0,depth0],"data":data}))));
  data.buffer.push("\r\n");
  return buffer;
},"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, escapeExpression=this.escapeExpression, helperMissing=helpers.helperMissing, buffer = '';
  data.buffer.push("<div class=\"row\">\r\n	<div class=\"col-sm-8\">\r\n		<div class=\"title2\">");
  stack1 = helpers._triageMustache.call(depth0, "shapeName", {"name":"_triageMustache","hash":{},"hashTypes":{},"hashContexts":{},"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  data.buffer.push("</div>\r\n	</div>\r\n	<div class=\"col-sm-4\">\r\n		<button class=\"btn btn-turquesa\"><span class=\"glyphicon glyphicon-minus\" aria-hidden=\"true\" ");
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "removeObstacle", "id", {"name":"action","hash":{},"hashTypes":{},"hashContexts":{},"types":["STRING","ID"],"contexts":[depth0,depth0],"data":data})));
  data.buffer.push("></span>&nbsp</button>\r\n	</div>\r\n</div>\r\n<div class=\"row\">\r\n    <div class=\"col-sm-12 block\">\r\n        <div>\r\n            <div class=\"whitefont\">Distance to Plate Centre X</div>\r\n            ");
  data.buffer.push(escapeExpression(((helpers.input || (depth0 && depth0.input) || helperMissing).call(depth0, {"name":"input","hash":{
    'data-slider-value': ("xCoordFromPlateCentre"),
    'data-slider-step': ("0.1"),
    'data-slider-min': ("0"),
    'type': ("text"),
    'data-slider-id': ("distanceXId"),
    'class': ("simpleSlider"),
    'id': ("distanceXId")
  },"hashTypes":{'data-slider-value': "ID",'data-slider-step': "STRING",'data-slider-min': "STRING",'type': "STRING",'data-slider-id': "ID",'class': "STRING",'id': "ID"},"hashContexts":{'data-slider-value': depth0,'data-slider-step': depth0,'data-slider-min': depth0,'type': depth0,'data-slider-id': depth0,'class': depth0,'id': depth0},"types":[],"contexts":[],"data":data}))));
  data.buffer.push("   \r\n        </div>\r\n    </div>\r\n</div>\r\n<div class=\"row\">\r\n    <div class=\"col-sm-12 block\">\r\n        <div>\r\n            <div class=\"whitefont\">Distance to Plate Centre Y</div>\r\n            ");
  data.buffer.push(escapeExpression(((helpers.input || (depth0 && depth0.input) || helperMissing).call(depth0, {"name":"input","hash":{
    'data-slider-value': ("yCoorDFromPlateCentre"),
    'data-slider-step': ("0.1"),
    'data-slider-min': ("0"),
    'type': ("text"),
    'data-slider-id': ("distanceYId"),
    'class': ("simpleSlider"),
    'id': ("distanceYId")
  },"hashTypes":{'data-slider-value': "ID",'data-slider-step': "STRING",'data-slider-min': "STRING",'type': "STRING",'data-slider-id': "ID",'class': "STRING",'id': "ID"},"hashContexts":{'data-slider-value': depth0,'data-slider-step': depth0,'data-slider-min': depth0,'type': depth0,'data-slider-id': depth0,'class': depth0,'id': depth0},"types":[],"contexts":[],"data":data}))));
  data.buffer.push("     \r\n        </div>\r\n    </div>\r\n</div>\r\n<div class=\"row\">\r\n    <div class=\"col-sm-12 block\">\r\n        <div>\r\n            <div class=\"whitefont\">Stiffness</div>\r\n            ");
  data.buffer.push(escapeExpression(((helpers.input || (depth0 && depth0.input) || helperMissing).call(depth0, {"name":"input","hash":{
    'data-slider-value': ("Stiffness"),
    'data-slider-step': ("0.1"),
    'data-slider-min': ("0"),
    'type': ("text"),
    'data-slider-id': ("stiffnessId"),
    'class': ("simpleSlider"),
    'id': ("stiffnessId")
  },"hashTypes":{'data-slider-value': "ID",'data-slider-step': "STRING",'data-slider-min': "STRING",'type': "STRING",'data-slider-id': "ID",'class': "STRING",'id': "ID"},"hashContexts":{'data-slider-value': depth0,'data-slider-step': depth0,'data-slider-min': depth0,'type': depth0,'data-slider-id': depth0,'class': depth0,'id': depth0},"types":[],"contexts":[],"data":data}))));
  data.buffer.push("      \r\n        </div>\r\n    </div>\r\n</div>\r\n");
  stack1 = helpers['if'].call(depth0, "isCylinder", {"name":"if","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(1, data),"inverse":this.noop,"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  stack1 = helpers['if'].call(depth0, "isCube", {"name":"if","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(3, data),"inverse":this.noop,"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  stack1 = helpers['if'].call(depth0, "isHexagon", {"name":"if","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(5, data),"inverse":this.noop,"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  return buffer;
},"useData":true});