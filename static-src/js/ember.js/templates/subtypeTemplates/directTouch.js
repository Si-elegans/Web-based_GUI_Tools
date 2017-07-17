Ember.TEMPLATES["directTouch"] = Ember.Handlebars.template({"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push("<div class=\"row\">\r\n    <div class=\"col-sm-12\">\r\n        <div class=\" title\">Force</div>\r\n    </div>\r\n</div>\r\n<div class=\"row\">\r\n    <div class=\"col-sm-12 block\">\r\n        <div>\r\n            <input id=\"touchForceSlider\" class='simpleSlider' data-slider-id='touchForceSlider' type=\"text\" data-slider-min=\"0\" data-slider-max=\"100\" data-slider-step=\"0.1\" data-slider-value=\"14\"/>     \r\n        </div>\r\n    </div>\r\n</div>\r\n<div class=\"row\">\r\n    <div class=\"col-sm-12\">\r\n        <div class=\" title\">Instrument</div>\r\n    </div>\r\n</div>\r\n<div class=\"row\">\r\n    <div class=\"col-sm-12 block\">\r\n        <div class=\"btn-group\">\r\n            <button type=\"button\" class=\"btn btn-default dropdown-toggle\" data-toggle=\"dropdown\" aria-expanded=\"false\">\r\n                ");
  stack1 = helpers._triageMustache.call(depth0, "typeName", {"name":"_triageMustache","hash":{},"hashTypes":{},"hashContexts":{},"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  data.buffer.push("<span class=\"caret\"></span>\r\n            </button>\r\n            <ul class=\"dropdown-menu\" role=\"menu\">\r\n                <li id=\"directEyebrow\" class=\"btn\">Eyebrow</li>\r\n                <li id=\"directVonfrey\" class=\"btn\">Von Frey hair</li>\r\n				<li id=\"directPlatinium\" class=\"btn\">Platinium wire</li>\r\n            </ul>\r\n        </div>\r\n    </div>\r\n</div>\r\n<div class=\"row\">\r\n    <div class=\"col-sm-12\">\r\n        <div class=\" title\">Location</div>\r\n    </div>\r\n</div>\r\n<div class=\"row\">\r\n    <div class=\"col-sm-12 block\">\r\n        <div>\r\n            <div class=\"whitefont\">Location Angle</div>\r\n            ");
  data.buffer.push(escapeExpression(((helpers.input || (depth0 && depth0.input) || helperMissing).call(depth0, {"name":"input","hash":{
    'data-slider-value': ("eventTime"),
    'data-slider-step': ("0.1"),
    'data-slider-min': ("0"),
    'type': ("text"),
    'data-slider-id': ("touchLocationAngleSlider"),
    'class': ("simpleSlider"),
    'id': ("touchLocationAngleSlider")
  },"hashTypes":{'data-slider-value': "ID",'data-slider-step': "STRING",'data-slider-min': "STRING",'type': "STRING",'data-slider-id': "STRING",'class': "STRING",'id': "STRING"},"hashContexts":{'data-slider-value': depth0,'data-slider-step': depth0,'data-slider-min': depth0,'type': depth0,'data-slider-id': depth0,'class': depth0,'id': depth0},"types":[],"contexts":[],"data":data}))));
  data.buffer.push("   \r\n        </div>\r\n    </div>\r\n</div>\r\n<div class=\"row\">\r\n    <div class=\"col-sm-12 block\">\r\n        <div>\r\n            <div class=\"whitefont\">Location Length</div>\r\n            ");
  data.buffer.push(escapeExpression(((helpers.input || (depth0 && depth0.input) || helperMissing).call(depth0, {"name":"input","hash":{
    'data-slider-value': ("eventTime"),
    'data-slider-step': ("0.1"),
    'data-slider-min': ("0"),
    'type': ("text"),
    'data-slider-id': ("touchLocationLengthSlider"),
    'class': ("simpleSlider"),
    'id': ("touchLocationLengthSlider")
  },"hashTypes":{'data-slider-value': "ID",'data-slider-step': "STRING",'data-slider-min': "STRING",'type': "STRING",'data-slider-id': "STRING",'class': "STRING",'id': "STRING"},"hashContexts":{'data-slider-value': depth0,'data-slider-step': depth0,'data-slider-min': depth0,'type': depth0,'data-slider-id': depth0,'class': depth0,'id': depth0},"types":[],"contexts":[],"data":data}))));
  data.buffer.push("     \r\n        </div>\r\n    </div>\r\n</div>");
  return buffer;
},"useData":true});