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
var wormScale = 115;
var loader = new THREE.ColladaLoader();
var container, stats;
var camera, controls, scene, renderer;
var cubes = [], objects = [], plane, cylinders = [], hexagonals = [];
var runSofaDone = false;
var inDataDone = false;
var isRunning = false;
var path, webPath;
var obstacleType = obstacleEnum.CUBE;
var renderWidth;
var	renderHeight;

var mouse = new THREE.Vector2(),
offset = new THREE.Vector3(),
INTERSECTED, SELECTED;
var model, model2, model3;

loader.load( staticPath + 'data/probeta.dae', function ( collada ) {
	

	model = collada.scene;
	
	model.scale.x = model.scale.y = model.scale.z = 10; // 1/8 scale, modeled in cm
	
	model.name = "probeta";
	
	loader.load(staticPath + 'data/cuticle.dae', function ( collada2){
	
		model2 = collada2.scene;
	
		model2.scale.x = model2.scale.y = model2.scale.z = wormScale; // 1/8 scale, modeled in cm
		
		
		var maxX = -10000, minX = 10000, maxY = -10000, minY = 10000, maxZ = -10000, minZ = 10000;
		
		init();
		animate();
	});
});

function init() {
	
	//obtain the path. This way the code works in every computer.
	webPath = document.URL;
	webPath = webPath.slice(0,webPath.lastIndexOf("/"));
	$.ajax({
		type: "GET",
		url: "php/getPath.php",  
		//async: false,
		success: function(data){
			path = data;
			path = path.slice(0,path.lastIndexOf("\\"));
		}
	});
	
	//remove previous simulation file
	$.ajax({
		type: "GET",
		url: "php/removeSimulationFile.php",  
	});
	
	camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 1, 100000 );
	camera.position.z = 500;
	camera.position.y = 2000;
	camera.lookAt(new THREE.Vector3(0,0,0));
	//camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 1, 10000 );
	

	controls = new THREE.TrackballControls( camera );

	controls.rotateSpeed = 1.0;
	controls.zoomSpeed = 1.2;
	controls.panSpeed = 0.8;

	controls.noZoom = false;
	controls.noPan = false;

	controls.staticMoving = false;
	controls.dynamicDampingFactor = 0.3;

	controls.keys = [ 65, 83, 68 ];

	controls.addEventListener( 'change', render );
	controls.target = new THREE.Vector3(0,0,0);
	
	/*controls.object.position.z = 0;
	controls.object.position.y = 2000;
	controls.object.target = new THREE.Vector3(0,0,0);*/

	// world

	scene = new THREE.Scene();

	scene.add( new THREE.AmbientLight( 0x666666 ) );

	var light = new THREE.SpotLight( 0x666666, 1.5 );
	light.position.set( 0, 15000, 0 );
	light.castShadow = false;

	light.shadowCameraNear = 200;
	light.shadowCameraFar = camera.far;
	light.shadowCameraFov = 50;

	light.shadowBias = -0.00022;
	light.shadowDarkness = 0.5;

	light.shadowMapWidth = 2048;
	light.shadowMapHeight = 2048;

	scene.add( light );
		
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
	//model2.children[1].material = new THREE.MeshLambertMaterial( { color: Math.random() * 0xffffff } );
	//model2.children[1].material.skinning = true;
	
	//model2.children[1] = new THREE.SkinnedMesh(model2.children[1].geometry, new THREE.MeshLambertMaterial( { color: Math.random() * 0xffffff } ), false);
	//model2.children[2] = new THREE.SkinnedMesh(model2.children[2].geometry, new THREE.MeshLambertMaterial( { color: Math.random() * 0xffffff } ), false);
	scene.add( model );
	scene.add( model2 );
	//scene.add(model3);
	objects.push(model);
	objects.push(model2);
			

	/*plane = new THREE.Mesh( new THREE.PlaneGeometry( 2000, 2000, 8, 8 ), new THREE.MeshBasicMaterial( { color: 0x000000, opacity: 0.25, transparent: true, wireframe: true } ) );
	plane.visible = false;
	scene.add( plane );*/


	// renderer

	renderer = new THREE.WebGLRenderer( { antialias: false } );
	renderer.setClearColor( 0xf0f0f0 );
	renderer.setSize( window.innerWidth, window.innerHeight );
	
	var screenDom = document.getElementById("visor");
	renderWidth = screenDom.clientWidth - 45;
	renderHeight = screenDom.clientHeight - 30;
	renderer.setSize(renderWidth, renderHeight);
	renderer.sortObjects = false;
	renderer.shadowMapEnabled = true;
	renderer.shadowMapType = THREE.PCFShadowMap;

	container = document.createElement( 'div' );
	document.getElementById("visor").appendChild( container );
	container.appendChild( renderer.domElement );
	
	var visorLeft = 15, visorTop = 15;
	renderer.domElement.style.left = visorLeft + "px";
	renderer.domElement.style.top = visorTop + "px";
	renderer.domElement.style.position = "absolute";

	stats = new Stats();
	stats.domElement.style.position = 'absolute';
	stats.domElement.style.top = '18px';
	stats.domElement.style.left = '18px';
	container.appendChild( stats.domElement );

	//

	window.addEventListener( 'resize', onWindowResize, false );
	renderer.domElement.addEventListener( 'mousemove', onDocumentMouseMove, false );
	renderer.domElement.addEventListener( 'mousedown', onDocumentMouseDown, false );
	renderer.domElement.addEventListener( 'mouseup', onDocumentMouseUp, false );
	window.addEventListener( 'keypress', onKeyPress);
	window.addEventListener( 'keyup', onKeyUp);

	//

	render();

}

