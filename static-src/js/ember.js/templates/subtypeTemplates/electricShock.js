Ember.TEMPLATES["electricShock"] = Ember.Handlebars.template({"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = '';
  data.buffer.push("<div class=\"row\">\r\n	<div class=\"col-sm-12\">\r\n		<div class=\" title\">Shock Duration</div>\r\n	</div>\r\n</div>\r\n<div class=\"row\">\r\n	<div class=\"col-sm-12 block\">\r\n		<div>\r\n			");
  data.buffer.push(escapeExpression(((helpers.input || (depth0 && depth0.input) || helperMissing).call(depth0, {"name":"input","hash":{
    'data-slider-value': ("eventTime"),
    'data-slider-step': ("0.1"),
    'data-slider-min': ("0"),
    'type': ("text"),
    'data-slider-id': ("shockDurationSlider"),
    'class': ("simpleSlider"),
    'id': ("shockDurationSlider")
  },"hashTypes":{'data-slider-value': "ID",'data-slider-step': "STRING",'data-slider-min': "STRING",'type': "STRING",'data-slider-id': "STRING",'class': "STRING",'id': "STRING"},"hashContexts":{'data-slider-value': depth0,'data-slider-step': depth0,'data-slider-min': depth0,'type': depth0,'data-slider-id': depth0,'class': depth0,'id': depth0},"types":[],"contexts":[],"data":data}))));
  data.buffer.push("\r\n		</div>\r\n	</div>\r\n</div>\r\n<div class=\"row\">\r\n	<div class=\"col-sm-12\">\r\n		<div class=\" title\">Shock Frequency</div>\r\n	</div>\r\n</div>\r\n<div class=\"row\">\r\n	<div class=\"col-sm-12 block\">\r\n		<div>\r\n			");
  data.buffer.push(escapeExpression(((helpers.input || (depth0 && depth0.input) || helperMissing).call(depth0, {"name":"input","hash":{
    'data-slider-value': ("eventTime"),
    'data-slider-step': ("0.1"),
    'data-slider-min': ("0"),
    'type': ("text"),
    'data-slider-id': ("shockFrequencySlider"),
    'class': ("simpleSlider"),
    'id': ("shockFrequencySlider")
  },"hashTypes":{'data-slider-value': "ID",'data-slider-step': "STRING",'data-slider-min': "STRING",'type': "STRING",'data-slider-id': "STRING",'class': "STRING",'id': "STRING"},"hashContexts":{'data-slider-value': depth0,'data-slider-step': depth0,'data-slider-min': depth0,'type': depth0,'data-slider-id': depth0,'class': depth0,'id': depth0},"types":[],"contexts":[],"data":data}))));
  data.buffer.push("\r\n		</div>\r\n	</div>\r\n</div>\r\n<div class=\"row\">\r\n	<div class=\"col-sm-12\">\r\n		<div class=\" title\">Amplitude</div>\r\n	</div>\r\n</div>\r\n<div class=\"row\">\r\n	<div class=\"col-sm-12 block\">\r\n		<div>\r\n			");
  data.buffer.push(escapeExpression(((helpers.input || (depth0 && depth0.input) || helperMissing).call(depth0, {"name":"input","hash":{
    'data-slider-value': ("eventTime"),
    'data-slider-step': ("0.1"),
    'data-slider-min': ("0"),
    'type': ("text"),
    'data-slider-id': ("shockAmplitudeSlider"),
    'class': ("simpleSlider"),
    'id': ("shockAmplitudeSlider")
  },"hashTypes":{'data-slider-value': "ID",'data-slider-step': "STRING",'data-slider-min': "STRING",'type': "STRING",'data-slider-id': "STRING",'class': "STRING",'id': "STRING"},"hashContexts":{'data-slider-value': depth0,'data-slider-step': depth0,'data-slider-min': depth0,'type': depth0,'data-slider-id': depth0,'class': depth0,'id': depth0},"types":[],"contexts":[],"data":data}))));
  data.buffer.push("\r\n		</div>\r\n	</div>\r\n</div>");
  return buffer;
},"useData":true});