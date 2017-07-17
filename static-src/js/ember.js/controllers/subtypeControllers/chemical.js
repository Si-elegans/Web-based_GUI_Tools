App.ChemicalController = Ember.ObjectController.extend({
	needs: [],
	typeName: function(){
		if(this.get('model.chemical_name')=="None"){
			return 'None';
		}
		else if(this.get('model.chemical_name')=="biotin"){
			return 'Biotin';
		}
		else if(this.get('model.chemical_name')=="NaCl"){
			return 'NaCl';
		}
		else if(this.get('model.chemical_name')=="ethanol"){
			return 'ethanol';
		}
		else if(this.get('model.chemical_name')=="butanone"){
			return 'butanone';
		}
		else if(this.get('model.chemical_name')=="CuSO4"){
			return 'CuSO4';
		}
		else if(this.get('model.chemical_name')=="SDS - Sodium dodecyl sulfate"){
			return 'Sodium dodecyl sulfate';
		}
		else if(this.get('model.chemical_name')=="benzaldehyde"){
			return 'benzaldehyde';
		}
		else if(this.get('model.chemical_name')=="diacetyl"){
			return 'diacetyl';
		}
		else if(this.get('model.chemical_name')=="NaN3"){
			return 'NaN3';
		}
		else if(this.get('model.chemical_name')=="quinine"){
			return 'Quinine';
		}
		else{
			return 'error';
		}
    }.property('model.chemical_name'),
});
