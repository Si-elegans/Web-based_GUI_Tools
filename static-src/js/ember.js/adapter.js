App.ApplicationAdapter = DS.RESTAdapter.extend({
		namespace : 'restAPI',
		//host: 'https://192.168.7.3:8000',
		headers : Ember.computed(function () {
			return {
				"X-CSRFToken" : Ember.$.cookie('csrftoken')
			};
		}).volatile(),
		pathForType : function (type) {
			if (type == "behaviouralExperiment")
				return "behaviouralExperimentsFull";
			else if (type == "cylinder")
				return "CylinderType";
			else if (type == "hair")
				return "HairType";
			else if (type == "hexagon")
				return "HexagonType";
			else if (type == "cube")
				return "CubeType";
			else if (type == "user")
				return "users";
			else if (type == "reservation")
				return "reservations";
			else if (type == "chemical")
				return "chemicalType";
			else if (type == "crowding")
				return "crowdingType";
			else if (type == "directTouch")
				return "directTouchType";
			else if (type == "dynamicDropTest")
				return "dynamicDropTestType";
			else if (type == "environment")
				return "environmentType";
			else if (type == "experiment")
				return "experimentType";
			else if (type == "experimentWideConf")
				return "experimentWideConfType";
			else if (type == "interactionAtSpecificTime")
				return "interactionAtSpecificTimeType";
			else if (type == "interactionFromt0tot1")
				return "interactionFromt0tot1Type";
			else if (type == "mechanoInteraction")
				return "mechanoInteractionType";
			else if (type == "mechanosensationPermanent")
				return "mechanosensationExpWideType";
			else if (type == "mechanosensationExact")
				return "mechanosensationTimeEventType";
			else if (type == "mechanosensationInterval")
				return "mechanosensationTimet0tot1Type";
			else if (type == "galvanotaxisPermanent")
				return "galvanotaxisExperimentWideType";
			else if (type == "galvanotaxisExact")
				return "galvanotaxisTimeEventType";
			else if (type == "galvanotaxisInterval")
				return "galvanotaxisTimet0tot1Type";
			else if (type == "termotaxisPermanent")
				return "termotaxisExperimentWideType";
			else if (type == "termotaxisExact")
				return "termotaxisTimeEventType";
			else if (type == "termotaxisInterval")
				return "termotaxisTimet0tot1Type";
			else if (type == "chemotaxisPermanent")
				return "chemotaxisExperimentWideType";
			else if (type == "chemotaxisExact")
				return "chemotaxisTimeEventType";
			else if (type == "chemotaxisInterval")
				return "chemotaxisTimet0tot1Type";
			else if (type == "obstacleLocation")
				return "obstacleLocationType";
			else if (type == "osmoticRing")
				return "osmoticRingType";
			else if (type == "plateConfiguration")
				return "plateConfigurationType";
			else if (type == "pointSourceHeatAvoidance")
				return "pointSourceHeatAvoidanceType";
			else if (type == "wormDatum")
				return "wormDataType";
			else if (type == "wormStatus")
				return "wormStatusType";
			else if (type == "phototaxisExact")
				return "phototaxisTimeEventType";
			else if (type == "phototaxisInterval")
				return "phototaxisTimet0tot1Type";
			else if (type == "phototaxisPermanent")
				return "phototaxisExperimentWideType";
			else if (type == "pointSourceLight")
				return "pointSourceLightType";
			else if (type == "temperatureChangeInTime")
				return "temperatureChangeInTimeType";
			else if (type == "chemotaxisQuadrants1")
				return "chemotaxisQuadrants_1_Type";
			else if (type == "chemotaxisQuadrants2")
				return "chemotaxisQuadrants_2_Type";
			else if (type == "chemotaxisQuadrants4")
				return "chemotaxisQuadrants_4_Type";
			else if (type == "linearThermalGradient")
				return "linearThermalGradientType";
			else if (type == "plateTap")
				return "plateTapType";
			else if (type == "temperatureChangeInTime")
				return "temperatureChangeInTimeType";
			else if (type == "linearThermalGradient")
				return "linearThermalGradientType";
			else if (type == "electricShock")
				return "electricShockType";
			else if (type == "staticPointSource")
				return "staticPointSourceType";
			else
				return this._super(type);
		},
		ajax : function (url, method, hash) {
			hash = hash || {}; // hash may be undefined
			hash.crossDomain = true;
			hash.xhrFields = {
				withCredentials : true
			};
			return this._super(url, method, hash);
		},
		buildURL : function (type, id, record) {
			var host = this.get('host');
			var url = [],
			//host = ember$data$lib$adapters$rest_adapter$$get(this, 'host'),
			prefix = this.urlPrefix();

			if (type) {
				url.push(this.pathForType(type));
			}

			//We might get passed in an array of ids from findMany
			//in which case we don't want to modify the url, as the
			//ids will be passed in through a query param
			if (id && !Ember.isArray(id)) {
				url.push(encodeURIComponent(id));
			}

			if (prefix) {
				url.unshift(prefix);
			}

			url = url.join('/');
			if (!host && url) {
				url = '/' + url;
			}

			return url + '/';
		},
	});

