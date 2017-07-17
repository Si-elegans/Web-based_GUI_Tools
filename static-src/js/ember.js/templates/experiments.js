Ember.TEMPLATES["experiments"] = Ember.Handlebars.template({"1":function(depth0,helpers,partials,data) {
  var stack1, helperMissing=helpers.helperMissing, buffer = '';
  data.buffer.push("		<li>");
  stack1 = ((helpers['link-to'] || (depth0 && depth0['link-to']) || helperMissing).call(depth0, "experiment", "experiment", {"name":"link-to","hash":{
    'class': ("whitefont")
  },"hashTypes":{'class': "STRING"},"hashContexts":{'class': depth0},"fn":this.program(2, data),"inverse":this.noop,"types":["STRING","ID"],"contexts":[depth0,depth0],"data":data}));
  if (stack1 != null) { data.buffer.push(stack1); }
  data.buffer.push("</li>\r\n");
  return buffer;
},"2":function(depth0,helpers,partials,data) {
  var stack1;
  stack1 = helpers._triageMustache.call(depth0, "experiment.about", {"name":"_triageMustache","hash":{},"hashTypes":{},"hashContexts":{},"types":["ID"],"contexts":[depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  else { data.buffer.push(''); }
  },"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, buffer = '';
  data.buffer.push("<div class=\"col-sm-12\">\r\n	<div class=\"row\">\r\n		<div class=\"col-sm-12\">\r\n			<div class=\" title\">My Experiments</div>\r\n		</div>\r\n	</div>\r\n	<ul>\r\n");
  stack1 = helpers.each.call(depth0, "experiment", "in", "model.content", {"name":"each","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(1, data),"inverse":this.noop,"types":["ID","ID","ID"],"contexts":[depth0,depth0,depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  data.buffer.push("	</ul>\r\n	<div class=\"row\">\r\n		<div class=\"col-sm-12\">\r\n			<div class=\" title\">Experiments Shared With Me</div>\r\n		</div>\r\n	</div>\r\n	<ul>\r\n");
  stack1 = helpers.each.call(depth0, "experiment", "in", "model.content", {"name":"each","hash":{},"hashTypes":{},"hashContexts":{},"fn":this.program(1, data),"inverse":this.noop,"types":["ID","ID","ID"],"contexts":[depth0,depth0,depth0],"data":data});
  if (stack1 != null) { data.buffer.push(stack1); }
  data.buffer.push("	</ul>\r\n</div>");
  return buffer;
},"useData":true});