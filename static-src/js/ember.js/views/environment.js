App.EnvironmentView = Ember.View.extend({
    classNames:["wrap"],
  didInsertElement: function() {
	var self = this;
			var temp = this.get('controller.model.envTemp');
			var environmentTempSlider = new Slider('#environmentTempSlider', {
					range : false,
					max : new Number(50),
					step : 0.1,
					value : temp,
					formatter : function (value) {
						var myModel = self.get('controller.model');
						if (myModel) {
							myModel.set('envTemp', value);
						}
						return value + ' ºC';
					},
					id : 'enviroment-temp-slider',
				});
  
  },
  /*willInsertElement:function(){
      this.get('controller.model.wormStatus').then(function(data){
         data.get('wormInitialPosition.orientation');
      });
  },   */     
            
});