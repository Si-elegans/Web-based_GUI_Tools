App.ExperimentController = Ember.ObjectController.extend({
		needs : ['visualization', 'application', 'definition', 'exact', 'interval', 'permanent', 'wormStatus', 'environment', 'plateConfiguration', 'chemotaxisPermanent'],
		changedModels : [],
		showButtons : function () {
			var currentPath = this.get('controllers.application.currentPath');
			return (currentPath === "experiment.index");
		}
		.property('controllers.application.currentPath'),
		showColor : function () {
			var currentPath = this.get('controllers.application.currentPath');
			return (currentPath === 'experiment.definition.index');
		}
		.property('controllers.application.currentPath'),
		saveChanges : function () {
			var num = this.changedModels.length;
			var count = 0;
			if (this.changedModels.length == 0)
				return;
			var A = false;
			$('#modalWaiting').modal('show');
			for (var i = 0; i < this.changedModels.length; i++) {
				if (i == this.changedModels.length - 1)
					A = true;
				this.changedModels[i].save().then(function () {
					count++;
					if (count == num) {
						$('#modalWaiting').modal('hide');
						$('#modalSaved').modal('show');
					}
				});
			}
			changedModels = [];
		},
		isAnyChemoPermanent : function () {
			var permanents = this.get('model.experimentDefinition.experimentWideConf');
			var aux = permanents.get('content.currentState');
			for (var i = 0; i < aux.length; i++) {
				if (aux[i].get('experimentCategory') == 'CT') {
					return aux[i].get('chemotaxis.chemicalCategory');
				}
			}
			return false;
		},
		init : function () {
			var wormScale = 100;
			var loader = new THREE.ColladaLoader();
			var model, model2, model3;
			
			var scene = new THREE.Scene();
			this.set("scene", scene);
			this.set('isRunningAnimation', false);
			this.set('isInFirstAnimationFrame', true);

			var parent = this;

			function animate() {
				if (parent.get('isRunningAnimation')) {
					var currentStep = 0;
					var timeFromCurrentStep;
					var time;
					var steps = parent.get('steps');
					if (parent.get('isInFirstAnimationFrame')) {
						parent.set('isInFirstAnimationFrame', false);
						initialTime = Date.now();

						//draw timeline line in the canvas
						var canvas = document.getElementById('timelineCanvas');
						var context = canvas.getContext('2d');

						context.beginPath();
						context.moveTo(15, 0);
						context.lineTo(15, canvas.width);
						context.lineWidth = 1.5;
						context.strokeStyle = '#ff0000';
						context.stroke();
					} else {

						parent.set('isRunningAnimation', false);
						time = (Date.now() - initialTime) * 0.0005; // seconds
						for (var i = currentStep; i < steps.length; i++) {
							if (time < steps[i].time) {
								currentStep = i - 1;
								timeFromCurrentStep = time - steps[i - 1].time;
								parent.set('isRunningAnimation', true);
								break;
							}
						}
						if (!parent.get('isRunningAnimation')) {
							return;
						}
					}

					var canvas = document.getElementById('timelineCanvas');
					var context = canvas.getContext('2d');

					context.clearRect(0, 0, canvas.width, canvas.height);
					context.beginPath();
					context.moveTo(15 + Math.floor(time * 13.2) + 0.5, 0);
					context.lineTo(15 + Math.floor(time * 13.2) + 0.5, canvas.width);
					context.lineWidth = 1;
					context.strokeStyle = '#ff0000';
					context.stroke();

					parent.get('controllers.visualization').send('timeChanged', time);

					var positions = [];

					for (var i = 0; i < steps[currentStep].DOFnum; i++) {
						var myPosition = [0, 0, 0];
						myPosition[0] = steps[currentStep].getTransX(i) + steps[currentStep].getSpeedX(i) * timeFromCurrentStep;
						myPosition[1] = steps[currentStep].getTransY(i) + steps[currentStep].getSpeedY(i) * timeFromCurrentStep;
						myPosition[2] = steps[currentStep].getTransZ(i) + steps[currentStep].getSpeedZ(i) * timeFromCurrentStep;
						positions[i] = myPosition;
					}
					for (var i = 0; i < 12; i++) {
						objects = [];
						var name;
						scene.traverse(function (object) {
							name = "joint";
							name += (i + 1);
							if (object.name === name)
								objects[objects.length] = object;
							// do what you want with it.

						});
						for (var j = 0; j < objects.length; j++) {
							objects[j].position.x = 5 * (positions[2 * i + 1][0] + positions[2 * i + 51][0]) / wormScale;
							objects[j].position.y = 5 * (positions[2 * i + 1][1] + positions[2 * i + 51][1]) / wormScale;
							objects[j].position.z = 5 * (positions[2 * i + 1][2] + positions[2 * i + 51][2]) / wormScale;

							//difference between last and next sphere
							var vec = new THREE.Vector3(0.5 * (positions[2 * i + 2][0] + positions[2 * i + 27][0]) - 0.5 * (positions[2 * i][0] + positions[2 * i + 25][0]), 0.5 * (positions[2 * i + 2][1] + positions[2 * i + 27][1]) - 0.5 * (positions[2 * i][1] + positions[2 * i + 25][1]), 0.5 * (positions[2 * i + 2][2] + positions[2 * i + 27][2]) - 0.5 * (positions[2 * i][2] + positions[2 * i + 25][2]));

							//console.log(vec);

							vec.normalize();

							//console.log(vec);

							var angle = Math.acos(vec.z);

							//console.log(-angle);

							objects[j].rotation.y = 3.1419 + angle;
						}

					}
					var signals = parent.get('signals');
					signals.sceneGraphChanged.dispatch();
				}
				requestAnimationFrame(animate);
			}

			animate();

			function readFile(path) {

				var file;

				$.ajax({
					type : "GET",
					url : path,
					async : false,
					success : function (data) {
						file = data;
						var lines = file.split("\n");
						lines = lines.slice(0, lines.length - 1);
						steps = [];
						var i = 0;
						while (i < lines.length) {

							//take the time
							var tokens = lines[i].split("= ");
							var time = parseFloat(String(tokens[1]));
							var myStep = new step(time);

							//take the DOFs
							i++;
							var xTokens = lines[i].split(" ");

							var j = 3;
							var num;
							while (j < xTokens.length) {
								num = myStep.getDOFnum();
								myStep.addDOF(num, parseFloat(String(xTokens[j])), parseFloat(String(xTokens[j + 1])), parseFloat(String(xTokens[j + 2])), parseFloat(String(xTokens[j + 3])), parseFloat(String(xTokens[j + 4])), parseFloat(String(xTokens[j + 5])), parseFloat(String(xTokens[j + 6])));
								j += 7;
							}

							//take the speeds
							i++;
							var vTokens = lines[i].split(" ");

							var k = 3;
							num = 0;
							while (k < vTokens.length) {
								myStep.addSpeed(String(num), parseFloat(String(vTokens[k])), parseFloat(String(vTokens[k + 1])), parseFloat(String(vTokens[k + 2])));
								num++;
								k += 6;
							}

							steps[steps.length] = myStep;
							i++;
							//jump F=
							i++;
						}
						parent.set('steps', steps);
					}
				});

				return;
			}

			loader.load(staticPath + 'data/probeta.dae', function (collada) {
				
				var probetaScale = 3.5;
				
				parent.set('probetaScale',probetaScale);

				model = collada.scene;

				model.scale.x = model.scale.y = model.scale.z = probetaScale*10; // 1/8 scale, modeled in cm

				model.name = "probeta";
				loader.load(staticPath + 'data/probetacuadrada.dae', function (item) {
					loader.load(staticPath + 'data/probetahexagono.dae', function (item2) {

						loader.load(staticPath + 'data/worm_9_neurons.dae', function (collada2) {
							scene.add(model);
							model2 = collada2.scene;
							model2.scale.x = model2.scale.y = model2.scale.z = wormScale; // 1/8 scale, modeled in cm
							//make cuticle translucent
							for (var i = 0; i < model2.children.length; i++) {
								if (model2.children[i].name == "CuticleLOW") {
									model2.children[i].children[0].material.transparent = true;
									model2.children[i].children[0].material.opacity = 1;
									//computeTouchingZones(model2.children[i].children[0].geometry,model2.children);
								} else {
									if (model2.children[i].children[0].material) {
										model2.children[i].children[0].material.ambient.r = 0.5;
										model2.children[i].children[0].material.ambient.g = 0.5;
										model2.children[i].children[0].material.ambient.b = 0.5;
										model2.children[i].children[0].material.color.r = 0.3;
										model2.children[i].children[0].material.color.g = 0.0;
										model2.children[i].children[0].material.color.b = 0.0;
										model2.children[i].children[0].receiveShadow = false;
										model2.children[i].receiveShadow = false;
									} else {
										console.log(model2.children[i].name);
									}
								}
							}

							model.position.x = 0;
							model.position.y = 0;
							model.position.z = 0;
							model.castShadow = true;
							model.receiveShadow = true;

							parent.set('plateModel', model);
							parent.set('plateCylinderModel', model);

							var aux1 = item.scene;
							aux1.scale.x = aux1.scale.y = aux1.scale.z = probetaScale*10;
							parent.set('plateCubeModel', aux1);

							var aux2 = item2.scene;
							aux2.scale.x = aux2.scale.y = aux2.scale.z = probetaScale*10;
							parent.set('plateHexagonModel', aux2);
							THREE.ImageUtils.crossOrigin = 'anonymous';
							var quad4Material = new THREE.MeshPhongMaterial({
									map : THREE.ImageUtils.loadTexture(staticPath + 'data/probeta colores 4.jpg')
								});
							parent.set('quad4Material', quad4Material);
							var quad2Material = new THREE.MeshPhongMaterial({
									map : THREE.ImageUtils.loadTexture(staticPath + 'data/probeta colores 2.jpg')
								});
							parent.set('quad2Material', quad2Material);
							var quad1Material = new THREE.MeshPhongMaterial({
									map : THREE.ImageUtils.loadTexture(staticPath + 'data/probeta.jpg')
								});
							parent.set('quad1Material', quad1Material);
							var ringMaterial = new THREE.MeshPhongMaterial({
									map : THREE.ImageUtils.loadTexture(staticPath + 'data/probeta colores c.jpg')
								});
							parent.set('ringMaterial', ringMaterial);

							parent.send('makePlateQuad1');

							//change worm's position to fit the starting position in SOFA. When starting the simulation, this transformation will be removed.
							model2.position.x = probetaScale*28 * parseFloat(parent.get('model.environmentDefinition.wormStatus.xCoordFromPlateCentre'));
							model2.position.y = -115*probetaScale - 1;
							model2.position.z = probetaScale*28 * parseFloat(parent.get('model.environmentDefinition.wormStatus.yCoorDFromPlateCentre'));
							model2.rotation.y = parseFloat(parent.get('model.environmentDefinition.wormStatus.angleRelativeXaxis'));
							model2.castShadow = false;
							model2.receiveShadow = false;
							scene.add(model2);
							console.log("worm and plate loaded and added");

							var plateConf = parent.get('model.environmentDefinition.plateConfiguration.shape');
							parent.get('controllers.plateConfiguration').setShape(plateConf);
							var chemo = parent.isAnyChemoPermanent();
							if (chemo) {
								parent.get('controllers.chemotaxisPermanent').setType(chemo);
							}

							loader.load(staticPath + 'data/cube.dae', function (obj1) {
								loader.load(staticPath + 'data/cylinder.dae', function (obj2) {
									loader.load(staticPath + 'data/prism.dae', function (obj3) {
										parent.set('cubeModel',obj1.scene.children[2]);
										parent.set('cylinderModel',obj2.scene.children[0]);
										parent.set('prismModel',obj3.scene.children[0]);
										var obstacles = parent.get('model.environmentDefinition._data.obstacle');
										for(var i = 0; i < obstacles.length; i++){
											if(obstacles[i]._data.shape == "CU"){
												var scene = parent.get('scene');
												var newObject = parent.get('cubeModel').clone();
												scene.add(newObject);
												var cube = scene.children[scene.children.length - 1];
												cube.uuid = obstacles[i].id;
												var cubeData = obstacles[i].get('Cube._data')
												cube.scale.x = 0.1*cubeData.side1Length;
												cube.scale.y = 0.1*cubeData.depth;
												cube.scale.z = 0.1*cubeData.side2Length;
												cube.position.y = cube.scale.y*50 - probetaScale*180;
												cube.position.x = probetaScale*28*obstacles[i]._data.xCoordFromPlateCentre;
												cube.position.z = probetaScale*28*obstacles[i]._data.yCoorDFromPlateCentre;
											}
											else if(obstacles[i]._data.shape == "CY"){
												var scene = parent.get('scene');
												var newObject = parent.get('cylinderModel').clone();
												scene.add(newObject);
												var cylinder = scene.children[scene.children.length - 1];
												cylinder.uuid = obstacles[i].id;
												var cylinderData = obstacles[i].get('Cylinder._data')
												cylinder.scale.x = 10*cylinderData.radius;
												cylinder.scale.y = 10*cylinderData.radius;
												cylinder.scale.z = 10*cylinderData.length;
												cylinder.rotation.x = 1.5708;
												cylinder.position.y = cylinder.scale.z - probetaScale*180;
												cylinder.position.x = probetaScale*28*obstacles[i]._data.xCoordFromPlateCentre;
												cylinder.position.z = probetaScale*28*obstacles[i]._data.yCoorDFromPlateCentre;
											}
											else if(obstacles[i]._data.shape == "HE"){
												var scene = parent.get('scene');
												var newObject = parent.get('prismModel').clone();
												scene.add(newObject);
												var prism = scene.children[scene.children.length - 1];
												prism.uuid = obstacles[i].id;
												var prismData = obstacles[i].get('Hexagon._data')
												prism.scale.x = 0.05*prismData.sideLength;
												prism.scale.y = 0.05*prismData.sideLength;
												prism.scale.z = 0.05*prismData.depth;
												prism.rotation.x = 1.5708;
												prism.position.y = prism.scale.z*600 - probetaScale*180;
												prism.position.x = probetaScale*28*obstacles[i]._data.xCoordFromPlateCentre;
												prism.position.z = probetaScale*28*obstacles[i]._data.yCoorDFromPlateCentre;
											}
										}
										setTimeout(function () {
											var signals = parent.get('signals');
											signals.cameraChanged.dispatch();
											$('#modalLoading').modal('hide');
										}, 2000);
									});
								});
							});
						});
					});
				});
			});
		},
		hasToBeCloned : false,
		changeCloned : function () {}

		.observes('controllers.application.currentPath'),

		actions : {
			addCube : function (name){
				var scene = this.get('scene');
				var newObject = this.get('cubeModel').clone();
				var probetaScale = this.get('probetaScale');
				scene.add(newObject);
				var cube = scene.children[scene.children.length - 1];
				cube.uuid = name;
				cube.scale.x = 0.1;
				cube.scale.y = 0.1;
				cube.scale.z = 0.1;
				cube.position.y = cube.scale.y*50 - probetaScale*180;
				var signals = this.get('signals');
				signals.cameraChanged.dispatch();
			},
			addCylinder : function (name){
				var scene = this.get('scene');
				var newObject = this.get('cylinderModel').clone();
				var probetaScale = this.get('probetaScale');
				scene.add(newObject);
				var cylinder = scene.children[scene.children.length - 1];
				cylinder.uuid = name;
				cylinder.rotation.x = 1.5708;
				cylinder.scale.x = 10;
				cylinder.scale.y = 10;
				cylinder.scale.z = 10;
				cylinder.position.y =  cylinder.scale.z - probetaScale*180;
				var signals = this.get('signals');
				signals.cameraChanged.dispatch();
			},
			addPrism : function (name){
				var scene = this.get('scene');
				var newObject = this.get('prismModel').clone();
				var probetaScale = this.get('probetaScale');
				scene.add(newObject);
				var prism = scene.children[scene.children.length - 1];
				prism.uuid = name;
				prism.rotation.x = 1.5708;
				prism.scale.x = 0.05;
				prism.scale.y = 0.05;
				prism.scale.z = 0.05;
				prism.position.y = prism.scale.z*600 - probetaScale*180;
				var signals = this.get('signals');
				signals.cameraChanged.dispatch();
			},
			setParams : function (params) {
				this.set('viewport', params[0]);
				this.set('renderer', params[1]);
				this.set('camera', params[2]);
				this.set('controls', params[3]);
				this.set('signals', params[4]);
			},
			rotateWorm : function (value) {}

			.observes('model.idx'),
			changeToEnvironment : function () {
				if (App.currentPath.slice(App.currentPath.lastIndexOf('.') + 1) == "visualization") {
					return;
				}
				var router = this.get('target');
				router.transitionTo('environment');
			},
			focusNeuron : function (neuron) {
				var scene = this.get('scene');
				var controls = this.get('controls');
				var camera = this.get('camera');

				var previousFocusedNeuron = this.get('focusedNeuron');
				if (previousFocusedNeuron) {

					var geom = scene.getObjectByName(previousFocusedNeuron.name);
					geom.children[0].material.color.setRGB(0.3, 0.0, 0.0);

					for (var i = 0; i < previousFocusedNeuron.synapse.length; i++) {
						var relatedNeuron = scene.getObjectByName(previousFocusedNeuron.synapse[i]);
						relatedNeuron.children[0].material.color.setRGB(0.3, 0.0, 0.0);
					}
				}

				this.set('focusedNeuron', neuron);

				var focusedNeuron = scene.getObjectByName(neuron.name);

				focusedNeuron.children[0].material.color.setRGB(0.0, 1.0, 0.0);

				for (var i = 0; i < neuron.synapse.length; i++) {
					var relatedNeuron = scene.getObjectByName(neuron.synapse[i]);
					relatedNeuron.children[0].material.color.setRGB(1, 1, 0.3);
				}

				console.log(camera.position);
				console.log(camera.quaternion);
				console.log(controls.target);
				controls.object.position.x = neuron.cameraFrom[0];
				controls.object.position.y = neuron.cameraFrom[1];
				controls.object.position.z = neuron.cameraFrom[2];

				controls.object.quaternion.x = neuron.cameraTo[0];
				controls.object.quaternion.y = neuron.cameraTo[1];
				controls.object.quaternion.z = neuron.cameraTo[2];
				controls.object.quaternion.z = neuron.cameraTo[3];

				controls.target.x = neuron.controlsTarget[0];
				controls.target.y = neuron.controlsTarget[1];
				controls.target.z = neuron.controlsTarget[2];

				controls.update();

				var signals = this.get('signals');
				signals.cameraChanged.dispatch(camera);
			},
			playAnimation : function () {
				this.set('isRunningAnimation', true);
			},
			goToVisualization : function () {
				var router = this.get('target');
				router.transitionTo('visualization');
			},
			goToDefinitionModify : function () {
				this.set('controllers.definition.isModifiable', true);
				this.set('controllers.exact.isModifiable', true);
				this.set('controllers.permanent.isModifiable', true);
				this.set('controllers.interval.isModifiable', true);
				var router = this.get('target');
				router.transitionTo('definition');
			},

			makePlateCylinder : function () {
				var model = this.get('plateModel');
				var mymaterial = model.children[0].children[0].material;
				var newModel = this.get('plateCylinderModel');
				newModel.children[0].children[0].material = mymaterial;
				this.set('plateModel', newModel);
				var scene = this.get('scene');
				scene.children[6] = newModel;
				var signals = this.get('signals');
				signals.cameraChanged.dispatch();
			},

			makePlateHexagon : function () {
				var model = this.get('plateModel');
				var mymaterial = model.children[0].children[0].material;
				var newModel = this.get('plateHexagonModel');
				newModel.children[0].children[0].material = mymaterial;
				this.set('plateModel', newModel);
				var scene = this.get('scene');
				scene.children[6] = newModel;
				var signals = this.get('signals');
				signals.cameraChanged.dispatch();
			},

			makePlateCube : function () {
				var model = this.get('plateModel');
				var mymaterial = model.children[0].children[0].material;
				var newModel = this.get('plateCubeModel');
				newModel.children[0].children[0].material = mymaterial;
				this.set('plateModel', newModel);
				var scene = this.get('scene');
				scene.children[6] = newModel;
				var signals = this.get('signals');
				signals.cameraChanged.dispatch();
			},

			makePlateQuad1 : function () {
				var model = this.get('plateModel');
				model.children[0].children[0].material = this.get('quad1Material');
				var signals = this.get('signals');
				signals.cameraChanged.dispatch();
			},

			makePlateQuad2 : function () {
				var model = this.get('plateModel');
				model.children[0].children[0].material = this.get('quad2Material');
				var signals = this.get('signals');
				signals.cameraChanged.dispatch();
			},

			makePlateQuad4 : function () {
				var model = this.get('plateModel');
				model.children[0].children[0].material = this.get('quad4Material');
				var signals = this.get('signals');
				signals.cameraChanged.dispatch();
			},

			makePlateRing : function () {
				var model = this.get('plateModel');
				model.children[0].children[0].material = this.get('ringMaterial');
				var signals = this.get('signals');
				signals.cameraChanged.dispatch();
			},

			goToDefinitionClone : function () {
				var router = this.get('target');
				var self = this;
				var index = document.URL.slice(document.URL.lastIndexOf('/') + 1, document.URL.length);
				if (index == "") {
					var aux = document.URL.slice(0, document.URL.length - 1);
					index = aux.slice(aux.lastIndexOf('/') + 1, aux.length)
				}

				var csrftoken = $.cookie('csrftoken');
				$.ajax({
					url : baseURL + "/restAPI/behaviouralExperiments_nested/" + index,
					cache : false,
					type : "GET",
					contentType : "application/json; charset=utf-8",
					dataType : "json",
					success : function (msg) {
						if (msg) {
							var csrftoken = $.cookie('csrftoken');
							msg.public = false;
							$.ajax({
								url : baseURL + "/restAPI/behaviouralExperiments_nested/",
								cache : false,
								type : "POST",
								data : JSON.stringify(msg),
								contentType : "application/json; charset=utf-8",
								dataType : "json",
								success : function (msg2) {
									if (msg2) {
										router.transitionTo('experiment', msg2.uuid).then(function () {
											var con = App.__container__.lookup("controller:experiment");
											con.init();
											router.transitionTo('definition');
										});
									} else {}
								},
								beforeSend : function (xhr) {
									xhr.setRequestHeader('X-CSRFToken', csrftoken);
									//xhr.setRequestHeader('X-CSRFToken', $('meta[name="csrf-token"]').attr('content'));
									//xhr.setRequestHeader("Authorization", "Basic " + btoa("admin" + ":" + "admin"));
									//xhr.setRequestHeader("Content-Type", "application/json");
								},
							});
						} else {}
					},
					beforeSend : function (xhr) {
						xhr.setRequestHeader('X-CSRFToken', csrftoken);
						//xhr.setRequestHeader('X-CSRFToken', $('meta[name="csrf-token"]').attr('content'));
						//xhr.setRequestHeader("Authorization", "Basic " + btoa("admin" + ":" + "admin"));
						//xhr.setRequestHeader("Content-Type", "application/json");
					},
				});
			},
			goToDefinitionView : function () {
				this.set('controllers.definition.isModifiable', false);
				this.set('controllers.exact.isModifiable', false);
				this.set('controllers.interval.isModifiable', false);
				this.set('controllers.permanent.isModifiable', false);
				var router = this.get('target');
				router.transitionTo('definition');
			},
			savingModelDidUpdate : function (model) {
				for (var i = 0; i < this.changedModels.length; i++) {
					if (model == this.changedModels[i]) {
						return;
					}
				}
				this.changedModels[this.changedModels.length] = model;
			},
			removeObstacle: function (id){
				var obstacles = this.get('model.environmentDefinition._data.obstacle');
				for(var i = 0; i < obstacles.length; i++){
					if(obstacles[i].id == id){
						obstacles[i].destroyRecord();
						obstacles.splice(i, 1);
						break;
					}
				}
				var scene = this.get('scene');
				for(var j = 0; j < scene.children.length; j++){
					if(scene.children[j].uuid == id){
						scene.remove(scene.children[j]);
						break;
					}
				}
				var signals = this.get('signals');
				signals.cameraChanged.dispatch();
			}
		},

	});
