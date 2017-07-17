App.ExperimentView = Ember.View.extend({
    classNames:["wrap", "row"],
    //controller: App.StateScene3dController.create(),
	willInsertElement: function(){
		var self = this;
			var CloneBehExpInfo = {
				"behaviouralExperiment" : this.get('controller.model.id'),
			};
			var csrftoken = $.cookie('csrftoken');
			$.ajax({
				url : cloneBehExpPath,
				cache : false,
				type : "POST", //type:"POST"
				data : JSON.stringify(CloneBehExpInfo),
				contentType : "application/json; charset=utf-8",
				dataType : "json",
				success : function (msg) {
					if (msg) {
						if (msg.clone == 0) {
							self.set('controller.hasToBeCloned',false);
						} else {
							self.set('controller.hasToBeCloned',true);
						}

					} else {
						self.set('controller.hasToBeCloned',true);
					}
				},
				beforeSend : function (xhr) {
					xhr.setRequestHeader('X-CSRFToken', csrftoken);
					//xhr.setRequestHeader('X-CSRFToken', $('meta[name="csrf-token"]').attr('content'));
					//xhr.setRequestHeader("Authorization", "Basic " + btoa("admin" + ":" + "admin"));
					//xhr.setRequestHeader("Content-Type", "application/json");
				},
			});
	},
    didInsertElement: function() {
		$('#modalLoading').modal('show');
        var self = this;
        var editor = new Editor(); 
        var controller = this.get('controller');     
        var scene = this.get("controller.scene");
        editor.scene = scene;
        var params = new Viewport( editor, scene);
        controller.send('setParams',params);
        this.set('viewport',params[0]);
        this.set('renderer',params[1]);
        this.set('camera',params[2]);
        this.set('controls', params[3]);
        this.set('signals', params[4]);
        
        
        //Get the scene and make a setInternal in the proxy
        /*var scene = editor.scene;
        this.get('controller.model').setInternal(scene);*/
        
        //No me gusta esto, un poco chapucero
        //viewport.dom.style.zIndex =1;
        $("#visor").append(params[0].dom );
        //$(".3dcontrols").appendTo("#viewport");
        
        editor.setTheme( editor.config.getKey( 'theme' ) );
        
        //camera
  
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
        
        /*global THREE, requestAnimationFrame, Detector, dat */
        THREE.ShaderTypes = {

        'phongDiffuse' : {

                uniforms: {

                        "uDirLightPos":	{ type: "v3", value: new THREE.Vector3() },
                        "uDirLightColor": { type: "c", value: new THREE.Color( 0xffffff ) },

                        "uMaterialColor":  { type: "c", value: new THREE.Color( 0xffffff ) },

                        uKd: {
                                type: "f",
                                value: 0.7
                        },
                        uBorder: {
                                type: "f",
                                value: 0.4
                        }
                },

                vertexShader: [

                        "varying vec3 vNormal;",
                        "varying vec3 vViewPosition;",

                        "void main() {",

                                "gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );",
                                "vNormal = normalize( normalMatrix * normal );",
                                "vec4 mvPosition = modelViewMatrix * vec4( position, 1.0 );",
                                "vViewPosition = -mvPosition.xyz;",

                        "}"

                ].join("\n"),

                fragmentShader: [

                        "uniform vec3 uMaterialColor;",

                        "uniform vec3 uDirLightPos;",
                        "uniform vec3 uDirLightColor;",

                        "uniform float uKd;",
                        "uniform float uBorder;",

                        "varying vec3 vNormal;",
                        "varying vec3 vViewPosition;",

                        "void main() {",

                                // compute direction to light
                                "vec4 lDirection = viewMatrix * vec4( uDirLightPos, 0.0 );",
                                "vec3 lVector = normalize( lDirection.xyz );",

                                // diffuse: N * L. Normal must be normalized, since it's interpolated.
                                "vec3 normal = normalize( vNormal );",
                                //was: "float diffuse = max( dot( normal, lVector ), 0.0);",
                                // solution
                                "float diffuse = dot( normal, lVector );",
                                "if ( diffuse > 0.6 ) { diffuse = 1.0; }",
                                "else if ( diffuse > -0.2 ) { diffuse = 0.7; }",
                                "else { diffuse = 0.3; }",

                                "gl_FragColor = vec4( uKd * uMaterialColor * uDirLightColor * diffuse, 1.0 );",

                        "}"

                ].join("\n")

        }

        };
        
        function createShaderMaterial(id, light) {

            var shader = THREE.ShaderTypes[id];

            var u = THREE.UniformsUtils.clone(shader.uniforms);

            var vs = shader.vertexShader;
            var fs = shader.fragmentShader;

            var material = new THREE.ShaderMaterial({ uniforms: u, vertexShader: vs, fragmentShader: fs });

            material.uniforms.uDirLightPos.value = light.position;
            material.uniforms.uDirLightColor.value = light.color;

            return material;

        }
        
        // MATERIALS
        var materialColor = new THREE.Color();
        materialColor.setRGB(1.0, 0.8, 0.6);

        phongMaterial = createShaderMaterial("phongDiffuse", light );
        phongMaterial.uniforms.uMaterialColor.value.copy(materialColor);
        phongMaterial.side = THREE.DoubleSide;
        
        var onWindowResize = function ( event ) {
                editor.signals.windowResize.dispatch();
        };
        //add ambient light
        var color = 0x333333;
        var ambienLight = new THREE.AmbientLight( color );
        ambienLight.name = "ambientLight 1";
        scene.add(ambienLight);
        /*editor.addObject( light );
        editor.select( light );   */   
        
        window.addEventListener( 'resize', onWindowResize, false );
        onWindowResize();
        
    },
//    lanaUpdated: function() {
//        
//    }.observes('controller.model'), 
    willDestroyElement: function() {
       
    }            
});