App.VisualizationController = Ember.ObjectController.extend({
		needs : ["experiment"],
		experiment : Ember.computed.alias("controllers.experiment"),
		actions : {
			addEvent : function (eventName) {
				this.get('model').events.push({});
			},
			changeToEvent : function (source) {
				console.log(source);
				var router = this.get('target');
				console.log(router);
				router.transitionTo(source.eventType, source.id);
			},
			changeMenu : function (neuron) {
				var neurons = this.get('model.neurons');
				for (var i = 0; i < neurons.length; i++) {
					if (neurons[i].name == neuron) {
						this.send('setNeuronSelectedValue', neurons[i]);
						return;
					}
				}
			},
			focusNeuron : function (neuronName) {
				var neuron;
				var neurons = this.get('model.neurons');
				for (var i = 0; i < neurons.length; i++) {
					if (neurons[i].name == neuronName) {
						neuron = neurons[i];
						break;
					}
				}
				//remove border for previous focused neuron
				var focused = this.get('controllers.experiment.focusedNeuron');
				if (focused) {
					var c = document.getElementById("button" + focused.name);
					c.className = c.className.replace(/(?:^|\s)green-bordered(?!\S)/g, '');
					for (var i = 0; i < focused.synapse.length; i++) {
						var d = document.getElementById("button" + focused.synapse[i]);
						d.className = d.className.replace(/(?:^|\s)yellow-bordered(?!\S)/g, '');
					}
				}
				//paint buttons border in the new
				var a = document.getElementById("button" + neuron.name);
				a.className = a.className + " green-bordered";
				for (var i = 0; i < neuron.synapse.length; i++) {
					var b = document.getElementById("button" + neuron.synapse[i]);
					b.className = b.className + " yellow-bordered";
				}
				//focus camera
				this.get('controllers.experiment').send('focusNeuron', neuron);
			},
			setNeuronSelectedValue : function (neuron, value) {
				if (neuron.selected) {
					Ember.set(neuron, 'selected', false);
				} else {
					Ember.set(neuron, 'selected', true);
				}
			},
			changeIsInTimeline : function () {
				var model = this.get('model');
				if (model.isInTimeline) {
					Ember.set(model, 'isInTimeline', false);
				} else {
					Ember.set(model, 'isInTimeline', true);
				}
			},
			playAnimation : function () {
				this.get('controllers.experiment').send('playAnimation');
			},
			timeChanged : function (time) {
				var neurons = this.get('model.neurons');
				for (var i = 0; i < neurons.length; i++) {
					Ember.set(neurons[i], "isSpiking", false);
					for (var j = 0; j < neurons[i].voltages.length; j++) {
						if (parseFloat(neurons[i].voltages[j].Run) > time - 0.2 && parseFloat(neurons[i].voltages[j].Run) < time + 0.2) {
							if (parseFloat(neurons[i].voltages[j].Speed) > 60) {
								Ember.set(neurons[i], "isSpiking", true);
							}
							break;
						}
					}
				}
			},
		}
	});
