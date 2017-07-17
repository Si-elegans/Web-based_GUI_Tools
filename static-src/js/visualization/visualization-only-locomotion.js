obstacleEnum = {
	CUBE : 0,
	CYLINDER : 1,
	HEXAGONAL : 2
}
environmentEnum = {
	WATER : 0,
	GELATIN : 1,
	AGAR : 2
}

var model, model2;
var scene = new THREE.Scene();
var isRunningAnimation = false;
var isInFirstAnimationFrame = true;
var locomotion = [];
//var wormScale = 14.375;
var wormScale = 115;
var loader = new THREE.ColladaLoader();
var container;
var camera, controls, renderer, transformControls;
var cubes = [], objects = [], plane, cylinders = [], hexagonals = [];
var path, webPath;
var obstacleType = obstacleEnum.CUBE;
var renderWidth;
var renderHeight;
var experimentDuration;
var timeSlider, opacitySlider;
var currentStep = 0;
var timeFromCurrentStep;
var timeStep = 0.02;
var lastTime = 0.0;
var lastTime2 = 0.0;
var opacityMaterial = 1.0;
var playingVelocity = 1.0;
var timeRectPos = 0;

var mouse = new THREE.Vector2(),
offset = new THREE.Vector3(),
INTERSECTED, SELECTED;
var model, model2, model3;

var OSName = "unknown OS";
if (navigator.appVersion.indexOf("Win") != -1)
	OSName = "Windows";
if (navigator.appVersion.indexOf("Mac") != -1)
	OSName = "MacOS";
if (navigator.appVersion.indexOf("X11") != -1)
	OSName = "UNIX";
if (navigator.appVersion.indexOf("Linux") != -1)
	OSName = "Linux";

initButtons();
$(document).ready(function() {
  $('#modalLoading').modal('show');
});
readFile();

