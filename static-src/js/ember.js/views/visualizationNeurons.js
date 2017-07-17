App.VisualizationNeuronsView = Ember.View.extend({
    classNames:["col-sm-4", "wrap", "color", "scrolly"],
    
  didInsertElement: function() {
	/*var forceSlider = new Slider('#ex1', {
		formatter: function(value) {
			return 'Current value: ' + value;
		}
	});
	var lengthSlider = new Slider('#ex2', {
		formatter: function(value) {
			return 'Current value: ' + value;
		}
	});
	var angleSlider = new Slider('#ex3', {
		formatter: function(value) {
			return 'Current value: ' + value;
		}
	});*/
      
      var parent = this;
      
      $('.btn-turquesa3').on('click',function(event){
          if(event.ctrlKey){
              parent.get('controller').send('changeMenu',event.currentTarget.id);
          }
          else{
              parent.get('controller').send('focusNeuron',event.currentTarget.id);
          }
          //active not needed
            var DOMparent   = event.currentTarget.parentNode,
                position = event.currentTarget.nextSibling;
            DOMparent.removeChild(event.currentTarget);
            // Using insertBefore instead of appendChild so that it is put at the right position among the siblings
            DOMparent.insertBefore(event.currentTarget, position);
      });
      $('.btn-naranja').on('click',function(event){
          if(event.ctrlKey){
              parent.get('controller').send('changeMenu',event.currentTarget.id);
          }
          else{
              parent.get('controller').send('focusNeuron',event.currentTarget.id);
          }
          //active not needed
            var DOMparent   = event.currentTarget.parentNode,
                position = event.currentTarget.nextSibling;
            DOMparent.removeChild(event.currentTarget);
            // Using insertBefore instead of appendChild so that it is put at the right position among the siblings
            DOMparent.insertBefore(event.currentTarget, position);
      });
  },
  actions:{
  }           



});