function onWindowResize() {

	camera.aspect = window.innerWidth / window.innerHeight;
	camera.updateProjectionMatrix();

	var screenDom = document.getElementById("visor");
	renderWidth = screenDom.clientWidth - 45;
	renderHeight = screenDom.clientHeight - 30;
	renderer.setSize(renderWidth, renderHeight);
	
	controls.handleResize();
	
	render();

}

function onKeyPress( event ) {

}

function onKeyUp( event ) {
	if(event.keyCode == 82){
		controls.reset();
	}
}

function onDocumentMouseMove( event ) {


}

function onDocumentMouseDown( event ) {


}

function onDocumentMouseUp( event ) {
	if(!event.ctrlKey){
		return;
	}
	event.preventDefault();

	mouse.x = ( (event.offsetX)/ renderWidth ) * 2 - 1;
	mouse.y = - ( (event.offsetY)/ renderHeight ) * 2 + 1;

	var vector = new THREE.Vector3( mouse.x, mouse.y, 0.5 );
	vector.unproject( camera );

	var raycaster = new THREE.Raycaster( camera.position, vector.sub( camera.position ).normalize() );

	var intersects = raycaster.intersectObjects( objects, true );
	console.log(intersects);
	if ( intersects.length > 0 ) {

		for(var i = 0; i < intersects.length; i++){
			if(intersects[i].object.name == ''){
				var myIntersect = intersects[i];
				if(obstacleType == obstacleEnum.CUBE){
					var manager = new THREE.LoadingManager();
					var loader = new THREE.OBJLoader( manager );
					loader.load( staticPath + 'data/cube.obj', function ( object ) {
						object.children[0].material = new THREE.MeshLambertMaterial( { color: 0x00CCA3 } );
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
						cubes.push(object.position.x/10);
						cubes.push(8.35);
						cubes.push(object.position.z/10);
						render();
						return;

					} );
					return;
				}
				else if(obstacleType == obstacleEnum.CYLINDER){
					var manager = new THREE.LoadingManager();
					var loader = new THREE.OBJLoader( manager );
					loader.load( staticPath + 'data/cylinder.obj', function ( object ) {
						object.children[0].material = new THREE.MeshLambertMaterial( { color: 0x00CCA3 } );
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
						cylinders.push(object.position.x/10);
						cylinders.push(8.35);
						cylinders.push(object.position.z/10);
						render();
						return;

					} );
					return;
				}
				else if(obstacleType == obstacleEnum.HEXAGONAL){
					var manager = new THREE.LoadingManager();
					var loader = new THREE.OBJLoader( manager );
					loader.load( staticPath + 'data/prisma.obj', function ( object ) {
						object.children[0].material = new THREE.MeshLambertMaterial( { color: 0x00CCA3 } );
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
						hexagonals.push(object.position.x/10);
						hexagonals.push(8.35);
						hexagonals.push(object.position.z/10);
						render();
						return;

					} );
					return;
				}
				
			}
		}
	}
}

