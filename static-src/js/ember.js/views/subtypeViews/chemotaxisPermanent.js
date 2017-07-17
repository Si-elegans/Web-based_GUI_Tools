App.ChemotaxisPermanentView = Ember.View.extend({
		//classNames:["col-sm-4", "wrap", "color", "scrolly"],
		didInsertElement : function () {
			var self = this;
			var store = this.get('controller.store');
			$('#chemoOsmotic').click(function(){
				if(self.get('controller.model.osmoticRing.content')){
					self.set('controller.model.chemicalCategory','OR');
				}
				else{
					var aux2 = store.createRecord("chemical",{
						chemical_name: "biotin",
						isVolatile: true,
						volatilitySpeed: 0,
						diffusionCoefficient: 0,
					});
					aux2.save().then(function(item){
						var aux = store.createRecord("osmoticRing", {
							chemicalConcentration: 0,
							internalRadius: 1,
							externalRadius: 2,
							ringChemical: item,
						});
						aux.save().then(function(item2){
							var osmoticItems = store.all('osmoticRing');
							if (self.get('controllers.osmoticRing.osmoticConcentrationSlider')) {
								for (var i = 0; i < osmoticItems.content.length; i++) {
									osmoticItems.content[i].set('osmoticConcentrationSlider', self.get('controllers.osmoticRing.osmoticConcentrationSlider'));
								}
							}
							if (self.get('controllers.osmoticRing.osmoticInternalSlider')) {
								for (var i = 0; i < osmoticItems.content.length; i++) {
									osmoticItems.content[i].set('osmoticInternalSlider', self.get('controllers.osmoticRing.osmoticInternalSlider'));
								}
							}
							if (self.get('controllers.osmoticRing.osmoticExternalSlider')) {
								for (var i = 0; i < osmoticItems.content.length; i++) {
									osmoticItems.content[i].set('osmoticExternalSlider', self.get('controllers.osmoticRing.osmoticExternalSlider'));
								}
							}
							self.set('controller.model.osmoticRing',item2);
							self.set('controller.model.chemicalCategory','OR');
						});
					});
				}
			});
			$('#chemoQuadrants1').click(function(){
				if(self.get('controller.model.chemotaxisQuadrants1.content')){
					self.set('controller.model.chemicalCategory','CQ1');
				}
				else{
					var aux2 = store.createRecord("chemical",{
						chemical_name: "biotin",
						isVolatile: true,
						volatilitySpeed: 0,
						diffusionCoefficient: 0,
					});
					aux2.save().then(function(item){
						var aux = store.createRecord("chemotaxisQuadrants1", {
							quadrantChemicalConcentration: 0,
							quadrantChemical: item,
						});
						aux.save().then(function(item2){
							var quadrants1Items = store.all('chemotaxisQuadrants1');
							if (self.get('controllers.chemotaxisQuadrants1.quad1ConcentrationSlider')) {
								for (var i = 0; i < quadrants1Items.content.length; i++) {
									quadrants1Items.content[i].set('quad1ConcentrationSlider', self.get('controllers.chemotaxisQuadrants1.quad1ConcentrationSlider'));
								}
							}
							self.set('controller.model.chemotaxisQuadrants1',item2);
							self.set('controller.model.chemicalCategory','CQ1');
						});
					});
				}
			});
			$('#chemoQuadrants2').click(function(){
				if(self.get('controller.model.chemotaxisQuadrants2.content')){
					self.set('controller.model.chemicalCategory','CQ2');
				}
				else{
					var aux2 = store.createRecord("chemical",{
						chemical_name: "biotin",
						isVolatile: true,
						volatilitySpeed: 0,
						diffusionCoefficient: 0,
					});
					aux2.save().then(function(item){
						var aux3 = store.createRecord("chemical",{
							chemical_name: "biotin",
							isVolatile: true,
							volatilitySpeed: 0,
							diffusionCoefficient: 0,
						});
						aux3.save().then(function(item2){
							var aux4 = store.createRecord("chemical",{
								chemical_name: "biotin",
								isVolatile: true,
								volatilitySpeed: 0,
								diffusionCoefficient: 0,
							});
							aux4.save().then(function(item3){
								var aux = store.createRecord("chemotaxisQuadrants2", {
									quadrant_1_ChemicalConcentration: 0,
									quadrant_2_ChemicalConcentration: 0,
									quadrant_1_Chemical: item,
									quadrant_2_Chemical: item2,
									quadrantBarrierChemicalConcentration: 0,
									quadrantBarrierChemical: item3,
								});
								aux.save().then(function(item4){
									var quadrants2Items = store.all('chemotaxisQuadrants2');
									if (self.get('controllers.chemotaxisQuadrants2.quad2ConcentrationSlider1')) {
										for (var i = 0; i < quadrants2Items.content.length; i++) {
											quadrants2Items.content[i].set('quad2ConcentrationSlider1', self.get('controllers.chemotaxisQuadrants2.quad2ConcentrationSlider1'));
										}
									}
									if (self.get('controllers.chemotaxisQuadrants2.quad2ConcentrationSlider2')) {
										for (var i = 0; i < quadrants2Items.content.length; i++) {
											quadrants2Items.content[i].set('quad2ConcentrationSlider2', self.get('controllers.chemotaxisQuadrants2.quad2ConcentrationSlider2'));
										}
									}
									if (self.get('controllers.chemotaxisQuadrants2.quad2BarrierConcentrationSlider')) {
										for (var i = 0; i < quadrants2Items.content.length; i++) {
											quadrants2Items.content[i].set('quad2BarrierConcentrationSlider', self.get('controllers.chemotaxisQuadrants2.quad2BarrierConcentrationSlider'));
										}
									}
									self.set('controller.model.chemotaxisQuadrants2',item4);
									self.set('controller.model.chemicalCategory','CQ2');
								});
							});
						});
					});
				}
			});
			$('#staticPointSource').click(function(){
				if(self.get('controller.model.staticPointSource.content')){
					self.set('controller.model.chemicalCategory','SPS');
				}
				else{
					var aux2 = store.createRecord("chemical",{
						chemical_name: "biotin",
						isVolatile: true,
						volatilitySpeed: 0,
						diffusionCoefficient: 0,
					});
					aux2.save().then(function(item){
						var aux = store.createRecord("staticPointSource", {
							dropQuantity: 0,
							chemicalConcentration: 0,
							xCoordFromPlateCentre: 0,
							yCoordFromPlateCentre: 0,
							chemical: item,
						});
						aux.save().then(function(item4){
							var staticPointItems = store.all('staticPointSource');
							if (self.get('controllers.staticPointSource.spsConcentrationSlider')) {
								for (var i = 0; i < staticPointItems.content.length; i++) {
									staticPointItems.content[i].set('spsConcentrationSlider', self.get('controllers.staticPointSource.spsConcentrationSlider'));
								}
							}
							if (self.get('controllers.staticPointSource.spsDropSlider')) {
								for (var i = 0; i < staticPointItems.content.length; i++) {
									staticPointItems.content[i].set('spsDropSlider', self.get('controllers.staticPointSource.spsDropSlider'));
								}
							}
							if (self.get('controllers.staticPointSource.spsXaxisSlider')) {
								for (var i = 0; i < staticPointItems.content.length; i++) {
									staticPointItems.content[i].set('spsXaxisSlider', self.get('controllers.staticPointSource.spsXaxisSlider'));
								}
							}
							if (self.get('controllers.staticPointSource.spsYaxisSlider')) {
								for (var i = 0; i < staticPointItems.content.length; i++) {
									staticPointItems.content[i].set('spsYaxisSlider', self.get('controllers.staticPointSource.spsYaxisSlider'));
								}
							}
							self.set('controller.model.staticPointSourceConf',item4);
							self.set('controller.model.chemicalCategory','SPS');
						});
					});
				}
			});
			$('#chemoQuadrants4').click(function(){
				if(self.get('controller.model.chemotaxisQuadrants4.content')){
					self.set('controller.model.chemicalCategory','CQ4');
				}
				else{
					var aux2 = store.createRecord("chemical",{
						chemical_name: "biotin",
						isVolatile: true,
						volatilitySpeed: 0,
						diffusionCoefficient: 0,
					});
					aux2.save().then(function(item){
						var aux3 = store.createRecord("chemical",{
							chemical_name: "biotin",
							isVolatile: true,
							volatilitySpeed: 0,
							diffusionCoefficient: 0,
						});
						aux3.save().then(function(item2){
							var aux4 = store.createRecord("chemical",{
								chemical_name: "biotin",
								isVolatile: true,
								volatilitySpeed: 0,
								diffusionCoefficient: 0,
							});
							aux4.save().then(function(item3){
								var aux5 = store.createRecord("chemical",{
									chemical_name: "biotin",
									isVolatile: true,
									volatilitySpeed: 0,
									diffusionCoefficient: 0,
								});
								aux5.save().then(function(item4){
									var aux6 = store.createRecord("chemical",{
										chemical_name: "biotin",
										isVolatile: true,
										volatilitySpeed: 0,
										diffusionCoefficient: 0,
									});
									aux6.save().then(function(item5){
										var aux = store.createRecord("chemotaxisQuadrants4", {
											quadrant_1_ChemicalConcentration: 0,
											quadrant_2_ChemicalConcentration: 0,
											quadrant_3_ChemicalConcentration: 0,
											quadrant_4_ChemicalConcentration: 0,
											quadrant_1_Chemical: item,
											quadrant_2_Chemical: item2,
											quadrant_3_Chemical: item3,
											quadrant_4_Chemical: item4,
											quadrantBarrierChemicalConcentration: 0,
											quadrantBarrierChemical: item5,
										});
										aux.save().then(function(item6){
											var quadrants4Items = store.all('chemotaxisQuadrants4');
											if (self.get('controllers.chemotaxisQuadrants4.quad4ConcentrationSlider1')) {
												for (var i = 0; i < quadrants4Items.content.length; i++) {
													quadrants4Items.content[i].set('quad4ConcentrationSlider1', self.get('controllers.chemotaxisQuadrants4.quad4ConcentrationSlider1'));
												}
											}
											if (self.get('controllers.chemotaxisQuadrants4.quad4ConcentrationSlider2')) {
												for (var i = 0; i < quadrants4Items.content.length; i++) {
													quadrants4Items.content[i].set('quad4ConcentrationSlider2', self.get('controllers.chemotaxisQuadrants4.quad4ConcentrationSlider2'));
												}
											}
											if (self.get('controllers.chemotaxisQuadrants4.quad4ConcentrationSlider3')) {
												for (var i = 0; i < quadrants4Items.content.length; i++) {
													quadrants4Items.content[i].set('quad4ConcentrationSlider3', self.get('controllers.chemotaxisQuadrants4.quad4ConcentrationSlider3'));
												}
											}
											if (self.get('controllers.chemotaxisQuadrants4.quad4ConcentrationSlider4')) {
												for (var i = 0; i < quadrants4Items.content.length; i++) {
													quadrants4Items.content[i].set('quad4ConcentrationSlider4', self.get('controllers.chemotaxisQuadrants4.quad4ConcentrationSlider4'));
												}
											}
											if (self.get('controllers.chemotaxisQuadrants4.quad4BarrierConcentrationSlider')) {
												for (var i = 0; i < quadrants4Items.content.length; i++) {
													quadrants4Items.content[i].set('quad4BarrierConcentrationSlider', self.get('controllers.chemotaxisQuadrants4.quad4BarrierConcentrationSlider'));
												}
											}
											self.set('controller.model.chemotaxisQuadrants4',item6);
											self.set('controller.model.chemicalCategory','CQ4');
										});
									});
								});
							});
						});
					});
				}
			});
		},
		templateName: 'chemotaxisPermanent',
	});