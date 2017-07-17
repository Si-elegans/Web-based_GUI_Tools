Ember.TEMPLATES["cube"] = Ember.Handlebars.template({"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push("<div class=\"row\">\r\n    <div class=\"col-sm-12 block\">\r\n        <div>\r\n            <div class=\"whitefont\">Cube Side 1 Length</div>\r\n            ");
  data.buffer.push(escapeExpression(((helpers.input || (depth0 && depth0.input) || helperMissing).call(depth0, {"name":"input","hash":{
    'data-slider-value': ("side1Length"),
    'data-slider-step': ("0.1"),
    'data-slider-min': ("0"),
    'type': ("text"),
    'data-slider-id': ("side1Id"),
    'class': ("simpleSlider"),
    'id': ("side1Id")
  },"hashTypes":{'data-slider-value': "ID",'data-slider-step': "STRING",'data-slider-min': "STRING",'type': "STRING",'data-slider-id': "ID",'class': "STRING",'id': "ID"},"hashContexts":{'data-slider-value': depth0,'data-slider-step': depth0,'data-slider-min': depth0,'type': depth0,'data-slider-id': depth0,'class': depth0,'id': depth0},"types":[],"contexts":[],"data":data}))));
  data.buffer.push("   \r\n        </div>\r\n    </div>\r\n</div>\r\n<div class=\"row\">\r\n    <div class=\"col-sm-12 block\">\r\n        <div>\r\n            <div class=\"whitefont\">Cube Side 2 Length</div>\r\n            ");
  data.buffer.push(escapeExpression(((helpers.input || (depth0 && depth0.input) || helperMissing).call(depth0, {"name":"input","hash":{
    'data-slider-value': ("side2Length"),
    'data-slider-step': ("0.1"),
    'data-slider-min': ("0"),
    'type': ("text"),
    'data-slider-id': ("side2Id"),
    'class': ("simpleSlider"),
    'id': ("side2Id")
  },"hashTypes":{'data-slider-value': "ID",'data-slider-step': "STRING",'data-slider-min': "STRING",'type': "STRING",'data-slider-id': "ID",'class': "STRING",'id': "ID"},"hashContexts":{'data-slider-value': depth0,'data-slider-step': depth0,'data-slider-min': depth0,'type': depth0,'data-slider-id': depth0,'class': depth0,'id': depth0},"types":[],"contexts":[],"data":data}))));
  data.buffer.push("   \r\n        </div>\r\n    </div>\r\n</div>\r\n<div class=\"row\">\r\n    <div class=\"col-sm-12 block\">\r\n        <div>\r\n            <div class=\"whitefont\">Cube Depth</div>\r\n            ");
  data.buffer.push(escapeExpression(((helpers.input || (depth0 && depth0.input) || helperMissing).call(depth0, {"name":"input","hash":{
    'data-slider-value': ("depth"),
    'data-slider-step': ("0.1"),
    'data-slider-min': ("0"),
    'type': ("text"),
    'data-slider-id': ("depthId"),
    'class': ("simpleSlider"),
    'id': ("depthId")
  },"hashTypes":{'data-slider-value': "ID",'data-slider-step': "STRING",'data-slider-min': "STRING",'type': "STRING",'data-slider-id': "ID",'class': "STRING",'id': "ID"},"hashContexts":{'data-slider-value': depth0,'data-slider-step': depth0,'data-slider-min': depth0,'type': depth0,'data-slider-id': depth0,'class': depth0,'id': depth0},"types":[],"contexts":[],"data":data}))));
  data.buffer.push("   \r\n        </div>\r\n    </div>\r\n</div>");
  return buffer;
},"useData":true});