function launchAnimation(){
	$.ajax({
		type: "GET",
		data: { cubes:cubes, cylinders:cylinders, hexagonals:hexagonals, path:path},
		url: "php/writeFile.php",
		success: function(data){
			console.log("scene.scn written, sofa launched");
			var timeValue = document.getElementsByName("time");
			$.ajax({
				type: "GET",
				url: "php/runSofa.php",
				data: { time:timeValue[0].value*100, path:path},
				success: function(data){
					console.log("sofa finished");
					console.log(data);
					var a = data;
					if(inDataDone){
						model2.position.x = 0;
						model2.position.y = 0;
						model2.position.z = 0;
						model2.rotation.y = 0;
						//remove root joint's translation
						objects = [];
						scene.traverse (function (object)
						{
							name = "joint0";
							if (object.name === name)
								objects[objects.length] = object;
									// do what you want with it.

						});
						objects[1].position.x = 0;
						objects[1].position.y = 0;
						objects[1].position.z = 0;
						window.alert("start simulation");
						var str = webPath + '/sofa/simulation.txt';
						readFile(str);
					}
					else{
						runSofaDone = true;
					}
				}
			});
			console.log("indata started");
			$.ajax({
				type: "GET",
				url: "php/inData.php",  
				//async: false,
				data: { time:timeValue[0].value*4},
				success: function(data){
					console.log("indata finished");
					console.log(data);
					if(runSofaDone){
						model2.position.x = 0;
						model2.position.y = 0;
						model2.position.z = 0;
						model2.rotation.y = 0;
						//remove root joint's translation
						objects = [];
						scene.traverse (function (object)
						{
							name = "joint0";
							if (object.name === name)
								objects[objects.length] = object;
									// do what you want with it.

						});
						objects[1].position.x = 0;
						objects[1].position.y = 0;
						objects[1].position.z = 0;
						window.alert("start simulation");
						var str = webPath + '/sofa/simulation.txt';
						readFile(str);
					}
					else{
						inDataDone = true;
					}
				}
			});
		}
	});
}

function animate() {
	if(isRunning){
		if(firstFrame){
			firstFrame = false;
			initialTime = Date.now();
		}
		else{
			isRunning = false;
			var time = ( Date.now() - initialTime ) * 0.0005; // seconds
			for(var i = currentStep; i < steps.length; i++){
				if(time < steps[i].time){
					currentStep = i-1;
					timeFromCurrentStep = time - steps[i-1].time;
					isRunning = true;
					break;
				}
			}
			if(!isRunning){
				return;
			}
		}
		
		var positions = [];
		for(var i = 0; i < steps[currentStep].DOFnum; i++){
			var myPosition = [0,0,0];
			myPosition[0] = steps[currentStep].getTransX(i) + steps[currentStep].getSpeedX(i)*timeFromCurrentStep;
			myPosition[1] = steps[currentStep].getTransY(i) + steps[currentStep].getSpeedY(i)*timeFromCurrentStep;
			myPosition[2] = steps[currentStep].getTransZ(i) + steps[currentStep].getSpeedZ(i)*timeFromCurrentStep;
			positions[i] = myPosition;
		}
		for(var i = 0; i < 12; i++){
			objects = [];
			var name;
			scene.traverse (function (object)
			{
				name = "joint";
				name += (i+1);
				if (object.name === name)
					objects[objects.length] = object;
						// do what you want with it.

			});
			
			
			objects[1].position.x = 5*(positions[2*i+1][0] + positions[2*i+51][0])/wormScale;
			objects[1].position.y = 5*(positions[2*i+1][1] + positions[2*i+51][1])/wormScale;
			objects[1].position.z = 5*(positions[2*i+1][2] + positions[2*i+51][2])/wormScale;
			
			//difference between last and next sphere
			var vec = new THREE.Vector3(0.5*(positions[2*i+2][0] + positions[2*i+27][0])-0.5*(positions[2*i][0] + positions[2*i+25][0]), 0.5*(positions[2*i+2][1] + positions[2*i+27][1])-0.5*(positions[2*i][1] + positions[2*i+25][1]), 0.5*(positions[2*i+2][2] + positions[2*i+27][2])-0.5*(positions[2*i][2] + positions[2*i+25][2]));
			
			//console.log(vec);
			
			vec.normalize();
			
			//console.log(vec);
			
			var angle = Math.acos(vec.z);
			
			//console.log(-angle);
			
			objects[1].rotation.y = 3.1419 + angle;
		
		}
	}
	
	requestAnimationFrame( animate );
	controls.update();

}

