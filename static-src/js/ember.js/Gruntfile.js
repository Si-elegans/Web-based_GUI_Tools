module.exports = function (grunt) {

	grunt.initConfig({
		emberTemplates : {
			compile : {
				options : {
					amd : false,
					concatenate : false,
					templateNamespace : 'Handlebars',
					templateBasePath : "templates/",
					//templateRegistration: function(name, contents) {
					//	return "Ember.TEMPLATES[\"templates/" + name + "\"] = " + contents + ";";
					//  }
				},
				files : {
					'templates/' : 'templates/*.hbs',
				}
			},
			compile2 : {
				options : {
					amd : false,
					concatenate : false,
					templateNamespace : 'Handlebars',
					templateBasePath : "templates/subtypeTemplates",
					//templateRegistration: function(name, contents) {
					//	return "Ember.TEMPLATES[\"templates/subtypeTemplates/" + name + "\"] = " + contents + ";";
					//  }
				},
				files : {
					'templates/subtypeTemplates/' : 'templates/subtypeTemplates/*.hbs'
				}
			},
			compile3 : {
				options : {
					amd : false,
					concatenate : false,
					templateNamespace : 'Handlebars',
					templateBasePath : "templates/environmentTemplates",
					//templateRegistration: function(name, contents) {
					//	return "Ember.TEMPLATES[\"templates/subtypeTemplates/" + name + "\"] = " + contents + ";";
					//  }
				},
				files : {
					'templates/environmentTemplates/' : 'templates/environmentTemplates/*.hbs'
				}
			}
		},
		watch : {
			files : ['templates/*.hbs', 'templates/subtypeTemplates/*.hbs', 'templates/environmentTemplates/*.hbs'],
			tasks : ['compile', 'compile2', 'compile3'],
		},
		uglify : {
			options : {
				mangle : true,
			},
			my_target : {
				files : {
					'dist/sielegans-ember.min.js' : ['dist/sielegans-ember.js'],
				}
			}
		},
		concat: {
			dist: {
				src: ['app.js', 'adapter.js', '**/*.js', '!node_modules/**/*', '!dist/*', '!libs/*','!Gruntfile.js','!package.json'],
				dest: 'dist/sielegans-ember.js'
			}
		}
	});

	grunt.loadNpmTasks('grunt-ember-templates');
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-contrib-uglify');
	grunt.loadNpmTasks('grunt-contrib-concat');

	grunt.registerTask('default', ['watch']);
	grunt.registerTask('compile', 'emberTemplates:compile');
	grunt.registerTask('compile2', 'emberTemplates:compile2');
	grunt.registerTask('compile3', 'emberTemplates:compile3');
	grunt.registerTask('min', ['concat', 'uglify']);

};
