/**
 * @author mrdoob / http://mrdoob.com/
 */
var Viewport = function ( editor, updateCb, selectionCb ) {

	var signals = editor.signals;

	var container = new UI.Panel();
	container.setId( 'viewport' );
	container.setPosition( 'absolute' );	

	var scene = editor.scene;
	var sceneHelpers = editor.sceneHelpers;

	var objects = [];

	// helpers

	//var grid = new THREE.GridHelper( 500, 25 );
	//sceneHelpers.add( grid );

	//

	var camera = new THREE.PerspectiveCamera(70, window.innerWidth / window.innerHeight, 1, 100000);
        camera.position.z = 500;
        camera.position.y = 3000;
        camera.lookAt(new THREE.Vector3(0, 0, 0));
        
	//

	var selectionBox = new THREE.BoxHelper();
	selectionBox.material.depthTest = false;
	selectionBox.material.transparent = true;
	selectionBox.visible = false;
	sceneHelpers.add( selectionBox );
        
        //controls
        

	var transformControls = new THREE.OrbitControls( camera, container.dom );
	transformControls.addEventListener( 'change', render );
	transformControls.addEventListener( 'mouseDown', function () {

		transformControls.enabled = false;

	} );
	transformControls.addEventListener( 'mouseUp', function () {

		signals.objectChanged.dispatch( transformControls.object );
		transformControls.enabled = true;

	} );
        
        transformControls.rotateSpeed = 1.0;
        transformControls.zoomSpeed = 1.2;
        transformControls.panSpeed = 0.8;
        transformControls.noZoom = false;
        transformControls.noPan = false;
        transformControls.staticMoving = false;
        transformControls.dynamicDampingFactor = 0.3;
        transformControls.keys = [ 65, 83, 68 ];
        transformControls.target = new THREE.Vector3(0,-200,0);

	//sceneHelpers.add( transformControls );

	// fog

	var oldFogType = "None";
	var oldFogColor = 0xaaaaaa;
	var oldFogNear = 1;
	var oldFogFar = 5000;
	var oldFogDensity = 0.00025;

	// object picking

	var raycaster = new THREE.Raycaster();
	var mouse = new THREE.Vector2();

	// events

	var getIntersects = function ( point, object ) {

		mouse.set( ( point.x * 2 ) - 1, - ( point.y * 2 ) + 1 );

		raycaster.setFromCamera( mouse, camera );

		if ( object instanceof Array ) {

			return raycaster.intersectObjects( object );

		}

		return raycaster.intersectObject( object );

	};

	var onDownPosition = new THREE.Vector2();
	var onUpPosition = new THREE.Vector2();
	var onDoubleClickPosition = new THREE.Vector2();

	var getMousePosition = function ( dom, x, y ) {

		var rect = dom.getBoundingClientRect();
		return [ ( x - rect.left ) / rect.width, ( y - rect.top ) / rect.height ];

	};

	var handleClick = function () {
                var controller = App.__container__.lookup("controller:experiment");
                var proxySend = jQuery.proxy(controller.send,controller);
                proxySend('changeToEnvironment');
		if ( onDownPosition.distanceTo( onUpPosition ) == 0 ) {

			var intersects = getIntersects( onUpPosition, objects );

			if ( intersects.length > 0 ) {

				var object = intersects[ 0 ].object;

				if ( object.userData.object !== undefined ) {

					// helper

					editor.select( object.userData.object );
                                        //selectionCb(object);

				} else {

					editor.select( object );
                                        //selectionCb(object);

				}

			} else {

				editor.select( null );
                                //selectionCb(null);

			}

			render();

		}

	};

	var onMouseDown = function ( event ) {

		event.preventDefault();

		var array = getMousePosition( container.dom, event.clientX, event.clientY );
		onDownPosition.fromArray( array );

		document.addEventListener( 'mouseup', onMouseUp, false );

	};

	var onMouseUp = function ( event ) {

		var array = getMousePosition( container.dom, event.clientX, event.clientY );
		onUpPosition.fromArray( array );

		handleClick();

		document.removeEventListener( 'mouseup', onMouseUp, false );

	};

	var onTouchStart = function ( event ) {

		var touch = event.changedTouches[ 0 ];

		var array = getMousePosition( container.dom, touch.clientX, touch.clientY );
		onDownPosition.fromArray( array );

		document.addEventListener( 'touchend', onTouchEnd, false );

	};

	var onTouchEnd = function ( event ) {

		var touch = event.changedTouches[ 0 ];

		var array = getMousePosition( container.dom, touch.clientX, touch.clientY );
		onUpPosition.fromArray( array );

		handleClick();

		document.removeEventListener( 'touchend', onTouchEnd, false );

	};

	var onDoubleClick = function ( event ) {

		var array = getMousePosition( container.dom, event.clientX, event.clientY );
		onDoubleClickPosition.fromArray( array );

		var intersects = getIntersects( onDoubleClickPosition, objects );

		if ( intersects.length > 0 ) {

			var intersect = intersects[ 0 ];

			signals.objectFocused.dispatch( intersect.object );

		}

	};

	container.dom.addEventListener( 'mousedown', onMouseDown, false );
	container.dom.addEventListener( 'touchstart', onTouchStart, false );
	container.dom.addEventListener( 'dblclick', onDoubleClick, false );

	// controls need to be added *after* main logic,
	// otherwise controls.enabled doesn't work.

	var controls = new THREE.EditorControls( camera, container.dom );
	controls.center.fromArray( editor.config.getKey( 'camera/target' ) );
	controls.addEventListener( 'change', function () {

		transformControls.update();                
		signals.cameraChanged.dispatch( camera );

	} );

	// signals

	signals.editorCleared.add( function () {

		controls.center.set( 0, 0, 0 );
		render();

	} );

	signals.themeChanged.add( function ( value ) {

		renderer.setClearColor( 0xaaaaaa );

		render();

	} );

	signals.transformModeChanged.add( function ( mode ) {

		transformControls.setMode( mode );

	} );

	signals.snapChanged.add( function ( dist ) {

		transformControls.setSnap( dist );

	} );

	signals.spaceChanged.add( function ( space ) {

		transformControls.setSpace( space );

	} );

	signals.rendererChanged.add( function ( type, antialias ) {

		container.dom.removeChild( renderer.domElement );

		renderer = createRenderer( type, antialias );
		renderer.setClearColor( clearColor );
		renderer.setPixelRatio( window.devicePixelRatio );
		renderer.setSize( container.dom.offsetWidth, container.dom.offsetHeight );

		container.dom.appendChild( renderer.domElement );

		render();

	} );

	signals.sceneGraphChanged.add( function () {
		render();
	} );

	var saveTimeout;

	signals.cameraChanged.add( function () {

		render();

	} );

	signals.objectSelected.add( function ( object ) {

		selectionBox.visible = false;
		transformControls.detach();

		if ( object !== null ) {

			if ( object.geometry !== undefined &&
				 object instanceof THREE.Sprite === false ) {

				selectionBox.update( object );
				selectionBox.visible = true;

			}

			transformControls.attach( object );

		}
                selectionCb(object);
		render();

	} );

	signals.objectFocused.add( function ( object , camera) {

		controls.focus( object , camera);

	} );

	signals.geometryChanged.add( function ( geometry ) {

		selectionBox.update( editor.selected );

		render();               

	} );

	signals.objectAdded.add( function ( object ) {

		var materialsNeedUpdate = false;

		object.traverse( function ( child ) {

			if ( child instanceof THREE.Light ) materialsNeedUpdate = true;

			objects.push( child );

		} );
                updateCb(object);
		if ( materialsNeedUpdate === true ) updateMaterials();

	} );

	signals.objectChanged.add( function ( object ) {

		transformControls.update();

		if ( object.geometry !== undefined ) {

			selectionBox.update( object );

		}

		if ( object instanceof THREE.PerspectiveCamera ) {

			object.updateProjectionMatrix();

		}

		if ( editor.helpers[ object.id ] !== undefined ) {

			editor.helpers[ object.id ].update();

		}
                updateCb(object);//added by Javi
		render();

	} );

	signals.objectRemoved.add( function ( object ) {

		var materialsNeedUpdate = false;
                updateCb(object);
		object.traverse( function ( child ) {

			if ( child instanceof THREE.Light ) materialsNeedUpdate = true;

			objects.splice( objects.indexOf( child ), 1 );

		} );
                
		if ( materialsNeedUpdate === true ) updateMaterials();

	} );

	

	signals.materialChanged.add( function ( material ) {

		render();

	} );

	signals.fogTypeChanged.add( function ( fogType ) {

		if ( fogType !== oldFogType ) {

			if ( fogType === "None" ) {

				scene.fog = null;

			} else if ( fogType === "Fog" ) {

				scene.fog = new THREE.Fog( oldFogColor, oldFogNear, oldFogFar );

			} else if ( fogType === "FogExp2" ) {

				scene.fog = new THREE.FogExp2( oldFogColor, oldFogDensity );

			}

			updateMaterials();

			oldFogType = fogType;

		}

		render();

	} );

	signals.fogColorChanged.add( function ( fogColor ) {

		oldFogColor = fogColor;

		updateFog( scene );

		render();

	} );

	signals.fogParametersChanged.add( function ( near, far, density ) {

		oldFogNear = near;
		oldFogFar = far;
		oldFogDensity = density;

		updateFog( scene );

		render();

	} );

	signals.windowResize.add( function () {

		camera.aspect = container.dom.offsetWidth / container.dom.offsetHeight;
		camera.updateProjectionMatrix();

		renderer.setSize( container.dom.offsetWidth, container.dom.offsetHeight );

		render();

	} );
	
	signals.cubeSide1Changed.add( function (value,id) {
		changeSide1Cube(value,id);
		render();

	} );
	
	signals.cubeSide2Changed.add( function (value,id) {
		changeSide2Cube(value,id);
		render();

	} );
	
	signals.cubeDepthChanged.add( function (value,id) {
		changeDepthCube(value,id);
		render();

	} );
	
	signals.cylinderLengthChanged.add( function (value,id) {
		changeLengthCylinder(value,id);
		render();

	} );
	
	signals.cylinderRadiusChanged.add( function (value,id) {
		changeRadiusCylinder(value,id);
		render();

	} );
	
	signals.prismDepthChanged.add( function (value,id) {
		changeDepthPrism(value,id);
		render();

	} );
	
	signals.prismSideChanged.add( function (value,id) {
		changeSidePrism(value,id);
		render();

	} );
	
	signals.wormXChanged.add( function (value) {
		moveXWorm(value);
		render();

	} );
	
	signals.wormYChanged.add( function (value) {
		moveYWorm(value);
		render();

	} );
	
	signals.obstacleXChanged.add( function (value,id) {
		moveXObstacle(value,id);
		render();

	} );
	
	signals.obstacleYChanged.add( function (value,id) {
		moveYObstacle(value,id);
		render();

	} );
	
	signals.wormAngleChanged.add( function (value) {
		moveAngleWorm(value);
		render();

	} );

	signals.showGridChanged.add( function ( showGrid ) {

		grid.visible = showGrid;
		render();

	} );
	

	var createRenderer = function ( type, antialias ) {

		if ( type === 'WebGLRenderer' && System.support.webgl === false ) {

			type = 'CanvasRenderer';

		}

		var renderer = new THREE[ type ]( { antialias: antialias } );
                renderer.setClearColor( clearColor );
		renderer.setPixelRatio( window.devicePixelRatio );
		renderer.autoClear = false;
		renderer.autoUpdateScene = false;                
		return renderer;

	};

	var clearColor;
	var renderer = createRenderer( editor.config.getKey( 'renderer' ), editor.config.getKey( 'renderer/antialias' ) );      
	container.dom.appendChild( renderer.domElement );
        
	
        

	function updateMaterials() {

		editor.scene.traverse( function ( node ) {

			if ( node.material ) {

				node.material.needsUpdate = true;

				if ( node.material instanceof THREE.MeshFaceMaterial ) {

					for ( var i = 0; i < node.material.materials.length; i ++ ) {

						node.material.materials[ i ].needsUpdate = true;

					}

				}

			}

		} );

	}

	function updateFog( root ) {

		if ( root.fog ) {

			root.fog.color.setHex( oldFogColor );

			if ( root.fog.near !== undefined ) root.fog.near = oldFogNear;
			if ( root.fog.far !== undefined ) root.fog.far = oldFogFar;
			if ( root.fog.density !== undefined ) root.fog.density = oldFogDensity;

		}

	}

	

	function render() {

		sceneHelpers.updateMatrixWorld();
		scene.updateMatrixWorld();

		renderer.clear();
		renderer.render( scene, camera );

		if ( renderer instanceof THREE.RaytracingRenderer === false ) {

			renderer.render( sceneHelpers, camera );

		}

	}
	
	function changeSide1Cube(value,id) {
		for(var i = 0; i < scene.children.length; i++){
			if(scene.children[i].uuid == id){
				var controller = App.__container__.lookup("controller:experiment");
				var probetaScale = controller.get('probetaScale');
				scene.children[i].scale.x = 0.1*value;
			}
		}
	}
	
	function changeSide2Cube(value,id) {
		for(var i = 0; i < scene.children.length; i++){
			if(scene.children[i].uuid == id){
				var controller = App.__container__.lookup("controller:experiment");
				var probetaScale = controller.get('probetaScale');
				scene.children[i].scale.z = 0.1*value;
			}
		}
	}
	
	function changeDepthCube(value,id) {
		for(var i = 0; i < scene.children.length; i++){
			if(scene.children[i].uuid == id){
				var controller = App.__container__.lookup("controller:experiment");
				var probetaScale = controller.get('probetaScale');
				scene.children[i].scale.y = 0.1*value;
				scene.children[i].position.y = scene.children[i].scale.y*50 - probetaScale*180;
			}
		}
	}
	
	function changeLengthCylinder(value,id) {
		for(var i = 0; i < scene.children.length; i++){
			if(scene.children[i].uuid == id){
				var controller = App.__container__.lookup("controller:experiment");
				var probetaScale = controller.get('probetaScale');
				scene.children[i].scale.z = 10*value;
				scene.children[i].position.y = scene.children[i].scale.z - probetaScale*180;
			}
		}
	}
	
	function changeRadiusCylinder(value,id) {
		for(var i = 0; i < scene.children.length; i++){
			if(scene.children[i].uuid == id){
				var controller = App.__container__.lookup("controller:experiment");
				var probetaScale = controller.get('probetaScale');
				scene.children[i].scale.x = 10*value;
				scene.children[i].scale.y = 10*value;
			}
		}
	}
	
	function changeDepthPrism(value,id) {
		for(var i = 0; i < scene.children.length; i++){
			if(scene.children[i].uuid == id){
				var controller = App.__container__.lookup("controller:experiment");
				var probetaScale = controller.get('probetaScale');
				scene.children[i].scale.z = 0.05*value;
				scene.children[i].position.y = scene.children[i].scale.z*600  - probetaScale*180;
			}
		}
	}
	
	function changeSidePrism(value,id) {
		for(var i = 0; i < scene.children.length; i++){
			if(scene.children[i].uuid == id){
				var controller = App.__container__.lookup("controller:experiment");
				var probetaScale = controller.get('probetaScale');
				scene.children[i].scale.x = 0.05*value;
				scene.children[i].scale.y = 0.05*value;
			}
		}
	}
	
	function moveYObstacle(value,id) {
		for(var i = 0; i < scene.children.length; i++){
			if(scene.children[i].uuid == id){
				var controller = App.__container__.lookup("controller:experiment");
				var probetaScale = controller.get('probetaScale');
				scene.children[i].position.z = probetaScale*28*value;
			}
		}
	}
	
	function moveXObstacle(value,id) {
		for(var i = 0; i < scene.children.length; i++){
			if(scene.children[i].uuid == id){
				var controller = App.__container__.lookup("controller:experiment");
				var probetaScale = controller.get('probetaScale');
				scene.children[i].position.x = probetaScale*28*value;
			}
		}
	}
	
	function moveYWorm(value) {
		var controller = App.__container__.lookup("controller:experiment");
		var probetaScale = controller.get('probetaScale');
		scene.children[7].position.z = probetaScale*28*value;
	}
	
	function moveXWorm(value) {
		var controller = App.__container__.lookup("controller:experiment");
		var probetaScale = controller.get('probetaScale');
		scene.children[7].position.x = probetaScale*28*value;
	}
	
	function moveAngleWorm(value) {
		scene.children[7].rotation.y = value;
	}
	return [container, renderer, camera, transformControls, signals];

}