function render() {

	renderer.render( scene, camera );
	stats.update();

}

function readFile(path){

	var file;

	$.ajax({
		type: "GET",
		url: path ,
		async: false,
		success: function(data){
			file = data;
			var lines = file.split("\n");
			lines = lines.slice(0,lines.length -1);
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
				while( j < xTokens.length){
					num = myStep.getDOFnum();
					myStep.addDOF(num, parseFloat(String(xTokens[j])), parseFloat(String(xTokens[j+1])), parseFloat(String(xTokens[j+2])), parseFloat(String(xTokens[j+3])), parseFloat(String(xTokens[j+4])), parseFloat(String(xTokens[j+5])),parseFloat(String(xTokens[j+6])));
					j+=7;
				}
				
				//take the speeds
				i++;
				var vTokens = lines[i].split(" ");
				
				var k = 3;
				num = 0;
				while( k < vTokens.length){
					myStep.addSpeed(String(num), parseFloat(String(vTokens[k])), parseFloat(String(vTokens[k+1])), parseFloat(String(vTokens[k+2])));
					num++;
					k+=6;
				}
				
				steps[steps.length] = myStep;
				i++;
			}
		}
	});
	
	isRunning = true;
	inDataDone = false;
	
	return;
}

function changeObstacleType(index) {
	if(index == 0){
		document.getElementById("buttonCubes").className = "btn btn-primary btn-lg active";
		document.getElementById("buttonCylinders").className = "btn btn-default btn-lg active";
		document.getElementById("buttonHexagonal").className = "btn btn-default btn-lg active";
		obstacleType = obstacleEnum.CUBE;
	}
	else if (index == 1){
		document.getElementById("buttonCubes").className = "btn btn-default btn-lg active";
		document.getElementById("buttonCylinders").className = "btn btn-primary btn-lg active";
		document.getElementById("buttonHexagonal").className = "btn btn-default btn-lg active";
		obstacleType = obstacleEnum.CYLINDER;
	}
	else if (index == 2){
		document.getElementById("buttonCubes").className = "btn btn-default btn-lg active";
		document.getElementById("buttonCylinders").className = "btn btn-default btn-lg active";
		document.getElementById("buttonHexagonal").className = "btn btn-primary btn-lg active";
		obstacleType = obstacleEnum.HEXAGONAL;
	}
}

function changeEnvironmentType(index) {
	if(index == 0){
		document.getElementById("buttonWater").className = "btn btn-primary btn-lg active";
		document.getElementById("buttonGelatin").className = "btn btn-default btn-lg active";
		document.getElementById("buttonAgar").className = "btn btn-default btn-lg active";
		obstacleType = obstacleEnum.WATER;
	}
	else if (index == 1){
		document.getElementById("buttonWater").className = "btn btn-default btn-lg active";
		document.getElementById("buttonGelatin").className = "btn btn-primary btn-lg active";
		document.getElementById("buttonAgar").className = "btn btn-default btn-lg active";
		obstacleType = obstacleEnum.GELATIN;
	}
	else if (index == 2){
		document.getElementById("buttonWater").className = "btn btn-default btn-lg active";
		document.getElementById("buttonGelatin").className = "btn btn-default btn-lg active";
		document.getElementById("buttonAgar").className = "btn btn-primary btn-lg active";
		obstacleType = obstacleEnum.AGAR;
	}
}

function changeExperiment(val){
	if(val == 0){
		document.getElementById("experimentButton").innerHTML = "Touch";
	}
	else if (val == 1){
		document.getElementById("experimentButton").innerHTML = "Toxic";
	}
	else if (val == 2){
		document.getElementById("experimentButton").innerHTML = "Plate Tapping";
	}
}

function changeTouch1(val){
	if(val == 0){
		document.getElementById("touchButton1").innerHTML = "Gentle";
	}
	else if (val == 1){
		document.getElementById("touchButton1").innerHTML = "Harsh";
	}
}

function changeTouch2(val){
	if(val == 0){
		document.getElementById("touchButton2").innerHTML = "Gentle";
	}
	else if (val == 1){
		document.getElementById("touchButton2").innerHTML = "Harsh";
	}
}
