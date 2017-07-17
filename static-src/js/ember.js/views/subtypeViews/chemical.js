App.ChemicalView = Ember.View.extend({
		didInsertElement : function () {
			var self = this;
			$('.chemicalNone').click(function () {
				if(self.elementId == event.currentTarget.parentNode.parentNode.parentNode.parentNode.id){
					self.set('controller.model.chemical_name', 'None');
				}
			});
			$('.chemicalBiotin').click(function (event) {
				if(self.elementId == event.currentTarget.parentNode.parentNode.parentNode.parentNode.id){
					self.set('controller.model.chemical_name', 'biotin');
				}
			});
			$('.chemicalNaCl').click(function () {
				if(self.elementId == event.currentTarget.parentNode.parentNode.parentNode.parentNode.id){
					self.set('controller.model.chemical_name', 'NaCl');
				}
			});
			$('.chemicalEthanol').click(function () {
				if(self.elementId == event.currentTarget.parentNode.parentNode.parentNode.parentNode.id){
					self.set('controller.model.chemical_name', 'ethanol');
				}
			});
			$('.chemicalButanone').click(function () {
				if(self.elementId == event.currentTarget.parentNode.parentNode.parentNode.parentNode.id){
					self.set('controller.model.chemical_name', 'butanone');
				}
			});
			$('.chemicalBenzaldehyde').click(function () {
				if(self.elementId == event.currentTarget.parentNode.parentNode.parentNode.parentNode.id){
					self.set('controller.model.chemical_name', 'benzaldehyde');
				}
			});
			$('.chemicalCuSO4').click(function () {
				if(self.elementId == event.currentTarget.parentNode.parentNode.parentNode.parentNode.id){
					self.set('controller.model.chemical_name', 'CuSO4');
				}
			});
			$('.chemicalDiacetyl').click(function () {
				if(self.elementId == event.currentTarget.parentNode.parentNode.parentNode.parentNode.id){
					self.set('controller.model.chemical_name', 'diacetyl');
				}
			});
			$('.chemicalDodecyl').click(function () {
				if(self.elementId == event.currentTarget.parentNode.parentNode.parentNode.parentNode.id){
					self.set('controller.model.chemical_name', 'SDS - Sodium dodecyl sulfate');
				}
			});
			$('.chemicalQuinine').click(function () {
				if(self.elementId == event.currentTarget.parentNode.parentNode.parentNode.parentNode.id){
					self.set('controller.model.chemical_name', 'quinine');
				}
			});
			$('.chemicalNaN3').click(function () {
				if(self.elementId == event.currentTarget.parentNode.parentNode.parentNode.parentNode.id){
					self.set('controller.model.chemical_name', 'NaN3');
				}
			});
		},
		templateName : "chemical",
	});