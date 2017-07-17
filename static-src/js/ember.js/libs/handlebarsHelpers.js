Ember.Handlebars.helper('collapse1', function (object) {

	var url = Handlebars.escapeExpression(object.url),
	text = Handlebars.escapeExpression(object.text);

	return new Ember.Handlebars.SafeString("<div class=\"title\" role=\"tab\" id=\"headingOne\">"
		 + "<a class=\"title\" id=\"neuronTitles\" data-toggle=\"collapse\" data-parent=\"#accordion\" href=\"#collapse" + object + "\" aria-expanded=\"true\" aria-controls=collapse" + object + "\">"
		 + object +
		"</a>"
		 + "</div>");
});
Ember.Handlebars.helper('collapse2', function (object) {
	var url = Handlebars.escapeExpression(object.url),
	text = Handlebars.escapeExpression(object.text);

	return new Ember.Handlebars.SafeString("<div id=\"collapse" + object.name + "\" class=\"panel-collapse collapse\" role=\"tabpanel\" aria-labelledby=\"headingOne\">"
		 + "<div class=\"\">"
		 + "<div class=\"row\">"
		 + "<div class=\"col-sm-12 block\">"
		 + "<div class=\"whitefont\">Time: 0 s</div>"
		 + "<div class=\"whitefont\">Neuron model: " + object.model + "</div>"
		 + "<div class=\"whitefont\">Current voltage: " + object.voltage + "</div>"
		 + "<div class=\"whitefont\">Spike- rate: " + object.rate + "</div>"
		 + "</div>"
		 + "</div>"
		 + "</div>" +
		"</div>");
});
Ember.Handlebars.helper('buttonName', function (object) {

	var url = Handlebars.escapeExpression(object.url),
	text = Handlebars.escapeExpression(object.text);

	return new Ember.Handlebars.SafeString("<button class=\"btn btn-turquesa3 boton-neurona\" id=\"button" + object + "\">" + object + "</button>");
});
Ember.Handlebars.helper('voltageName', function (object) {

	var url = Handlebars.escapeExpression(object.url),
	text = Handlebars.escapeExpression(object.text);

	return new Ember.Handlebars.SafeString("<div class=\"graph\" id=\"voltage" + object + "\"></div>");
});
Ember.Handlebars.helper('divName', function (object) {

	var url = Handlebars.escapeExpression(object.url),
	text = Handlebars.escapeExpression(object.text);

	return new Ember.Handlebars.SafeString("<div class=\"static-button div-turquesa4 boton-neurona\" id=\"div" + object + "\">" + object + "</div>");
});

Ember.Handlebars.registerHelper('compare', function (lvalue, rvalue, options) {
	if (arguments.length < 3)
		throw new Error("Handlerbars Helper 'compare' needs 2 parameters");

	var operator = options.hash.operator || "==";

	var operators = {
		'==' : function (l, r) {
			return l == r;
		},
		'===' : function (l, r) {
			return l === r;
		},
		'!=' : function (l, r) {
			return l != r;
		},
		'<' : function (l, r) {
			return l < r;
		},
		'>' : function (l, r) {
			return l > r;
		},
		'<=' : function (l, r) {
			return l <= r;
		},
		'>=' : function (l, r) {
			return l >= r;
		},
		'typeof' : function (l, r) {
			return typeof l == r;
		}
	}

	if (!operators[operator])
		throw new Error("Handlerbars Helper 'compare' doesn't know the operator " + operator);
	var result = operators[operator](this.get(lvalue), rvalue);
	if (result) {
		return options.fn(this);
	} else {
		return options.inverse(this);
	}

});
Ember.Handlebars.registerHelper('compareWithModel', function (lvalue, rvalue, options) {
	if (arguments.length < 3)
		throw new Error("Handlerbars Helper 'compare' needs 2 parameters");
	var myself = this;
	console.log(this);
	this.get('model').then(function (item) {
		var operator = options.hash.operator || "==";
		
		var operators = {
			'==' : function (l, r) {
				return l == r;
			},
			'===' : function (l, r) {
				return l === r;
			},
			'!=' : function (l, r) {
				return l != r;
			},
			'<' : function (l, r) {
				return l < r;
			},
			'>' : function (l, r) {
				return l > r;
			},
			'<=' : function (l, r) {
				return l <= r;
			},
			'>=' : function (l, r) {
				return l >= r;
			},
			'typeof' : function (l, r) {
				return typeof l == r;
			}
		}

		if (!operators[operator])
			throw new Error("Handlerbars Helper 'compare' doesn't know the operator " + operator);
		var result = operators[operator](item.get(lvalue), rvalue);
		if (result) {
			return options.fn(myself);
		} else {
			return options.inverse(myself);
		}
	});

});

Ember.Handlebars.helper('obstacleAngle', function (id, anglevalue) {
	if(id && anglevalue){
		return new Ember.Handlebars.SafeString('<input id="obstacleAngleSlider' + id + '" class="simpleSlider" data-slider-id="obstacleAngleSlider' + id + '" type="text" data-slider-min="0" data-slider-step="0.1" data-slider-value=anglevalue />');
	}
	else{
		return '';
	}
	
});

Ember.Handlebars.helper('obstacleXDistance', function (id,xvalue) {
	if(id && xvalue){
		return new Ember.Handlebars.SafeString('<input id="obstacleDistanceXSlider' + id + '" class="simpleSlider" data-slider-id="obstacleDistanceXSlider' + id + '" type="text" data-slider-min="0" data-slider-step="0.1" data-slider-value=xvalue />');
	}
	else{
		return '';
	}
});

Ember.Handlebars.helper('obstacleYDistance', function (id,yvalue) {
	if(id && yvalue){
		return new Ember.Handlebars.SafeString('<input id="obstacleDistanceYSlider' + id + '" class="simpleSlider" data-slider-id="obstacleDistanceYSlider' + id + '" type="text" data-slider-min="0" data-slider-step="0.1" data-slider-value=yvalue />');
	}
	else{
		return '';
	}
});