App.myMixin = Ember.Mixin.create(DS.EmbeddedRecordsMixin, {
		extractEmbeddedBelongsTo : function (store, key, embeddedType, hash) {
			if (!hash[key]) {
				return hash;
			}

			var embeddedSerializer = store.serializerFor(embeddedType.typeKey);
			var embeddedRecord = embeddedSerializer.normalize(embeddedType, hash[key], null);
			if (typeof(embeddedRecord) === "object") {
				store.push(embeddedType, embeddedRecord);
				hash[key] = embeddedRecord.id;
			} else {
				hash[key] = embeddedRecord;
			}

			//TODO Need to add a reference to the parent later so relationship works between both `belongsTo` records
			return hash;
		},
		normalize : function (type, hash, prop) {
			//var normalizedHash = typeof(hash) === "object" ? this._super(type, hash, prop) : hash;
			var normalizedHash = typeof(hash) === "object" ? DS.RESTSerializer.prototype.normalize.call(this, type, hash, prop) : hash;

			//in this case, we know the server and hash not need to be normalized.
			return this.extractEmbeddedRecords(this, this.store, type, normalizedHash);
		},
		extractEmbeddedRecords : function (serializer, store, type, partial) {

			var self = this;
			type.eachRelationship(function (key, relationship) {
				if (serializer.hasDeserializeRecordsOption(key)) {
					var embeddedType = store.modelFor(relationship.type.typeKey);
					if (relationship.kind === "hasMany") {
						if (relationship.options.polymorphic) {
							ember$data$lib$serializers$embedded_records_mixin$$extractEmbeddedHasManyPolymorphic(store, key, partial);
						} else {
							self.extractEmbeddedHasMany(store, key, embeddedType, partial);
						}
					}
					if (relationship.kind === "belongsTo") {
						self.extractEmbeddedBelongsTo(store, key, embeddedType, partial);
					}
				}
			});

			return partial;
		},
		extractEmbeddedHasMany : function (store, key, embeddedType, hash) {
			if (!hash[key]) {
				return hash;
			}

			var ids = [];

			var embeddedSerializer = store.serializerFor(embeddedType.typeKey);
			Ember.EnumerableUtils.forEach(hash[key], function (data) {
				var embeddedRecord = embeddedSerializer.normalize(embeddedType, data, null);
				if (typeof(embeddedRecord) === "object") {
					store.push(embeddedType, embeddedRecord);
					ids.push(embeddedRecord.id);
				} else {
					ids.push(embeddedRecord);
				}
			});

			hash[key] = ids;
			return hash;
		}
	});

