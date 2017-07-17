App.DefinitionController = Ember.ObjectController.extend({
		needs : ["experiment", "exact", "interval", "permanent", "directTouch", "plateTap", "pointSourceLight", 'chemotaxisQuadrants1', 'chemotaxisQuadrants2', 'chemotaxisQuadrants4', 'osmoticRing', 'staticPointSource', 'dynamicDropTest', 'pointSourceHeatAvoidance', 'linearThermalGradient', 'electricShock', 'temperatureChangeInTime'],
		isModifiable : true,

		updateDuration : function () {
			var timeline = this.get('timeline'); //reset seconds, before setting milliseconds
			if (timeline) {
				timeline.options.end = new Number(this.get('model.experimentDuration'));
				timeline.range.end = this.get('model.experimentDuration');
				timeline.redraw();
			}
			
			var slider = this.get("controllers.exact.exactTimeSlider");
			if(slider){
				slider.setAttribute("max",this.get('model.experimentDuration'));
				slider.refresh();
			}
			
			var slider2 = this.get("controllers.interval.intervalTimeSlider");
			if(slider2){
				slider2.setAttribute("max",this.get('model.experimentDuration'));
				slider2.refresh();
			}
		}
		.observes('model.experimentDuration'),

		actions : {
			gotoEnvironment : function () {
				this.set("selectedBox", null);
				var timeline = this.get('timeline'); //reset seconds, before setting milliseconds
				if (timeline) {
					timeline.itemSet.setSelection("");
					timeline.redraw();
				}
				this.transitionToRoute('environment');
			},
			addEvent : function (eventName) {
				this.get('model').events.push({});
			},
			changeToEvent : function (source) {
				if (this.controllerFor('application').get('currentRouteName') == 'environment') {
					//we remove "inter", "perma" or "exact" to the id
					var self = this;
					this.transitionToRoute('experiment').then(function () {
						self.transitionToRoute('definition').then(function () {
							self.transitionToRoute(source.eventType, source.id.slice(5, source.id.length));
						});
					});
				} else {
					var self = this;
					self.transitionToRoute(source.eventType, source.id.slice(5, source.id.length));
				}
				/*router.transitionTo('definition');
				router.transitionTo();*/
				/*if (source.eventType == "exact") {
				var view = App.__container__.lookup("view:exact");
				view.rerender();
				}
				if (source.eventType == "interval") {
				var view = App.__container__.lookup("view:interval");
				view.rerender();
				}
				if (source.eventType == "permanent") {
				var view = App.__container__.lookup("view:permanent");
				view.rerender();
				}*/
			},
			updateTimelineBoxTime : function (a, b) {
				var timeline = this.get('timeline'); //reset seconds, before setting milliseconds
				if (timeline) {
					timeline.itemSet.items[a].data.start = b;
					timeline.itemsData._data[a].start = b;
					timeline.redraw();
				}
			},
			updateTimelineBoxName : function (a, b) {
				var timeline = this.get('timeline'); //reset seconds, before setting milliseconds
				if (timeline) {
					if (timeline.itemSet.items[a]) {
						timeline.itemSet.items[a].data.content = b;
						timeline.itemsData._data[a].content = b;
					} else {}
					timeline.redraw();
				}
			},
			updateTimelineBoxStart : function (a, b) { ;
				var timeline = this.get('timeline'); //reset seconds, before setting milliseconds
				if (timeline) {
					timeline.itemSet.items[a].data.start = b;
					timeline.itemsData._data[a].start = b;
					timeline.redraw();
				}
			},
			updateTimelineBoxStop : function (a, b) {
				var timeline = this.get('timeline'); //reset seconds, before setting milliseconds
				if (timeline) {
					timeline.itemSet.items[a].data.end = b;
					timeline.itemsData._data[a].end = b;
					timeline.redraw();
				}
			},
			deleteBox : function (index) {
				var timeline = this.get('timeline'); //reset seconds, before setting milliseconds
				if (timeline) {
					timeline.itemSet.removeItem(index);
					timeline.redraw();
				}
			},

			addExactBox : function (id, start, content, type) {
				var timeline = this.get('timeline'); //reset seconds, before setting milliseconds
				timeline.itemsData._data[id] = {
					'id' : id,
					'start' : new Number(0),
					'content' : new String(content),
					'eventType' : 'exact',
					'eventSubType' : new String(type),
				};
				timeline.setItems(timeline.itemsData);
				timeline.redraw();
			},

			addIntervalBox : function (id, start, stop, content, type) {
				var timeline = this.get('timeline'); //reset seconds, before setting milliseconds
				timeline.itemsData._data[id] = {
					'id' : id,
					'start' : new Number(start),
					'end' : new Number(stop),
					'content' : new String(content),
					'eventType' : 'interval',
					'eventSubType' : new String(type),
				};
				timeline.setItems(timeline.itemsData);
				timeline.redraw();
			},

			addPermanentBox : function (id, content, type) {
				var timeline = this.get('timeline'); //reset seconds, before setting milliseconds
				timeline.itemsData._data[id] = {
					'id' : id,
					'start' : -1000000000000000,
					'end' : 1000000000000000,
					'content' : new String(content),
					'eventType' : 'permanent',
					'eventSubType' : new String(type),
				};
				timeline.setItems(timeline.itemsData);
				timeline.redraw();
			},

			setSelectedBox : function (id) {
				this.set('selectedBox', id);
				var timeline = this.get('timeline'); //reset seconds, before setting milliseconds
				if (timeline) {
					timeline.itemSet.setSelection(id);
					timeline.redraw();
				}
			},
			saveExperiment : function () {
				var experimentController = this.get('controllers.experiment');
				experimentController.saveChanges();
			},
			createEvent : function () {
				$('#modalCreating').modal('show');
				var e = document.getElementById("createDuration");
				var strDuration = e.options[e.selectedIndex].text;
				e = document.getElementById("createType");
				var strType = e.options[e.selectedIndex].text;
				var strName = document.getElementById("createName").value;
				var store = this.store;
				var self = this;

				if (strDuration == "Exact") {
					if (strType == "Mechanosensation") {
						/*store.find('mechanosensationExact').then(function (array) {
						var num = 0;
						if (array.content.length > 1) {
						for (var i = 0; i < array.content.length; i++) {
						if (parseFloat(array.content[i].get('id')) > num) {
						num = parseFloat(array.content[i].get('id'));
						}
						}
						} else {
						num = array.content.get('id');
						}
						num++;*/
						var aux3 = store.createRecord("plateTap", {
								appliedForce : 0,
							});
						aux3.save().then(function (item3) {
							var plateItems = store.all('plateTap');
							if (self.get('controllers.plateTap.plateForceSlider')) {
								for (var i = 0; i < plateItems.content.length; i++) {
									plateItems.content[i].set('plateForceSlider', self.get('controllers.plateTap.plateForceSlider'));
								}
							}
							var aux4 = store.createRecord("directTouch", {
									"directTouchInstrument" : "EB",
									"touchDistance" : 0.0,
									"touchAngle" : 1.0,
									"appliedForce" : 1.0,
								});
							aux4.save().then(function (item4) {
								var directItems = store.all('directTouch');
								if (self.get('controllers.directTouch.touchForceSlider')) {
									for (var i = 0; i < directItems.content.length; i++) {
										directItems.content[i].set('touchForceSlider', self.get('controllers.directTouch.touchForceSlider'));
										directItems.content[i].set('touchLocationLengthSlider', self.get('controllers.directTouch.touchLocationLengthSlider'));
										directItems.content[i].set('touchLocationAngleSlider', self.get('controllers.directTouch.touchLocationAngleSlider'));
									}
								}
								var aux2 = store.createRecord("mechanosensationExact", {
										description : "new mechano exact " /* + num*/
									,
										interactionType : "DWT",
										directTouch : item4,
										plateTap : item3,
									});
								aux2.save().then(function (item) {
									var aux5 = store.createRecord("interactionAtSpecificTime", {
											//"name" : strName,
											"description" : strName,
											"eventTime" : 0,
											"experimentCategory" : "MS",
											"chemotaxis" : null,
											"termotaxis" : null,
											"galvanotaxis" : null,
											"phototaxis" : null,
											"mechanosensation" : item,
										});
									aux5.save().then(function (item2) {
										var experimentModel = self.get('model');
										var exactEvents = experimentModel.get('interactionAtSpecificTime');
										console.log(exactEvents.content);
										exactEvents.pushObject(aux5);
										console.log(exactEvents.content);
										//set to be saved
										var controller = App.__container__.lookup("controller:experiment");
										var items = experimentModel.get('interactionAtSpecificTime.content.currentState');
										if (self.get('controllers.exact.exactTimeSlider')) {
											for (var i = 0; i < items.length; i++) {
												items[i].set('exactTimeSlider', self.get('controllers.exact.exactTimeSlider'));
											}
										}
										var proxySend = jQuery.proxy(controller.send, controller);
										proxySend('savingModelDidUpdate', experimentModel);

										self.send('addExactBox', "exact" + item2.get('id'), 0, strName, 'MS');
										self.send('setSelectedBox', "exact" + item2.get('id'));
										self.transitionToRoute('exact', item2.get('id'));
										document.getElementById("createName").value = "";
										$('#modalCreating').modal('hide');
									});
								});
								//});
							});
						});
					} else if (strType == "Galvanotaxis") {}
					else if (strType == "Chemotaxis") {
						/*store.find('chemotaxisExact').then(function (array) {
						var num = 0;
						if (array.content.length > 1) {
						for (var i = 0; i < array.content.length; i++) {
						if (parseFloat(array.content[i].get('id')) > num) {
						num = parseFloat(array.content[i].get('id'));
						}
						}
						} else {
						num = array.content.get('id');
						}
						num++;*/
						var aux3 = store.createRecord("chemical", {
								chemical_name : "biotin",
								isVolatile : true,
								volatilitySpeed : 0,
								diffusionCoefficient : 0,
							});
						aux3.save().then(function (item3) {
							var aux4 = store.createRecord("dynamicDropTest", {
									dropQuantity : 0,
									chemicalConcentration : 0,
									xCoordFromPlateCentre : 0,
									yCoordFromPlateCentre : 0,
									chemical : item3,
								});
							var dynamicDropItems = store.all('dynamicDropTest');
							if (self.get('controllers.dynamicDropTest.ddtConcentrationSlider')) {
								for (var i = 0; i < dynamicDropItems.content.length; i++) {
									dynamicDropItems.content[i].set('ddtConcentrationSlider', self.get('controllers.dynamicDropTest.ddtConcentrationSlider'));
								}
							}
							if (self.get('controllers.dynamicDropTest.ddtXaxisSlider')) {
								for (var i = 0; i < dynamicDropItems.content.length; i++) {
									dynamicDropItems.content[i].set('ddtXaxisSlider', self.get('controllers.dynamicDropTest.ddtXaxisSlider'));
								}
							}
							if (self.get('controllers.dynamicDropTest.ddtYaxisSlider')) {
								for (var i = 0; i < dynamicDropItems.content.length; i++) {
									dynamicDropItems.content[i].set('ddtYaxisSlider', self.get('controllers.dynamicDropTest.ddtYaxisSlider'));
								}
							}
							if (self.get('controllers.dynamicDropTest.ddtDropSlider')) {
								for (var i = 0; i < dynamicDropItems.content.length; i++) {
									dynamicDropItems.content[i].set('ddtDropSlider', self.get('controllers.dynamicDropTest.ddtDropSlider'));
								}
							}
							aux4.save().then(function (item4) {
								var aux2 = store.createRecord("chemotaxisExact", {
										description : "new chemo exact " /*+ num*/
									,
										chemotaxisType : "DDT",
										dynamicDropTestConf : item4,
									});
								aux2.save().then(function (item) {
									var aux5 = store.createRecord("interactionAtSpecificTime", {
											//"name" : strName,
											"description" : strName,
											"eventTime" : 0,
											"experimentCategory" : "CT",
											"chemotaxis" : item,
											"termotaxis" : null,
											"galvanotaxis" : null,
											"phototaxis" : null,
											"mechanosensation" : null,
										});
									aux5.save().then(function (item2) {
										var experimentModel = self.get('model');
										var exactEvents = experimentModel.get('interactionAtSpecificTime');
										exactEvents.pushObject(aux5);
										//set to be saved
										var controller = App.__container__.lookup("controller:experiment");
										var items = experimentModel.get('interactionAtSpecificTime.content.currentState');
										if (self.get('controllers.exact.exactTimeSlider')) {
											for (var i = 0; i < items.length; i++) {
												items[i].set('exactTimeSlider', self.get('controllers.exact.exactTimeSlider'));
											}
										}
										var proxySend = jQuery.proxy(controller.send, controller);
										proxySend('savingModelDidUpdate', experimentModel);

										self.send('addExactBox', "exact" + item2.get('id'), 0, strName, 'CT');
										self.send('setSelectedBox', "exact" + item2.get('id'));
										self.transitionToRoute('exact', item2.get('id'));
										document.getElementById("createName").value = "";
										$('#modalCreating').modal('hide');
									});
								});
								//});
							});
						});
					} else if (strType == "Phototaxis") {}
					else if (strType == "Termotaxis") {}
				} else if (strDuration == "Interval") {
					if (strType == "Mechanosensation") {}
					else if (strType == "Galvanotaxis") {
						/*store.find('galvanotaxisInterval').then(function (array) {
						var num = 0;
						if (array.content.length > 1) {
						for (var i = 0; i < array.content.length; i++) {
						if (parseFloat(array.content[i].get('id')) > num) {
						num = parseFloat(array.content[i].get('id'));
						}
						}
						} else {
						num = array.content.get('id');
						}
						num++;*/
						var aux3 = store.createRecord("electricShock", {
								amplitude : 0,
								shockDuration : 0,
								shockFrequency : 0,
							});
						aux3.save().then(function (item3) {
							var shockItems = store.all('electricShock');
							if (self.get('controllers.electricShock.shockDurationSlider')) {
								for (var i = 0; i < shockItems.content.length; i++) {
									shockItems.content[i].set('shockDurationSlider', self.get('controllers.electricShock.shockDurationSlider'));
								}
							}
							if (self.get('controllers.electricShock.shockFrequencySlider')) {
								for (var i = 0; i < shockItems.content.length; i++) {
									shockItems.content[i].set('shockFrequencySlider', self.get('controllers.electricShock.shockFrequencySlider'));
								}
							}
							if (self.get('controllers.electricShock.shockAmplitudeSlider')) {
								for (var i = 0; i < shockItems.content.length; i++) {
									shockItems.content[i].set('shockAmplitudeSlider', self.get('controllers.electricShock.shockAmplitudeSlider'));
								}
							}
							var aux2 = store.createRecord("galvanotaxisInterval", {
									description : "new galvano interval " /* + num*/
								,
									galvanotaxisType : "ES",
									electricShockConf : item3,
								});
							aux2.save().then(function (item) {
								var aux5 = store.createRecord("interactionFromt0tot1", {
										//"name" : strName,
										"description" : strName,
										"eventStartTime" : 0,
										"eventStopTime" : 1000,
										"experimentCategory" : "GT",
										"chemotaxis" : null,
										"termotaxis" : null,
										"galvanotaxis" : item,
										"phototaxis" : null,
										"mechanosensation" : null,
									});
								aux5.save().then(function (item2) {
									var experimentModel = self.get('model');
									var intervalEvents = experimentModel.get('interactionFromt0tot1');
									intervalEvents.pushObject(aux5);
									//set to be saved
									var controller = App.__container__.lookup("controller:experiment");
									var items = experimentModel.get('interactionFromt0tot1.content.currentState');
									if (self.get('controllers.interval.intervalTimeSlider')) {
										for (var i = 0; i < items.length; i++) {
											items[i].set('intervalTimeSlider', self.get('controllers.interval.intervalTimeSlider'));
										}
									}
									var proxySend = jQuery.proxy(controller.send, controller);
									proxySend('savingModelDidUpdate', experimentModel);

									self.send('addIntervalBox', "inter" + item2.get('id'), 0, 1000, strName, 'GT');
									self.send('setSelectedBox', "inter" + item2.get('id'));
									self.transitionToRoute('interval', item2.get('id'));
									document.getElementById("createName").value = "";
									$('#modalCreating').modal('hide');
								});
								//});
							});
						});
					} else if (strType == "Chemotaxis") {}
					else if (strType == "Phototaxis") {
						/*store.find('phototaxisInterval').then(function (array) {
						var num = 0;
						if (array.content.length > 1) {
						for (var i = 0; i < array.content.length; i++) {
						if (parseFloat(array.content[i].get('id')) > num) {
						num = parseFloat(array.content[i].get('id'));
						}
						}
						} else {
						num = array.content.get('id');
						}
						num++;*/
						var aux3 = store.createRecord("pointSourceLight", {
								waveLength : 0,
								intensity : 0,
								lightingPointDistance : 0,
								lightBeamRadius : 0,
							});
						aux3.save().then(function (item3) {
							var pointLightItems = store.all('pointSourceLight');
							if (self.get('controllers.pointSourceLight.pointLightWavelengthSlider')) {
								for (var i = 0; i < pointLightItems.content.length; i++) {
									pointLightItems.content[i].set('pointLightWavelengthSlider', self.get('controllers.pointSourceLight.pointLightWavelengthSlider'));
								}
							}
							if (self.get('controllers.pointSourceLight.pointLightIntensitySlider')) {
								for (var i = 0; i < pointLightItems.content.length; i++) {
									pointLightItems.content[i].set('pointLightIntensitySlider', self.get('controllers.pointSourceLight.pointLightIntensitySlider'));
								}
							}
							if (self.get('controllers.pointSourceLight.pointLightLightingDistanceSlider')) {
								for (var i = 0; i < pointLightItems.content.length; i++) {
									pointLightItems.content[i].set('pointLightLightingDistanceSlider', self.get('controllers.pointSourceLight.pointLightLightingDistanceSlider'));
								}
							}
							if (self.get('controllers.pointSourceLight.pointLightBeamSlider')) {
								for (var i = 0; i < pointLightItems.content.length; i++) {
									pointLightItems.content[i].set('pointLightBeamSlider', self.get('controllers.pointSourceLight.pointLightBeamSlider'));
								}
							}
							var aux2 = store.createRecord("phototaxisInterval", {
									description : "new photo interval " /* + num*/
								,
									phototaxisType : "PSL",
									pointSourceLightConf : item3,
								});
							aux2.save().then(function (item) {
								var aux5 = store.createRecord("interactionFromt0tot1", {
										//"name" : strName,
										"description" : strName,
										"eventStartTime" : 0,
										"eventStopTime" : 1000,
										"experimentCategory" : "PT",
										"chemotaxis" : null,
										"termotaxis" : null,
										"galvanotaxis" : null,
										"phototaxis" : item,
										"mechanosensation" : null,
									});
								aux5.save().then(function (item2) {
									var experimentModel = self.get('model');
									var intervalEvents = experimentModel.get('interactionFromt0tot1');
									intervalEvents.pushObject(aux5);
									//set to be saved
									var controller = App.__container__.lookup("controller:experiment");
									var items = experimentModel.get('interactionFromt0tot1.content.currentState');
									if (self.get('controllers.interval.intervalTimeSlider')) {
										for (var i = 0; i < items.length; i++) {
											items[i].set('intervalTimeSlider', self.get('controllers.interval.intervalTimeSlider'));
										}
									}
									var proxySend = jQuery.proxy(controller.send, controller);
									proxySend('savingModelDidUpdate', experimentModel);

									self.send('addIntervalBox', "inter" + item2.get('id'), 0, 1000, strName, 'PT');
									self.send('setSelectedBox', "inter" + item2.get('id'));
									self.transitionToRoute('interval', item2.get('id'));
									document.getElementById("createName").value = "";
									$('#modalCreating').modal('hide');
								});
								//});
							});
						});
					} else if (strType == "Termotaxis") {
						/*store.find('termotaxisInterval').then(function (array) {
						var num = 0;
						if (array.content.length > 1) {
						for (var i = 0; i < array.content.length; i++) {
						if (parseFloat(array.content[i].get('id')) > num) {
						num = parseFloat(array.content[i].get('id'));
						}
						}
						} else {
						num = array.content.get('id');
						}
						num++;*/
						var aux3 = store.createRecord("temperatureChangeInTime", {
								initialTemperature : 0,
								finalTemperature : 0,
							});
						aux3.save().then(function (item3) {
							var temperatureItems = store.all('temperatureChangeInTime');
							if (self.get('controllers.temperatureChangeInTime.temperatureFinalSlider')) {
								for (var i = 0; i < temperatureItems.content.length; i++) {
									temperatureItems.content[i].set('temperatureFinalSlider', self.get('controllers.temperatureChangeInTime.temperatureFinalSlider'));
								}
							}
							if (self.get('controllers.temperatureChangeInTime.temperatureInitialSlider')) {
								for (var i = 0; i < temperatureItems.content.length; i++) {
									temperatureItems.content[i].set('temperatureInitialSlider', self.get('controllers.temperatureChangeInTime.temperatureInitialSlider'));
								}
							}
							var aux2 = store.createRecord("termotaxisInterval", {
									description : "new termo interval " /* + num*/
								,
									termotaxisType : "TC",
									temperatureChangeInTime : item3,
									pointSourceHeatAvoidance : null,
								});
							aux2.save().then(function (item) {
								var aux5 = store.createRecord("interactionFromt0tot1", {
										//"name" : strName,
										"description" : strName,
										"eventStartTime" : 0,
										"eventStopTime" : 1000,
										"experimentCategory" : "TT",
										"chemotaxis" : null,
										"termotaxis" : item,
										"galvanotaxis" : null,
										"phototaxis" : null,
										"mechanosensation" : null,
									});
								aux5.save().then(function (item2) {
									var experimentModel = self.get('model');
									var intervalEvents = experimentModel.get('interactionFromt0tot1');
									intervalEvents.pushObject(aux5);
									//set to be saved
									var controller = App.__container__.lookup("controller:experiment");
									var items = experimentModel.get('interactionFromt0tot1.content.currentState');
									if (self.get('controllers.interval.intervalTimeSlider')) {
										for (var i = 0; i < items.length; i++) {
											items[i].set('intervalTimeSlider', self.get('controllers.interval.intervalTimeSlider'));
										}
									}
									var proxySend = jQuery.proxy(controller.send, controller);
									proxySend('savingModelDidUpdate', experimentModel);

									self.send('addIntervalBox', "inter" + item2.get('id'), 0, 1000, strName, 'TT');
									self.send('setSelectedBox', "inter" + item2.get('id'));
									self.transitionToRoute('interval', item2.get('id'));
									document.getElementById("createName").value = "";
									$('#modalCreating').modal('hide');
								});
							});
							//});
						});
					}
				} else if (strDuration == "Permanent") {
					if (strType == "Mechanosensation") {}
					else if (strType == "Galvanotaxis") {}
					else if (strType == "Chemotaxis") {
						if (this.get('controllers.experiment').isAnyChemoPermanent()) {
							$('#modalCreating').modal('hide');
							$('#modalNotPossible').modal('show');
							return;
						}
						/*store.find('chemotaxisPermanent').then(function (array) {
						var num = 0;
						if (array.content.length > 1) {
						for (var i = 0; i < array.content.length; i++) {
						if (parseFloat(array.content[i].get('id')) > num) {
						num = parseFloat(array.content[i].get('id'));
						}
						}
						} else {
						num = array.content.get('id');
						}
						num++;*/
						var aux3 = store.createRecord("chemical", {
								chemical_name : "biotin",
								isVolatile : true,
								volatilitySpeed : 0,
								diffusionCoefficient : 0,
							});
						aux3.save().then(function (item3) {
							var aux = store.createRecord("chemotaxisQuadrants1", {
									quadrantChemicalConcentration : 0,
									quadrantChemical : item3,
								});
							var quadrants1Items = store.all('chemotaxisQuadrants1');
							if (self.get('controllers.chemotaxisQuadrants1.quad1ConcentrationSlider')) {
								for (var i = 0; i < quadrants1Items.content.length; i++) {
									quadrants1Items.content[i].set('quad1ConcentrationSlider', self.get('controllers.chemotaxisQuadrants1.quad1ConcentrationSlider'));
								}
							}
							aux.save().then(function (item2) {
								var aux2 = store.createRecord("chemotaxisPermanent", {
										description : "new chemo permanent " /* + num*/
									,
										chemicalCategory : "CQ1",
										osmoticRing : null,
										staticPointSourceConf : null,
										chemotaxisQuadrants1 : item2,
										chemotaxisQuadrants2 : null,
										chemotaxisQuadrants4 : null,
									});
								aux2.save().then(function (item) {
									var aux5 = store.createRecord("experimentWideConf", {
											"description" : strName,
											"experimentCategory" : "CT",
											"chemotaxis" : item,
											"termotaxis" : null,
											"galvanotaxis" : null,
											"phototaxis" : null,
											"mechanosensation" : null,
										});
									aux5.save().then(function (item4) {
										var experimentModel = self.get('model');
										var intervalEvents = experimentModel.get('experimentWideConf');
										intervalEvents.pushObject(aux5);
										//set to be saved
										var controller = App.__container__.lookup("controller:experiment");
										var proxySend = jQuery.proxy(controller.send, controller);
										proxySend('savingModelDidUpdate', experimentModel);
										self.send('addPermanentBox', "perma" + item4.get('id'), strName, 'CT');
										self.send('setSelectedBox', "perma" + item4.get('id'));
										self.transitionToRoute('permanent', item4.get('id'));
										document.getElementById("createName").value = "";
										$('#modalCreating').modal('hide');
									});
								});
								//});
							});
						});
					} else if (strType == "Phototaxis") {}
					else if (strType == "Termotaxis") {
						/*store.find('termotaxisPermanent').then(function (array) {
						var num = 0;
						if (array.content.length > 1) {
						for (var i = 0; i < array.content.length; i++) {
						if (parseFloat(array.content[i].get('id')) > num) {
						num = parseFloat(array.content[i].get('id'));
						}
						}
						} else {
						num = array.content.get('id');
						}
						num++;*/
						var aux3 = store.createRecord("linearThermalGradient", {
								temperatureRightHorizonal : 0,
								temperatureLeftHorizontal : 1,
							});
						var gradientItems = store.all('linearThermalGradient');
						if (self.get('controllers.linearThermalGradient.gradientLeftSlider')) {
							for (var i = 0; i < gradientItems.content.length; i++) {
								gradientItems.content[i].set('gradientLeftSlider', self.get('controllers.linearThermalGradient.gradientLeftSlider'));
							}
						}
						if (self.get('controllers.linearThermalGradient.gradientRightSlider')) {
							for (var i = 0; i < gradientItems.content.length; i++) {
								gradientItems.content[i].set('gradientRightSlider', self.get('controllers.linearThermalGradient.gradientRightSlider'));
							}
						}
						aux3.save().then(function (item3) {
							var aux2 = store.createRecord("termotaxisPermanent", {
									description : "new termo permanent " /* + num*/
								,
									termotaxisType : "LT",
									linearThermalGradient : item3,
								});
							aux2.save().then(function (item) {
								var aux5 = store.createRecord("experimentWideConf", {
										"description" : strName,
										"experimentCategory" : "TT",
										"chemotaxis" : null,
										"termotaxis" : item,
										"galvanotaxis" : null,
										"phototaxis" : null,
										"mechanosensation" : null,
									});
								aux5.save().then(function (item4) {
									var experimentModel = self.get('model');
									var intervalEvents = experimentModel.get('experimentWideConf');
									intervalEvents.pushObject(aux5);
									//set to be saved
									var controller = App.__container__.lookup("controller:experiment");
									var proxySend = jQuery.proxy(controller.send, controller);
									proxySend('savingModelDidUpdate', experimentModel);
									self.send('addPermanentBox', "perma" + item4.get('id'), strName, 'TT');
									self.send('setSelectedBox', "perma" + item4.get('id'));
									self.transitionToRoute('permanent', item4.get('id'));
									document.getElementById("createName").value = "";
									$('#modalCreating').modal('hide');
								});
								//});
							});
						});
					}
				}
			},
		},
		isRerender : false,
	});

newEventTypeSelected = function (value) {
	if (value == 0) {
		$('#mechanoOption').removeAttr('disabled');
		$('#chemoOption').removeAttr('disabled');
		$('#termoOption').attr('disabled', 'disabled');
		$('#galvanoOption').attr('disabled', 'disabled');
		$('#photoOption').attr('disabled', 'disabled');

		$('#mechanoOption').attr("selected", "selected");
	} else if (value == 1) {
		$('#mechanoOption').attr('disabled', 'disabled');
		$('#chemoOption').attr('disabled', 'disabled');
		$('#termoOption').removeAttr('disabled');
		$('#galvanoOption').removeAttr('disabled');
		$('#photoOption').removeAttr('disabled');

		$('#termoOption').attr("selected", "selected");
	} else if (value == 2) {
		$('#mechanoOption').attr('disabled', 'disabled');
		$('#chemoOption').removeAttr('disabled');
		$('#termoOption').removeAttr('disabled');
		$('#galvanoOption').attr('disabled', 'disabled');
		$('#photoOption').attr('disabled', 'disabled');

		$('#chemoOption').attr("selected", "selected");
	}
}