loader.load(staticPath + 'data/probeta.dae', function (collada) {

	
	model = collada.scene;

	model.scale.x = model.scale.y = model.scale.z = 10; // 1/8 scale, modeled in cm

	model.name = "probeta";

	// instantiate a loader
	var loader_texture = new THREE.TextureLoader();

	//allow cross origin loading
	loader_texture.crossOrigin = '';
	THREE.ImageUtils.crossOrigin = '';
	
	var quad1Material = new THREE.MeshPhongMaterial( { map: THREE.ImageUtils.loadTexture(staticPath + 'data/probeta.jpg') } );

	// load a resource
	/*loader_texture.load(staticPath + 'data/probeta colores.jpg', function (collada2){
		model.children[0].children[0].material = new THREE.MeshPhongMaterial({map: collada2, needsUpdate: true});
		model.children[0].children[0].geometry.buffersNeedUpdate = true;
		model.children[0].children[0].geometry.uvsNeedUpdate = true;
	}
	);*/
	
	model.children[0].children[0].material = quad1Material;

	loader.load(staticPath + 'data/gusano24yNeuronasPesajeNEURONAS.dae', function (collada2) {

		scene.add(model);
		model2 = collada2.scene;

		model2.scale.x = model2.scale.y = model2.scale.z = wormScale; // 1/8 scale, modeled in cm
		//make cuticle translucent
		for (var i = 0; i < model2.children.length; i++) {
			if (model2.children[i].name == "CuticleLOW_OK1") {
				model2.children[i].children[0].material.transparent = true;
				model2.children[i].children[0].material.opacity = 1;
				opacityMaterial = model2.children[i].children[0].material;
			} else {
				if (model2.children[i].children.length > 0 && model2.children[i].children[0].material) {
					//model2.children[i].children[0].material.ambient.r = 0.5;
					//model2.children[i].children[0].material.ambient.g = 0.5;
					//model2.children[i].children[0].material.ambient.b = 0.5;
					model2.children[i].children[0].material.color.r = 0.3;
					model2.children[i].children[0].material.color.g = 0.0;
					model2.children[i].children[0].material.color.b = 0.0;
					model2.children[i].children[0].receiveShadow = true;
					model2.children[i].receiveShadow = true;
					model2.children[i].children[0].material.transparent = false;
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
		//change worm's position to fit the starting position in SOFA. When starting the simulation, this transformation will be removed.
		model2.position.x = 440;
		model2.position.y = -15;
		model2.position.z = 20;
		model2.rotation.y = 3.1419;
		model2.castShadow = true;
		model2.receiveShadow = true;

		scene.add(model2);
		console.log("worm and plate loaded and added");
		
		scene.add(new THREE.AmbientLight(0x666666));

        var light = new THREE.SpotLight(0x666666, 1);
        light.name = "spot";
        light.position.set(0, 15000, 0);
        light.castShadow = false;

        light.shadowCameraNear = 200;
        //light.shadowCameraFar = viewport.far;
        light.shadowCameraFov = 50;

        light.shadowBias = -0.00022;
        light.shadowDarkness = 0.5;

        light.shadowMapWidth = 2048;
        light.shadowMapHeight = 2048;

        scene.add(light);
        
        var light2 = new THREE.SpotLight(0x666666, 0.8);
        light2.name = "spot";
        light2.position.set(0, -15000, 0);
        light2.castShadow = false;

        light2.shadowCameraNear = 200;
        //light.shadowCameraFar = viewport.far;
        light2.shadowCameraFov = 50;

        light2.shadowBias = -0.00022;
        light2.shadowDarkness = 0.2;

        light2.shadowMapWidth = 2048;
        light2.shadowMapHeight = 2048;

        scene.add(light2);
        
        var light3 = new THREE.SpotLight(0x666666, 0.8);
        light3.name = "spot";
        light3.position.set(-15000, 0, 0);
        light3.castShadow = false;

        light3.shadowCameraNear = 200;
        //light.shadowCameraFar = viewport.far;
        light3.shadowCameraFov = 50;

        light3.shadowBias = -0.00022;
        light3.shadowDarkness = 0.2;

        light3.shadowMapWidth = 2048;
        light3.shadowMapHeight = 2048;

        scene.add(light3);
        
        var light4 = new THREE.SpotLight(0x666666, 1);
        light4.name = "spot";
        light4.position.set(15000, 0, 0);
        light4.castShadow = false;

        light4.shadowCameraNear = 200;
        //light.shadowCameraFar = viewport.far;
        light4.shadowCameraFov = 50;

        light4.shadowBias = -0.00022;
        light4.shadowDarkness = 0.2;

        light4.shadowMapWidth = 2048;
        light4.shadowMapHeight = 2048;

        scene.add(light4);

		init();
		animate();
		$('#modalLoading').modal('hide');
	});
});

callTimeline();

function initButtons() {
	timeSlider = new Slider('#timeSlider', {
			range : false,
			max : new Number(255),
			step : 0.01,
			value : 0,
			id : 'timeSliderImplemented',
		});
	
	timeSlider.on("change",function(slideEvt){
		for (var i = 0; i < locomotion.length - 1; i++) {
			if (slideEvt.newValue < parseFloat(locomotion[i].t)) {
				currentStep = i - 1;
				timeFromCurrentStep = slideEvt.newValue - parseFloat(locomotion[i - 1].t);
				break;
			}
		}
		lastTime = Date.now();
		lastTime2 = timeSlider.getValue();
		goToAnimation(slideEvt.newValue);
		
	});

	opacitySlider = new Slider('#opacitySlider', {
			range : false,
			max : new Number(1),
			step : 0.01,
			value : 1,
			id : 'opacitySliderImplemented',
		});
	opacitySlider.on("change", function (slideEvt) {
		opacityMaterial.opacity = slideEvt.newValue;
		render();
	});
	
	velocitySlider = new Slider('#velocitySlider', {
			range : false,
			max : new Number(2),
			step : 0.01,
			value : 1,
			id : 'opacitySliderImplemented',
		});
	velocitySlider.on("change", function (slideEvt) {
		playingVelocity = slideEvt.newValue;
		render();
	});

}

function init() {
	
	//resize the canvas to match the size of its parent
	var c=document.getElementById("timeCanvas");
	var ctx=c.getContext("2d");
	ctx.canvas.width = ctx.canvas.clientWidth;
	ctx.canvas.height = ctx.canvas.clientHeight;
	

	//obtain the path. This way the code works in every computer.
	webPath = document.URL;
	webPath = webPath.slice(0, webPath.lastIndexOf("/"));

	camera = new THREE.PerspectiveCamera(70, window.innerWidth / window.innerHeight, 1, 100000);
	camera.position.z = 500;
	camera.position.y = 3000;
	camera.lookAt(new THREE.Vector3(0, 0, 0));
	//camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 1, 10000 );


	transformControls = new THREE.OrbitControls( camera);

        
        transformControls.rotateSpeed = 1.0;
        transformControls.zoomSpeed = 1.2;
        transformControls.panSpeed = 0.8;
        transformControls.noZoom = false;
        transformControls.noPan = false;
        transformControls.staticMoving = false;
        transformControls.dynamicDampingFactor = 0.3;
        transformControls.keys = [ 65, 83, 68 ];
		transformControls.addEventListener('change', render);
	/*controls = new THREE.TrackballControls(camera);

	controls.rotateSpeed = 1.0;
	controls.zoomSpeed = 1.2;
	controls.panSpeed = 0.8;

	controls.noZoom = false;
	controls.noPan = false;

	controls.staticMoving = false;
	controls.dynamicDampingFactor = 0.3;

	controls.keys = [65, 83, 68];

	controls.addEventListener('change', render);
	controls.target = new THREE.Vector3(0, 0, 0);*/

	/*controls.object.position.z = 0;
	controls.object.position.y = 2000;
	controls.object.target = new THREE.Vector3(0,0,0);*/

	// world

	scene = new THREE.Scene();

	scene.add(new THREE.AmbientLight(0x666666));

	var light = new THREE.SpotLight(0x666666, 1.5);
	light.position.set(0, 15000, 0);
	light.castShadow = false;

	light.shadowCameraNear = 200;
	light.shadowCameraFar = camera.far;
	light.shadowCameraFov = 50;

	light.shadowBias = -0.00022;
	light.shadowDarkness = 0.5;

	light.shadowMapWidth = 2048;
	light.shadowMapHeight = 2048;

	scene.add(light);

	model.position.x = 0;
	model.position.y = 0;
	model.position.z = 0;
	model.castShadow = true;
	model.receiveShadow = true;
	model.children[0].castShadow = true;
	model.children[0].receiveShadow = true;
	model.children[0].children[0].castShadow = true;
	model.children[0].children[0].receiveShadow = true;
	//change worm's position to fit the starting position in SOFA. When starting the simulation, this transformation will be removed.
	model2.position.x = 440;
	model2.position.y = -15;
	model2.position.z = 20;
	model2.rotation.y = 3.1419;
	model2.castShadow = true;
	model2.receiveShadow = true;
	//model2.children[1].material = new THREE.MeshLambertMaterial( { color: Math.random() * 0xffffff } );
	//model2.children[1].material.skinning = true;

	//model2.children[1] = new THREE.SkinnedMesh(model2.children[1].geometry, new THREE.MeshLambertMaterial( { color: Math.random() * 0xffffff } ), false);
	//model2.children[2] = new THREE.SkinnedMesh(model2.children[2].geometry, new THREE.MeshLambertMaterial( { color: Math.random() * 0xffffff } ), false);
	scene.add(model);
	scene.add(model2);
	//scene.add(model3);
	objects.push(model);
	objects.push(model2);

	/*plane = new THREE.Mesh( new THREE.PlaneGeometry( 2000, 2000, 8, 8 ), new THREE.MeshBasicMaterial( { color: 0x000000, opacity: 0.25, transparent: true, wireframe: true } ) );
	plane.visible = false;
	scene.add( plane );*/

	// renderer

	renderer = new THREE.WebGLRenderer({
			antialias : false
		});
	renderer.setClearColor(0xf0f0f0);
	var screenDom = document.getElementById("visualizationScreenLocomotion");
	renderer.setSize(screenDom.clientWidth, screenDom.clientHeight);

	
	renderer.sortObjects = false;
	renderer.shadowMapEnabled = true;
	renderer.shadowMapType = THREE.PCFShadowMap;

	container = document.createElement('div');
	document.getElementById("visualizationScreenLocomotion").appendChild(container);
	container.appendChild(renderer.domElement);

	//

	window.addEventListener('resize', onWindowResize, false);
	renderer.domElement.addEventListener('mousemove', onDocumentMouseMove, false);
	renderer.domElement.addEventListener('mousedown', onDocumentMouseDown, false);
	renderer.domElement.addEventListener('mouseup', onDocumentMouseUp, false);
	window.addEventListener('keypress', onKeyPress);
	window.addEventListener('keyup', onKeyUp);

	//

	render();

}

function onWindowResize() {

	camera.aspect = window.innerWidth / window.innerHeight;
	camera.updateProjectionMatrix();

	var screenDom = document.getElementById("visualizationScreenLocomotion");
	renderWidth = screenDom.clientWidth;
	renderHeight = screenDom.clientHeight;
	renderer.setSize(renderWidth, renderHeight);

	//controls.handleResize();

	render();

}

function onKeyPress(event) {}

function onKeyUp(event) {
	if (event.keyCode == 82) {
		transformControls.reset();
		//controls.reset();
	}
}

function onDocumentMouseMove(event) {}

function onDocumentMouseDown(event) {}

function onDocumentMouseUp(event) {
	if (!event.ctrlKey) {
		return;
	}
	else{
		return;
	}
	event.preventDefault();

	mouse.x = ((event.offsetX) / renderWidth) * 2 - 1;
	mouse.y =  - ((event.offsetY) / renderHeight) * 2 + 1;

	var vector = new THREE.Vector3(mouse.x, mouse.y, 0.5);
	vector.unproject(camera);

	var raycaster = new THREE.Raycaster(camera.position, vector.sub(camera.position).normalize());

	var intersects = raycaster.intersectObjects(objects, true);
	console.log(intersects);
	if (intersects.length > 0) {

		for (var i = 0; i < intersects.length; i++) {
			if (intersects[i].object.name == '') {
				var myIntersect = intersects[i];
				if (obstacleType == obstacleEnum.CUBE) {
					var manager = new THREE.LoadingManager();
					var loader = new THREE.OBJLoader(manager);
					loader.load(staticPath + 'data/cube.obj', function (object) {
						object.children[0].material = new THREE.MeshLambertMaterial({
								color : 0x00CCA3
							});
						object.children[0].castShadow = true;
						object.position.x = myIntersect.point.x;
						object.position.y = myIntersect.point.y + 50;
						object.position.z = myIntersect.point.z;
						object.scale.x = 60;
						object.scale.y = 60;
						object.scale.z = 60;

						object.castShadow = true;
						object.receiveShadow = true;
						scene.add(object);
						cubes.push(object.position.x / 10);
						cubes.push(8.35);
						cubes.push(object.position.z / 10);
						render();
						return;

					});
					return;
				} else if (obstacleType == obstacleEnum.CYLINDER) {
					var manager = new THREE.LoadingManager();
					var loader = new THREE.OBJLoader(manager);
					loader.load(staticPath + 'data/cylinder.obj', function (object) {
						object.children[0].material = new THREE.MeshLambertMaterial({
								color : 0x00CCA3
							});
						object.children[0].castShadow = true;
						object.position.x = myIntersect.point.x;
						object.position.y = myIntersect.point.y;
						object.position.z = myIntersect.point.z;
						object.scale.x = 20;
						object.scale.y = 20;
						object.scale.z = 20;

						object.castShadow = true;
						object.receiveShadow = true;
						scene.add(object);
						cylinders.push(object.position.x / 10);
						cylinders.push(8.35);
						cylinders.push(object.position.z / 10);
						render();
						return;

					});
					return;
				} else if (obstacleType == obstacleEnum.HEXAGONAL) {
					var manager = new THREE.LoadingManager();
					var loader = new THREE.OBJLoader(manager);
					loader.load(staticPath + 'data/prisma.obj', function (object) {
						object.children[0].material = new THREE.MeshLambertMaterial({
								color : 0x00CCA3
							});
						object.children[0].castShadow = true;
						object.position.x = myIntersect.point.x;
						object.position.y = myIntersect.point.y;
						object.position.z = myIntersect.point.z;
						object.rotation.x = -1.5708;
						object.scale.x = 3;
						object.scale.y = 3;
						object.scale.z = 3;

						object.castShadow = true;
						object.receiveShadow = true;
						scene.add(object);
						hexagonals.push(object.position.x / 10);
						hexagonals.push(8.35);
						hexagonals.push(object.position.z / 10);
						render();
						return;

					});
					return;
				}

			}
		}
	}
}

function goToAnimation(time) {
	
	//line in the event timeline
	var c=document.getElementById("timeCanvas");
	var ctx=c.getContext("2d");
	
	ctx.clearRect(timeRectPos-10,0,20,330);
	
	timeRectPos = time*ctx.canvas.clientWidth/experimentDuration;
	ctx.fillStyle="#FF0000";
	console.log(ctx);
	ctx.fillRect(timeRectPos,0,2,330);

	//worm joint positions
	var positions = [];
	for (var i = 0; i < locomotion[currentStep].x.length; i += 3) {
		var myPosition = [0, 0, 0];
		myPosition[0] = locomotion[currentStep].x[i] + (locomotion[currentStep + 1].x[i] - locomotion[currentStep].x[i]) * timeFromCurrentStep / timeStep;
		myPosition[1] = locomotion[currentStep].x[i + 1] + (locomotion[currentStep + 1].x[i + 1] - locomotion[currentStep].x[i + 1]) * timeFromCurrentStep / timeStep;
		myPosition[2] = locomotion[currentStep].x[i + 2] + (locomotion[currentStep + 1].x[i + 2] - locomotion[currentStep].x[i + 2]) * timeFromCurrentStep / timeStep;

		positions[parseInt(i / 3)] = myPosition;
	}
	for (var i = 1; i < 25; i++) {
		objects = [];
		var name;
		scene.traverse(function (object) {
			name = "joint";
			var num = i-1;
			name += num.toString();
			if (object.name === name)
				objects[objects.length] = object;
			// do what you want with it.

		});
		for (var j = 0; j < objects.length; j++) {
			objects[j].position.x = 10.5 * (positions[i-1][0]) / wormScale;
			//objects[j].position.y = 10.5 * (positions[i-1][1]) / wormScale;
			objects[j].position.y = -3.3;
			objects[j].position.z = 10.5 * (positions[i-1][2]) / wormScale;
			
			/*if(i==1) objects[j].position.y += 0.03;
			if(i==12) objects[j].position.y += 0.15;*/
			var vec;
			
			if (i == 1) {
				vec = new THREE.Vector3(positions[1][0] - positions[0][0], positions[1][1] - positions[0][1], positions[1][2] - positions[0][2]);
			} else if (i == 24) {
				vec = new THREE.Vector3(positions[23][0] - positions[22][0], positions[23][1] - positions[22][1], positions[23][2] - positions[22][2]);
			} else {
				vec = new THREE.Vector3(positions[i][0] - positions[i - 2][0],positions[i][1] - positions[i - 2][1], positions[i][2] - positions[i - 2][2]);
			}


			vec.normalize();
			/*var auxVec = new THREE.Vector3(0,0,-1);
			
			var angleQuaternion = new THREE.Quaternion();
			angleQuaternion.setFromUnitVectors(auxVec,vec);
			
			objects[j].rotation.setFromQuaternion(angleQuaternion,"XYZ");*/

			var angle = Math.acos(-vec.z);

			if(vec.x >= 0){
				objects[j].rotation.y = 6.28318 - angle;
			}
			else{
				objects[j].rotation.y = angle;
			}
			
			//objects[j].rotation.z = Math.acos(Math.sqrt(vec.x*vec.x + vec.z*vec.z));
		}

	}
}

function animate() {
	var wasRunningAnimation = isRunningAnimation;
	if (isRunningAnimation) {
		isRunningAnimation = false;
		var now = Date.now();
		var time = lastTime2 + (now - lastTime) * 0.0005 * playingVelocity;
		console.log(time);
		for (var i = 0; i < locomotion.length; i++) {
			if (time < parseFloat(locomotion[i].t)) {
				currentStep = i - 1;
				timeFromCurrentStep = time - parseFloat(locomotion[i - 1].t);
				isRunningAnimation = true;
				break;
			}
		}
		timeSlider.setValue(time);
		lastTime2 = time;
		lastTime = now;
		
	}

	if (isRunningAnimation) {
		goToAnimation(time);
	} else {
		var button = document.getElementById("playPauseButton");
		button.innerHTML = "Play";
		if(wasRunningAnimation){
			timeSlider.setValue(0.0);
		}
	}

	requestAnimationFrame(animate);
	render();
	//controls.update();
	transformControls.update();

}

function render() {

	renderer.render(scene, camera);

}

//loads timeline data to display in it vis.js
function callTimeline(){
	var csrftoken = $.cookie('csrftoken');
	$.ajax({
		url : behavExp_path,
		cache : false,
		type : "GET", 
		contentType : "application/json; charset=utf-8",
		dataType : "json",
		success : function (msg) {
			if (msg) {
				loadTimeline(msg.experimentDefinition);
			} 
			else {
			}
		},
		beforeSend : function (xhr) {
			xhr.setRequestHeader('X-CSRFToken', csrftoken);
			//xhr.setRequestHeader('X-CSRFToken', $('meta[name="csrf-token"]').attr('content'));
			//xhr.setRequestHeader("Authorization", "Basic " + btoa("admin" + ":" + "admin"));
			//xhr.setRequestHeader("Content-Type", "application/json");
		},
});
}

function loadTimeline(experiment){
	var visActions = [];
	var self = this;
		var options = {
			editable : false,
			snap : function (date, scale, step) {
				var hour = 100;
				return Math.round(date / hour) * hour;
			},
			height : '12em',
			showMajorLabels : false,
			moveable : false,
			start : new Number(0),
			end : new Number(experiment.experimentDuration),
		};
		if(experiment.interactionAtSpecificTime){
			for(var i = 0; i < experiment.interactionAtSpecificTime.length; i++){
				var action = {
					'id' : "exact" + experiment.interactionAtSpecificTime[i].id + "_" + i,
					'start' : experiment.interactionAtSpecificTime[i].eventTime,
					'content' : experiment.interactionAtSpecificTime[i].description,
					'type' : 'box',
					'eventType' : 'exact',
					'eventSubType' : experiment.interactionAtSpecificTime[i].experimentCategory,
				}
				visActions[visActions.length] = action;
			}
		}
		
		if(experiment.interactionFromt0tot1){
			for(var i = 0; i < experiment.interactionFromt0tot1.length; i++){
				var action = {
					'id' : "inter" + experiment.interactionFromt0tot1[i].id + "_" + i,
					'start' : experiment.interactionFromt0tot1[i].eventStartTime,
					'end' : experiment.interactionFromt0tot1[i].eventStopTime,
					'content' : experiment.interactionFromt0tot1[i].description,
					'eventType' : 'interval',
					'eventSubType' : experiment.interactionFromt0tot1[i].experimentCategory,
				}
				visActions[visActions.length] = action;
			}
		}
		
		if(experiment.experimentWideConf){
			for(var i = 0; i < experiment.experimentWideConf.length; i++){
				var action = {
					
					'id' : "perma" + experiment.experimentWideConf[i].id + "_" + i,
					'start' : -100000000000000,
					'end' : 100000000000000,
					'content' :  experiment.experimentWideConf[i].description,
					'eventType' : 'permanent',
					'eventSubType' : experiment.experimentWideConf[i].experimentCategory,
				}
				visActions[visActions.length] = action;
			}
		}
		var data = new vis.DataSet(visActions);


		// create the timeline
		var timelineContainer = this.$("#visualizationTimelineLocomotion");
		var timeline = new vis.Timeline(timelineContainer[0], data, options);

}

function readFile() {

	var file = results_path + 'sources.list';

	$.ajax({
		type : "GET",
		url : file,
		async : true,
		success : function (data) {
			var aux = data.split("\n");
			//var aux = data.split(/\r?\n/);
			for (var i = 0; i < aux.length; i++) {
				//console.log(aux[i]);
				if (aux[i] != "") {
					$.ajax({
						type : "GET",
						url : results_path + aux[i],
						async : true,
						success : function (data2) {
							var myData;
							if (typeof data2 === 'string' || data2 instanceof String){
								myData = JSON.parse(data2);
							}
							else{
								myData = data2;
							}
							//asynchronous: they may not come in order
							var A = false;
							for (var i = 0; i < locomotion.length; i++) {
								if (locomotion[i].t > myData[0].t) {
									locomotion.splice.apply(locomotion, [i, 0].concat(myData));
									A = true;
									break;
								}
							}
							if (!A) {
								locomotion = locomotion.concat(myData);
							}

							experimentDuration = locomotion.length * timeStep;
							timeSlider.setAttribute('max', experimentDuration);
							//timeSlider.refresh();
						},
						error : function (response) {
							//console.log('error');
							//console.log(response);
						},
						complete : function (response) {
							//console.log('complete');
							//console.log(response);
						}
					});
				}
			}
		}
	});

	return;
}

function changeObstacleType(index) {
	if (index == 0) {
		document.getElementById("buttonCubes").className = "btn btn-primary btn-lg active";
		document.getElementById("buttonCylinders").className = "btn btn-default btn-lg active";
		document.getElementById("buttonHexagonal").className = "btn btn-default btn-lg active";
		obstacleType = obstacleEnum.CUBE;
	} else if (index == 1) {
		document.getElementById("buttonCubes").className = "btn btn-default btn-lg active";
		document.getElementById("buttonCylinders").className = "btn btn-primary btn-lg active";
		document.getElementById("buttonHexagonal").className = "btn btn-default btn-lg active";
		obstacleType = obstacleEnum.CYLINDER;
	} else if (index == 2) {
		document.getElementById("buttonCubes").className = "btn btn-default btn-lg active";
		document.getElementById("buttonCylinders").className = "btn btn-default btn-lg active";
		document.getElementById("buttonHexagonal").className = "btn btn-primary btn-lg active";
		obstacleType = obstacleEnum.HEXAGONAL;
	}
}

function changeEnvironmentType(index) {
	if (index == 0) {
		document.getElementById("buttonWater").className = "btn btn-primary btn-lg active";
		document.getElementById("buttonGelatin").className = "btn btn-default btn-lg active";
		document.getElementById("buttonAgar").className = "btn btn-default btn-lg active";
		obstacleType = obstacleEnum.WATER;
	} else if (index == 1) {
		document.getElementById("buttonWater").className = "btn btn-default btn-lg active";
		document.getElementById("buttonGelatin").className = "btn btn-primary btn-lg active";
		document.getElementById("buttonAgar").className = "btn btn-default btn-lg active";
		obstacleType = obstacleEnum.GELATIN;
	} else if (index == 2) {
		document.getElementById("buttonWater").className = "btn btn-default btn-lg active";
		document.getElementById("buttonGelatin").className = "btn btn-default btn-lg active";
		document.getElementById("buttonAgar").className = "btn btn-primary btn-lg active";
		obstacleType = obstacleEnum.AGAR;
	}
}

function changeExperiment(val) {
	if (val == 0) {
		document.getElementById("experimentButton").innerHTML = "Touch";
	} else if (val == 1) {
		document.getElementById("experimentButton").innerHTML = "Toxic";
	} else if (val == 2) {
		document.getElementById("experimentButton").innerHTML = "Plate Tapping";
	}
}

function changeTouch1(val) {
	if (val == 0) {
		document.getElementById("touchButton1").innerHTML = "Gentle";
	} else if (val == 1) {
		document.getElementById("touchButton1").innerHTML = "Harsh";
	}
}

function changeTouch2(val) {
	if (val == 0) {
		document.getElementById("touchButton2").innerHTML = "Gentle";
	} else if (val == 1) {
		document.getElementById("touchButton2").innerHTML = "Harsh";
	}
}

function playPauseAnimation() {
	var button = document.getElementById("playPauseButton");
	if (button.innerHTML == "Play") {
		lastTime = Date.now();
		lastTime2 = timeSlider.getValue();
		button.innerHTML = "Pause";
		isRunningAnimation = true;
	} else {
		button.innerHTML = "Play";
		isRunningAnimation = false;
	}

}