App.ApplicationSerializer = DS.RESTSerializer.extend(App.myMixin, {
		primaryKey: 'uuid',
		attrs : {
			experimentDefinition : {
				deserialize : 'records'
			},
			interactionAtSpecificTime : {
				deserialize : 'records'
			},
			environmentDefinition : {
				deserialize : 'records'
			},
			users_with_access : {
				deserialize : 'records'
			},
			interactionFromt0tot1 : {
				deserialize : 'records'
			},
			experimentWideConf : {
				deserialize : 'records'
			},
			mechanosensation : {
				deserialize : 'records'
			},
			chemotaxis : {
				deserialize : 'records'
			},
			termotaxis : {
				deserialize : 'records'
			},
			galvanotaxis : {
				deserialize : 'records'
			},
			phototaxis : {
				deserialize : 'records'
			},
			directTouch : {
				deserialize : 'records'
			},
			plateTap : {
				deserialize : 'records'
			},
			pointSourceLightConf : {
				deserialize : 'records'
			},
			wormStatus : {
				deserialize : 'records'
			},
			wormData : {
				deserialize : 'records'
			},
			plateConfiguration : {
				deserialize : 'records'
			},
			crowding : {
				deserialize : 'records'
			},
			obstacle : {
				deserialize : 'records'
			},
			Cylinder : {
				deserialize : 'records'
			},
			Cube : {
				deserialize : 'records'
			},
			Hexagon : {
				deserialize : 'records'
			},
			Hair : {
				deserialize : 'records'
			},
			creator : {
				deserialize : 'records'
			},
			dynamicDropTestConf : {
				deserialize : 'records'
			},
			chemical : {
				deserialize : 'records'
			},
			temperatureChangeInTime : {
				deserialize : 'records'
			},
			osmoticRing : {
				deserialize : 'records'
			},
			chemotaxisQuadrants : {
				deserialize : 'records'
			},
			quadrantBarrierChemical : {
				deserialize : 'records'
			},
			quadrantChemical : {
				deserialize : 'records'
			},
			ringChemical : {
				deserialize : 'records'
			},
			linearThermalGradient : {
				deserialize : 'records'
			},
			pointSourceHeatAvoidance : {
				deserialize : 'records'
			},
			electricShockConf : {
				deserialize : 'records'
			},
			chemotaxisQuadrants1 : {
				deserialize : 'records'
			},
			chemotaxisQuadrants2 : {
				deserialize : 'records'
			},
			chemotaxisQuadrants4 : {
				deserialize : 'records'
			},
			staticPointSourceConf : {
				deserialize : 'records'
			},
			quadrant_1_Chemical : {
				deserialize : 'records'
			},
			quadrant_2_Chemical : {
				deserialize : 'records'
			},
			quadrant_3_Chemical : {
				deserialize : 'records'
			},
			quadrant_4_Chemical : {
				deserialize : 'records'
			},
			temperatureChangeInTime : {
				deserialize : 'records'
			},
			linearThermalGradient : {
				deserialize : 'records'
			},
		},

		extractArray : function (store, primaryType, payload) {
			var newPayload = {};
			newPayload[primaryType.typeKey.pluralize()] = payload;
			return this._super(store, primaryType, newPayload);
		},
		/**
		 * @since 0.0.11
		 * @method extractSingle
		 * @inheritDoc
		 */
		extractSingle : function (store, primaryType, payload, recordId) {
			var newPayload;
			if (payload === null) {
				return this._super.apply(this, arguments);
			}
			if (recordId) {
				payload.id = recordId;
			}
			newPayload = {};
			newPayload[primaryType.typeKey.pluralize()] = [payload];
			return this._super(store, primaryType, newPayload, recordId);
		},
		/**
		 * @since 0.0.11
		 * @method extractDeleteRecord
		 * @inheritDoc
		 */
		extractDeleteRecord : function (store, type, payload, id, requestType) {
			return this._super(store, type, null, id, requestType);
		},

		//method that converts Ember JSON format to Django JSON format
		serializeIntoHash : function (hash, type, record, options) {
			var s = this.serialize(record, options);
			Object.getOwnPropertyNames(s).forEach(function (item) {
				hash[item] = s[item];
			});
		},

	});
	
App.UserSerializer = App.ApplicationSerializer.extend({
	primaryKey: 'id'
});

App.savingMixin = Ember.Mixin.create({
		init : function () {
			this._super();
			this.get('isDirty');
			//})
		},
		becameDirty : function () {
			if (this.get('isDirty')) {
				var controller = App.__container__.lookup("controller:experiment");
				var proxySend = jQuery.proxy(controller.send, controller);
				proxySend('savingModelDidUpdate', this);
			} else {}
		}
		.observes('isDirty')
	});

	