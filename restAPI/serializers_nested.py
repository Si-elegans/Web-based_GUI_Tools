from rest_framework import routers, serializers, viewsets
from rest_framework.fields import empty, set_value, Field, SkipField
from behaviouralExperimentDefinition.models import *
from booking.models import Reservation, PE_results
from spirit.models import User
from collections import OrderedDict
from siteLogic.utils import secure_exception_to_str
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)




class User_nested_type_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


###############behaviouralExperimentDefinition##########

class Cube_nested_type_serializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret
    class Meta:
        model = CubeType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class Cylinder_nested_type_serializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret
    class Meta:
        model = CylinderType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class Hexagon_nested_type_serializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret
    class Meta:
        model = HexagonType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class crowding_nested_type_serializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret
    class Meta:
        model = crowdingType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class obstacleLocation_nested_type_serializer(serializers.ModelSerializer):
    Cylinder = Cylinder_nested_type_serializer (required=False)
    Cube = Cube_nested_type_serializer (required=False)
    Hexagon = Hexagon_nested_type_serializer (required=False)

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = obstacleLocationType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class plateConfiguration_nested_type_serializer(serializers.ModelSerializer):
    Cylinder = Cylinder_nested_type_serializer (required=False)
    Cube = Cube_nested_type_serializer (required=False)
    Hexagon = Hexagon_nested_type_serializer (required=False)

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    def create (self, validated_data):
        try:
            Cylinder = validated_data.pop ('Cylinder')
            cylinder_data = CylinderType_model.objects.create (**Cylinder)
            plate_configuration_object=plateConfigurationType_model.objects.create(Cylinder=cylinder_data, **validated_data)
        except:
            try:
                Cube = validated_data.pop ('Cube')
                cube_data = CubeType_model.objects.create (**Cube)
                plate_configuration_object=plateConfigurationType_model.objects.create(Cube=cube_data, **validated_data)
            except:
                try:
                    Hexagon = validated_data.pop ('Hexagon')
                    hexagon_data = HexagonType_model.objects.create (**Hexagon)
                    plate_configuration_object=plateConfigurationType_model.objects.create(Hexagon=hexagon_data,**validated_data)
                except KeyError as e:
                    logger.debug ("Key error, all keys are null" + secure_exception_to_str(e))
        return plate_configuration_object



    class Meta:
        model = plateConfigurationType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class wormData_nested_type_serializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret
    class Meta:
        model = wormDataType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class wormStatus_nested_type_serializer(serializers.ModelSerializer):
    wormData = wormData_nested_type_serializer()

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = wormStatusType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

    def create(self, validated_data):
        worm_data = validated_data.pop('wormData')
        print 'worm_data' , worm_data
        worm_data_object=wormDataType_model.objects.create(**worm_data)
        wormStatus = wormStatusType_model.objects.create(wormData=worm_data_object,**validated_data)
        return wormStatus

class environment_nested_type_serializer(serializers.ModelSerializer):
    wormStatus = wormStatus_nested_type_serializer ()
    plateConfiguration = plateConfiguration_nested_type_serializer ()
    obstacle = obstacleLocation_nested_type_serializer (many=True, required = False )
    crowding = crowding_nested_type_serializer ()

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = environmentType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class chemical_nested_type_serializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = chemicalType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class chemotaxisQuadrants_1_nested_type_serializer(serializers.ModelSerializer):
    quadrantChemical = chemical_nested_type_serializer()

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                representation = field.to_representation(attribute)
                if representation is None:
                    # Do not serialize empty objects
                    continue
                if isinstance(representation, list) and not representation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = representation

        return ret

    class Meta:
        model = chemotaxisQuadrantsType_1_model
        exclude = ('uuid',)
        lookup_field = 'uuid'


class chemotaxisQuadrants_2_nested_type_serializer(serializers.ModelSerializer):
    quadrant_1_Chemical = chemical_nested_type_serializer()
    quadrant_2_Chemical = chemical_nested_type_serializer()
    quadrantBarrierChemical = chemical_nested_type_serializer()

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                representation = field.to_representation(attribute)
                if representation is None:
                    # Do not serialize empty objects
                    continue
                if isinstance(representation, list) and not representation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = representation

        return ret

    class Meta:
        model = chemotaxisQuadrantsType_2_model
        exclude = ('uuid',)
        lookup_field = 'uuid'


class chemotaxisQuadrants_4_nested_type_serializer(serializers.ModelSerializer):
    quadrant_1_Chemical = chemical_nested_type_serializer()
    quadrant_2_Chemical = chemical_nested_type_serializer()
    quadrant_3_Chemical = chemical_nested_type_serializer()
    quadrant_4_Chemical = chemical_nested_type_serializer()
    quadrantBarrierChemical = chemical_nested_type_serializer()

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                representation = field.to_representation(attribute)
                if representation is None:
                    # Do not serialize empty objects
                    continue
                if isinstance(representation, list) and not representation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = representation

        return ret

    class Meta:
        model = chemotaxisQuadrantsType_4_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class osmoticRing_nested_type_serializer(serializers.ModelSerializer):
    ringChemical = chemical_nested_type_serializer ()
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = osmoticRingType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class staticPointSource_nested_type_serializer(serializers.ModelSerializer):
    chemical = chemical_nested_type_serializer ()
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = staticPointSourceType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'


class chemotaxisExperimentWide_nested_type_serializer(serializers.ModelSerializer):
    staticPointSourceConf = staticPointSource_nested_type_serializer(required = False)
    chemotaxisQuadrants1 = chemotaxisQuadrants_1_nested_type_serializer (required = False)
    chemotaxisQuadrants2 = chemotaxisQuadrants_2_nested_type_serializer (required = False)
    chemotaxisQuadrants4 = chemotaxisQuadrants_4_nested_type_serializer (required = False)
    osmoticRing = osmoticRing_nested_type_serializer (required=False)
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                representation = field.to_representation(attribute)
                if representation is None:
                    # Do not serialize empty objects
                    continue
                if isinstance(representation, list) and not representation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = representation

        return ret

    class Meta:
        model = chemotaxisExperimentWideType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class staticPointSource_nested_type_serializer(serializers.ModelSerializer):
    chemical = chemical_nested_type_serializer ()
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = staticPointSourceType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class dynamicDropTestType_nested_type_serializer(serializers.ModelSerializer):
    chemical = chemical_nested_type_serializer ()
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = dynamicDropTestType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class chemotaxisTimeEvent_nested_type_serializer(serializers.ModelSerializer):
    dynamicDropTestConf = dynamicDropTestType_nested_type_serializer(required = False)
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                representation = field.to_representation(attribute)
                if representation is None:
                    # Do not serialize empty objects
                    continue
                if isinstance(representation, list) and not representation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = representation

        return ret

    class Meta:
        model = chemotaxisTimeEventType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class chemotaxisTimet0tot1_nested_type_serializer(serializers.ModelSerializer):
    #GE: No experiment below right now so no serializer defined for concrete experiments
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = chemotaxisTimet0tot1Type_model
        exclude = ('uuid',)
        lookup_field = 'uuid'



class directTouch_nested_type_serializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = directTouchType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'





class galvanotaxisExperimentWide_nested_type_serializer(serializers.ModelSerializer):
    #GE: No experiment below right now so no serializer defined for concrete experiments
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = galvanotaxisExperimentWideType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class galvanotaxisTimeEvent_nested_type_serializer(serializers.ModelSerializer):
    #GE: No experiment below right now so no serializer defined for concrete experiments

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = galvanotaxisTimeEventType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class electricShock_nested_type_serializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                representation = field.to_representation(attribute)
                if representation is None:
                    # Do not serialize empty objects
                    continue
                if isinstance(representation, list) and not representation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = representation

        return ret

    class Meta:
        model = electricShockType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class galvanotaxisTimet0tot1_nested_type_serializer(serializers.ModelSerializer):
    # GE: right now is the only experiment available, if more are added it should be set to required = False
    electricShockConf = electricShock_nested_type_serializer ()
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = galvanotaxisTimet0tot1Type_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class plateTap_nested_type_serializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = plateTapType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'


class mechanosensationTimeEvent_nested_type_serializer(serializers.ModelSerializer):
    directTouch = directTouch_nested_type_serializer(required = False)
    plateTap = plateTap_nested_type_serializer (required = False)
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = mechanosensationTimeEventType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class pointSourceLight_nested_type_serializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = pointSourceLightType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class phototaxisTimeEvent_nested_type_serializer(serializers.ModelSerializer):
    #GE: right now is the only experiment available, if more are added it should be set to required = False
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = phototaxisTimeEventType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class pointSourceHeatAvoidance_nested_type_serializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = pointSourceHeatAvoidanceType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class termotaxisTimeEvent_nested_type_serializer(serializers.ModelSerializer):
    #GE: right now is the only experiment available, if more are added it should be set to required = False
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = termotaxisTimeEventType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'



class linearThermalGradient_nested_type_serializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = linearThermalGradientType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class mechanosensationExpWide_nested_type_serializer(serializers.ModelSerializer):
    #GE: No experiment below right now so no serializer defined for concrete experiments
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = mechanosensationExpWideType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'



class mechanosensationTimet0tot1_nested_type_serializer(serializers.ModelSerializer):
    #GE: No experiment below right now so no serializer defined for concrete experiments
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = mechanosensationTimet0tot1Type_model
        exclude = ('uuid',)
        lookup_field = 'uuid'




class phototaxisExperimentWide_nested_type_serializer(serializers.ModelSerializer):
    #GE: No experiment below right now so no serializer defined for concrete experiments
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = phototaxisExperimentWideType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'



class phototaxisTimet0tot1_nested_type_serializer(serializers.ModelSerializer):
    pointSourceLightConf = pointSourceLight_nested_type_serializer ()
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = phototaxisTimet0tot1Type_model
        exclude = ('uuid',)
        lookup_field = 'uuid'







class temperatureChangeInTime_nested_type_serializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = temperatureChangeInTimeType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class termotaxisExperimentWide_nested_type_serializer(serializers.ModelSerializer):
    linearThermalGradient = linearThermalGradient_nested_type_serializer ()
    #GE: right now is the only experiment available, if more are added it should be set to required = False
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = termotaxisExperimentWideType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'


class termotaxisTimet0tot1_nested_type_serializer(serializers.ModelSerializer):
    temperatureChangeInTime = temperatureChangeInTime_nested_type_serializer(required = False)
    pointSourceHeatAvoidance = pointSourceHeatAvoidance_nested_type_serializer(required = False)
    #GE: right now is the only experiment available, if more are added it should be set to required = False
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = termotaxisTimet0tot1Type_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class interactionAtSpecificTime_nested_type_serializer(serializers.ModelSerializer):

    mechanosensation=mechanosensationTimeEvent_nested_type_serializer (required=False)
    chemotaxis=chemotaxisTimeEvent_nested_type_serializer (required=False)
    termotaxis=termotaxisTimeEvent_nested_type_serializer (required=False)
    galvanotaxis=galvanotaxisTimeEvent_nested_type_serializer (required=False)
    phototaxis=phototaxisTimeEvent_nested_type_serializer (required=False)

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = interactionAtSpecificTimeType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class interactionFromt0tot1_nested_type_serializer(serializers.ModelSerializer):
    mechanosensation= mechanosensationTimet0tot1_nested_type_serializer (required=False)
    chemotaxis= chemotaxisTimet0tot1_nested_type_serializer (required=False)
    termotaxis= termotaxisTimet0tot1_nested_type_serializer (required=False)
    galvanotaxis= galvanotaxisTimet0tot1_nested_type_serializer (required=False)
    phototaxis = phototaxisTimet0tot1_nested_type_serializer (required=False)

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = interactionFromt0tot1Type_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class experimentWideConf_nested_type_serializer(serializers.ModelSerializer):
    mechanosensation= mechanosensationExpWide_nested_type_serializer (required=False)
    chemotaxis= chemotaxisExperimentWide_nested_type_serializer (required=False)
    termotaxis= termotaxisExperimentWide_nested_type_serializer (required=False)
    galvanotaxis= galvanotaxisExperimentWide_nested_type_serializer (required=False)
    phototaxis = phototaxisExperimentWide_nested_type_serializer (required=False)


    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:

        model = experimentWideConfType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class experiment_nested_type_serializer(serializers.ModelSerializer):
    interactionAtSpecificTime = interactionAtSpecificTime_nested_type_serializer (many=True, required = False)
    interactionFromt0tot1 = interactionFromt0tot1_nested_type_serializer (many=True, required = False)
    experimentWideConf = experimentWideConf_nested_type_serializer (many=True, required = False)

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret


    class Meta:
        model = experimentType_model
        exclude = ('uuid',)
        lookup_field = 'uuid'

class behaviourExperiment_nested_type_serializer(serializers.ModelSerializer):
    experimentDefinition = experiment_nested_type_serializer ()
    environmentDefinition = environment_nested_type_serializer()
    #creator = User
    class Meta:
        model = behaviourExperimentType_model
        exclude = ('users_with_access','creator','created')
        lookup_field = 'uuid'
        ##The following has added to avoid receiving uiid unique validation (this field must be unique) fail when a post is done with a uuid. With this we're not checkin the uniqueness automatically done by modelSerializers, but since this is generated by a function on the model, this is not a problem
        extra_kwargs = {
            "uuid": {
                "validators": [],
            },
        }

    def create(self,validated_data):
        del validated_data['uuid'] # I need to delete the uuid from the data, to avoid reusing it and to have the model create it
        ########## Environment ####################       
        environment_definition = validated_data.pop('environmentDefinition')
        worm_status = environment_definition ['wormStatus']
        worm_data = worm_status ['wormData']
        worm_data_object=wormDataType_model.objects.create(**worm_data)
        ######
        #GE: del need to be done, because the foreign key element has already this info and collides with
        # it other wise. Error looks like "create() got multiple values for keyword argument 'plateConfiguration'"
        # for a following element
        del worm_status ['wormData']
        wormStatus = wormStatusType_model.objects.create(wormData=worm_data_object,**worm_status)
        del environment_definition ['wormStatus']
        plate_conf = environment_definition ['plateConfiguration']
        try:
            Cylinder = plate_conf ['Cylinder']
            cylinder_data = CylinderType_model.objects.create (**Cylinder)
            del plate_conf ['Cylinder']
            plate_configuration_object=plateConfigurationType_model.objects.create(Cylinder=cylinder_data,**plate_conf)
        except:
            try:
                Cube = plate_conf ['Cube']
                cube_data = CubeType_model.objects.create (**Cube)
                del plate_conf ['Cube']
                plate_configuration_object=plateConfigurationType_model.objects.create(Cube=cube_data, **plate_conf)
            except:
                try:
                    Hexagon = plate_conf ['Hexagon']
                    hexagon_data = HexagonType_model.objects.create (**Hexagon)
                    del plate_conf ['Hexagon']
                    plate_configuration_object=plateConfigurationType_model.objects.create(Hexagon=hexagon_data,**plate_conf)
                except KeyError as e:
                    logger.debug ("Key error, all plateConfiguration keys are null" + secure_exception_to_str(e))
                    plate_configuration_object=plateConfigurationType_model.objects.create(**plate_conf)
        del environment_definition ['plateConfiguration']
        crowding_data = environment_definition ['crowding']
        crowding_data_object=crowdingType_model.objects.create(**crowding_data)
        del environment_definition ['crowding']
        obstacle_object_list = []
        try:
            obstacle_conf = environment_definition ['obstacle']
            for obstacle in obstacle_conf:
                try:
                    Cylinder = obstacle['Cylinder']
                    cylinder_data = CylinderType_model.objects.create (**Cylinder)
                    del obstacle['Cylinder']
                    obstacleLocationType_model_object=obstacleLocationType_model.objects.create(Cylinder=cylinder_data, **obstacle)
                except:
                    try:
                        Cube = obstacle ['Cube']
                        cube_data = CubeType_model.objects.create (**Cube)
                        del obstacle['Cube']
                        obstacleLocationType_model_object=obstacleLocationType_model.objects.create(Cube=cube_data, **obstacle)
                    except:
                        try:
                            Hexagon = obstacle ['Hexagon']
                            hexagon_data = HexagonType_model.objects.create (**Hexagon)
                            del obstacle['Hexagon']
                            obstacleLocationType_model_object=obstacleLocationType_model.objects.create(Hexagon=hexagon_data,**obstacle)
                        except KeyError as e:
                            logger.debug ("Key error, all obstacle keys are null" + secure_exception_to_str(e))
                            obstacleLocationType_model_object=obstacleLocationType_model.objects.create(**obstacle)
                obstacle_object_list.append (obstacleLocationType_model_object)
            del environment_definition ['obstacle']
        except KeyError as e:
            logger.debug ("No obstacles found" + secure_exception_to_str(e))

        ####
        ##GE: I had to do this and not with objects.create () given the obstacles many to many relationship
        ####
        environmentType_object = environmentType_model ()
        environmentType_object.description = environment_definition ['description']
        environmentType_object.wormStatus = wormStatus
        environmentType_object.crowding = crowding_data_object
        environmentType_object.plateConfiguration = plate_configuration_object
        environmentType_object.save()
        for obstacle in obstacle_object_list:
            environmentType_object.obstacle.add (obstacle.pk)

        ########## Experiment ####################
        experiment_definition = validated_data.pop('experimentDefinition')
        #######interaction at specific t####################
        #GE: Make a for each interaction type and create it based on the loop!!!!!
        interactionAtSpecificTime_list = []
        interactionFromt0tot1_list = []
        experimentWideConf_list = []
        #GE:!!!!!!!!!!!!!!! WHAT HAPPENS IF NO INTERACTION AT SPECIFIC TIME!!!!!!!!!!!!!
        try:
            interactionAtSpecificTime = experiment_definition ['interactionAtSpecificTime']

            for interaction in interactionAtSpecificTime:
                #mechanosensation chemotaxis termotaxis galvanotaxis phototaxis
                try:
                    mechano = interaction['mechanosensation']
                    try:
                        directTouch = mechano ['directTouch']
                        directTouchType_model_data = directTouchType_model.objects.create (**directTouch)
                        del mechano['directTouch']
                        mechanosensationTimeEventType_model_object=mechanosensationTimeEventType_model.objects.create(directTouch=directTouchType_model_data, **mechano)
                    except:
                        try:
                            plateTap = mechano ['plateTap']
                            plateTapType_model_data = plateTapType_model.objects.create (**plateTap)
                            del mechano['plateTap']
                            mechanosensationTimeEventType_model_object=mechanosensationTimeEventType_model.objects.create(plateTap=plateTapType_model_data, **mechano)
                        except KeyError as e:
                            logger.debug ("Key error, all mechanosensation keys are null" + secure_exception_to_str(e))
                            mechanosensationTimeEventType_model_object=mechanosensationTimeEventType_model.objects.create (**mechano)
                    del interaction['mechanosensation']
                    interactionAtSpecificTimeType_model_object=interactionAtSpecificTimeType_model.objects.create(mechanosensation=mechanosensationTimeEventType_model_object, **interaction)
                except:
                    try:
                        chemotaxis = interaction['chemotaxis']
                        try:
                            dynamicDropTestConf = chemotaxis ['dynamicDropTestConf']
                            try:
                                chemical = dynamicDropTestConf ['chemical']
                                chemicalType_model_data = chemicalType_model.objects.create (**chemical)
                                del dynamicDropTestConf ['chemical']
                                dynamicDropTestType_model_data = dynamicDropTestType_model.objects.create (chemical=chemicalType_model_data, **dynamicDropTestConf)
                                del chemotaxis['dynamicDropTestConf']
                                chemotaxisTimeEventType_model_object=chemotaxisTimeEventType_model.objects.create(dynamicDropTestConf=dynamicDropTestType_model_data, **chemotaxis)
                            except KeyError as e:
                                logger.debug ("Key error, chemical not available" + secure_exception_to_str(e))
                        except KeyError as e:
                            logger.debug ("Key error, all chemotaxis keys are null" + secure_exception_to_str(e))
                            chemotaxisTimeEventType_model_object=chemotaxisTimeEventType_model.objects.create(**chemotaxis)
                        del interaction['chemotaxis']
                        interactionAtSpecificTimeType_model_object=interactionAtSpecificTimeType_model.objects.create(chemotaxis=chemotaxisTimeEventType_model_object, **interaction)
                    except:
                        try:
                            termotaxis = interaction['termotaxis']
                            termotaxisTimeEventType_model_object=termotaxisTimeEventType_model.objects.create(**termotaxis)
                            del interaction['termotaxis']
                            interactionAtSpecificTimeType_model_object=interactionAtSpecificTimeType_model.objects.create(termotaxis=termotaxisTimeEventType_model_object, **interaction)
                        except:
                            try:
                                galvanotaxis = interaction['galvanotaxis']
                                galvanotaxisTimeEventType_model_object=galvanotaxisTimeEventType_model.objects.create(**galvanotaxis)
                                del interaction['galvanotaxis']
                                interactionAtSpecificTimeType_model_object=interactionAtSpecificTimeType_model.objects.create(galvanotaxis=galvanotaxisTimeEventType_model_object, **interaction)
                            except:
                                try:
                                    phototaxis = interaction['phototaxis']
                                    phototaxisTimeEventType_model_object=phototaxisTimeEventType_model.objects.create(**phototaxis)
                                    del interaction['phototaxis']
                                    interactionAtSpecificTimeType_model_object=interactionAtSpecificTimeType_model.objects.create(phototaxis=phototaxisTimeEventType_model_object, **interaction)
                                except KeyError as e:
                                    logger.debug("Key error, no key for interactionAtSpecificTime available" + secure_exception_to_str(e))
                                    interactionAtSpecificTimeType_model_object=interactionAtSpecificTimeType_model.objects.create(**interaction)
                interactionAtSpecificTime_list.append(interactionAtSpecificTimeType_model_object)
            del experiment_definition ['interactionAtSpecificTime']
        except KeyError as e:
            logger.debug ("Key error, no interactionAtSpecificTime available" + secure_exception_to_str(e))

        #######interaction from t0 - t1####################

        try:
            interactionFromt0tot1 = experiment_definition ['interactionFromt0tot1']
            for interaction in interactionFromt0tot1:
                #mechanosensation chemotaxis termotaxis galvanotaxis phototaxis
                try:
                    mechano = interaction['mechanosensation']
                    mechanosensationTimet0tot1Type_model_object=mechanosensationTimet0tot1Type_model.objects.create(**mechano)
                    del interaction['mechanosensation']
                    interactionFromt0tot1Type_model_object = interactionFromt0tot1Type_model.objects.create(mechanosensation=mechanosensationTimet0tot1Type_model_object, **interaction)
                except:
                    try:
                        chemotaxis = interaction['chemotaxis']
                        chemotaxisTimet0tot1Type_model_object=chemotaxisTimet0tot1Type_model.objects.create(**chemotaxis)
                        del interaction['chemotaxis']
                        interactionFromt0tot1Type_model_object = interactionFromt0tot1Type_model.objects.create(chemotaxis=chemotaxisTimet0tot1Type_model_object, **interaction)
                    except:
                        try:
                            termotaxis = interaction['termotaxis']
                            try:
                                temperatureChangeInTime = termotaxis['temperatureChangeInTime']
                                temperatureChangeInTimeType_model_data = temperatureChangeInTimeType_model.objects.create(**temperatureChangeInTime)
                                del termotaxis['temperatureChangeInTime']
                                termotaxisTimet0tot1Type_model_object=termotaxisTimet0tot1Type_model.objects.create(temperatureChangeInTime=temperatureChangeInTimeType_model_data, **termotaxis)
                            except:
                                try:
                                    pointSourceHeatAvoidance = termotaxis['pointSourceHeatAvoidance']
                                    pointSourceHeatAvoidanceType_model_data = pointSourceHeatAvoidanceType_model.objects.create(**pointSourceHeatAvoidance)
                                    del termotaxis['pointSourceHeatAvoidance']
                                    termotaxisTimet0tot1Type_model_object=termotaxisTimet0tot1Type_model.objects.create(pointSourceHeatAvoidance=pointSourceHeatAvoidanceType_model_data, **termotaxis)
                                except KeyError as e:
                                    logger.debug ("Key error, all termotaxis keys are null" + secure_exception_to_str(e))
                                    termotaxisTimet0tot1Type_model_object=termotaxisTimet0tot1Type_model.objects.create(**termotaxis)
                            del interaction['termotaxis']
                            interactionFromt0tot1Type_model_object=interactionFromt0tot1Type_model.objects.create(termotaxis=termotaxisTimet0tot1Type_model_object, **interaction)
                        except:
                            try:
                                galvanotaxis = interaction['galvanotaxis']
                                try:
                                    electricShockConf = galvanotaxis['electricShockConf']
                                    electricShockType_model_data  = electricShockType_model.objects.create(**electricShockConf)
                                    del galvanotaxis['electricShockConf']
                                    galvanotaxisTimet0tot1Type_model_object=galvanotaxisTimet0tot1Type_model.objects.create(electricShockConf=electricShockType_model_data, **galvanotaxis)
                                except KeyError as e:
                                    logger.debug ("Key error, all galvanotaxis keys are null" + secure_exception_to_str(e))
                                    galvanotaxisTimet0tot1Type_model_object=galvanotaxisTimet0tot1Type_model.objects.create(**galvanotaxis)
                                del interaction['galvanotaxis']
                                interactionFromt0tot1Type_model_object = interactionFromt0tot1Type_model.objects.create(galvanotaxis=galvanotaxisTimet0tot1Type_model_object, **interaction)
                            except:
                                try:
                                    phototaxis = interaction['phototaxis']
                                    try:
                                        pointSourceLightConf= phototaxis['pointSourceLightConf']
                                        pointSourceLightType_model_data = pointSourceLightType_model.objects.create(**pointSourceLightConf)
                                        del phototaxis ['pointSourceLightConf']
                                        phototaxisTimet0tot1Type_model_object=phototaxisTimet0tot1Type_model.objects.create(pointSourceLightConf=pointSourceLightType_model_data,**phototaxis)
                                    except KeyError as e:
                                        logger.debug ("Key error, pointSourceLightConf not available" + secure_exception_to_str(e))
                                        phototaxisTimet0tot1Type_model_object=phototaxisTimet0tot1Type_model.objects.create (**phototaxis)
                                    del interaction['phototaxis']
                                    interactionFromt0tot1Type_model_object = interactionFromt0tot1Type_model.objects.create(phototaxis=phototaxisTimet0tot1Type_model_object, **interaction)
                                except KeyError as e:
                                    logger.debug ("Key error, no key for interactionFromt0tot1 available" + secure_exception_to_str(e))
                                    interactionFromt0tot1Type_model.objects.create(**interaction)
                interactionFromt0tot1_list.append(interactionFromt0tot1Type_model_object)
            del experiment_definition ['interactionFromt0tot1']
        except KeyError as e:
            logger.debug ("Key error, no interactionFromt0tot1 available" + secure_exception_to_str(e))
        #######Experiment - wide ####################
        try:
            experimentWideConf = experiment_definition ['experimentWideConf']
            for interaction in experimentWideConf:
                #mechanosensation chemotaxis termotaxis galvanotaxis phototaxis
                try:
                    mechano = interaction['mechanosensation']
                    mechanosensationExpWideType_model_object=mechanosensationExpWideType_model.objects.create(**mechano)
                    del interaction['mechanosensation']
                    experimentWideConfType_model_object = experimentWideConfType_model.objects.create(mechanosensation=mechanosensationExpWideType_model_object, **interaction)
                except:
                    try:
                        chemotaxis = interaction['chemotaxis']
                        try:
                            staticPointSourceConf = chemotaxis ['staticPointSourceConf']
                            try:
                                chemical = staticPointSourceConf ['chemical']
                                chemicalType_model_data = chemicalType_model.objects.create (**chemical)
                                del staticPointSourceConf ['chemical']
                                staticPointSourceType_model_data = staticPointSourceType_model.objects.create (chemical = chemicalType_model_data,**staticPointSourceConf)
                                del chemotaxis['staticPointSourceConf']
                                chemotaxisExperimentWideType_model_object=chemotaxisExperimentWideType_model.objects.create(staticPointSourceConf=staticPointSourceType_model_data, **chemotaxis)
                            except KeyError as e:
                                logger.debug ("Key error, chemical not available" + secure_exception_to_str(e))
                        except:
                            try:
                                chemotaxisQuadrants1 = chemotaxis['chemotaxisQuadrants1']
                                try:
                                    quadrantChemical = chemotaxisQuadrants1['quadrantChemical']
                                    quadrantChemical_chemicalType_model_object=chemicalType_model.objects.create(**quadrantChemical)
                                    del chemotaxisQuadrants1['quadrantChemical']
                                except KeyError as e:
                                    logger.debug ("Key error, chemical keys missing" + secure_exception_to_str(e))
                                chemotaxisQuadrantsType_1_model_data = chemotaxisQuadrantsType_1_model.objects.create(quadrantChemical=quadrantChemical_chemicalType_model_object, **chemotaxisQuadrants1)
                                del chemotaxis['chemotaxisQuadrants1']
                                chemotaxisExperimentWideType_model_object=chemotaxisExperimentWideType_model.objects.create(chemotaxisQuadrants1=chemotaxisQuadrantsType_1_model_data, **chemotaxis)
                            except:
                                try:
                                    chemotaxisQuadrants2 = chemotaxis ['chemotaxisQuadrants2']
                                    try:
                                        quadrant_1_Chemical = chemotaxisQuadrants2['quadrant_1_Chemical']
                                        quadrant_1_Chemical_chemicalType_model_object=chemicalType_model.objects.create(**quadrant_1_Chemical)
                                        del chemotaxisQuadrants2['quadrant_1_Chemical']
                                        quadrant_2_Chemical = chemotaxisQuadrants2['quadrant_2_Chemical']
                                        quadrant_2_Chemical_chemicalType_model_object=chemicalType_model.objects.create(**quadrant_2_Chemical)
                                        del chemotaxisQuadrants2['quadrant_2_Chemical']
                                        quadrantBarrierChemical = chemotaxisQuadrants2 ['quadrantBarrierChemical']
                                        quadrantBarrierChemical_chemicalType_model_object=chemicalType_model.objects.create(**quadrantBarrierChemical)
                                        del chemotaxisQuadrants2['quadrantBarrierChemical']
                                    except KeyError as e:
                                        logger.debug("Key error, chemical keys missing" + secure_exception_to_str(e))
                                    chemotaxisQuadrantsType_2_model_data = chemotaxisQuadrantsType_2_model.objects.create(quadrant_1_Chemical=quadrant_1_Chemical_chemicalType_model_object, quadrant_2_Chemical=quadrant_2_Chemical_chemicalType_model_object, quadrantBarrierChemical=quadrantBarrierChemical_chemicalType_model_object, **chemotaxisQuadrants2)
                                    del chemotaxis ['chemotaxisQuadrants2']
                                    chemotaxisExperimentWideType_model_object=chemotaxisExperimentWideType_model.objects.create(chemotaxisQuadrants2=chemotaxisQuadrantsType_2_model_data, **chemotaxis)
                                except:
                                    try:
                                        chemotaxisQuadrants4 = chemotaxis ['chemotaxisQuadrants4']
                                        try:
                                            quadrant_1_Chemical = chemotaxisQuadrants4['quadrant_1_Chemical']
                                            quadrant_1_Chemical_chemicalType_model_object=chemicalType_model.objects.create(**quadrant_1_Chemical)
                                            del chemotaxisQuadrants4['quadrant_1_Chemical']
                                            quadrant_2_Chemical = chemotaxisQuadrants4['quadrant_2_Chemical']
                                            quadrant_2_Chemical_chemicalType_model_object=chemicalType_model.objects.create(**quadrant_2_Chemical)
                                            del chemotaxisQuadrants4['quadrant_2_Chemical']
                                            quadrant_3_Chemical = chemotaxisQuadrants4['quadrant_3_Chemical']
                                            quadrant_3_Chemical_chemicalType_model_object=chemicalType_model.objects.create(**quadrant_3_Chemical)
                                            del chemotaxisQuadrants4['quadrant_3_Chemical']
                                            quadrant_4_Chemical = chemotaxisQuadrants4['quadrant_4_Chemical']
                                            quadrant_4_Chemical_chemicalType_model_object=chemicalType_model.objects.create(**quadrant_4_Chemical)
                                            del chemotaxisQuadrants4['quadrant_4_Chemical']
                                            quadrantBarrierChemical = chemotaxisQuadrants4['quadrantBarrierChemical']
                                            quadrantBarrierChemical_chemicalType_model_object=chemicalType_model.objects.create(**quadrantBarrierChemical)
                                            del chemotaxisQuadrants4['quadrantBarrierChemical']
                                        except KeyError as e:
                                            logger.debug ("Key error, chemical keys missing" + secure_exception_to_str(e))
                                        chemotaxisQuadrantsType_4_model_data = chemotaxisQuadrantsType_4_model.objects.create\
                                            (quadrant_1_Chemical=quadrant_1_Chemical_chemicalType_model_object, quadrant_2_Chemical=quadrant_2_Chemical_chemicalType_model_object,\
                                             quadrant_3_Chemical=quadrant_3_Chemical_chemicalType_model_object, quadrant_4_Chemical=quadrant_4_Chemical_chemicalType_model_object,\
                                             quadrantBarrierChemical=quadrantBarrierChemical_chemicalType_model_object,**chemotaxisQuadrants4)
                                        del chemotaxis ['chemotaxisQuadrants4']
                                        chemotaxisExperimentWideType_model_object=chemotaxisExperimentWideType_model.objects.create(chemotaxisQuadrants4=chemotaxisQuadrantsType_4_model_data, **chemotaxis)
                                    except:
                                        try:
                                            osmoticRing = chemotaxis ['osmoticRing']
                                            try:
                                                ringChemical = osmoticRing ['ringChemical']
                                                ringChemical_chemicalType_model_object=chemicalType_model.objects.create(**ringChemical)
                                                del osmoticRing ['ringChemical']
                                            except KeyError as e:
                                                logger.debug ("Key error, chemical key missing" + secure_exception_to_str(e))
                                            osmoticRingType_model_data = osmoticRingType_model.objects.create (ringChemical=ringChemical_chemicalType_model_object,**osmoticRing)
                                            del chemotaxis ['osmoticRing']
                                            chemotaxisExperimentWideType_model_object=chemotaxisExperimentWideType_model.objects.create(osmoticRing=osmoticRingType_model_data, **chemotaxis)
                                        except KeyError as e:
                                            logger.debug ("Key error, all chemotaxis keys are null" + secure_exception_to_str(e) + unicode (**chemotaxis))
                                            chemotaxisExperimentWideType_model_object=chemotaxisExperimentWideType_model.objects.create(**chemotaxis)
                        del interaction['chemotaxis']
                        experimentWideConfType_model_object = experimentWideConfType_model.objects.create(chemotaxis=chemotaxisExperimentWideType_model_object, **interaction)
                    except:
                        try:
                            termotaxis = interaction['termotaxis']
                            try:
                                linearThermalGradient = termotaxis ['linearThermalGradient']
                                linearThermalGradientType_model_data = linearThermalGradientType_model.objects.create (**linearThermalGradient)
                                del termotaxis ['linearThermalGradient']
                                termotaxisExperimentWideType_model_object=termotaxisExperimentWideType_model.objects.create(linearThermalGradient=linearThermalGradientType_model_data, **termotaxis)
                            except KeyError as e:
                                logger.debug ("Key error, linearThermalGradient not available" + secure_exception_to_str(e))
                                termotaxisExperimentWideType_model_object=termotaxisExperimentWideType_model.objects.create(**termotaxis)
                            del interaction['termotaxis']
                            experimentWideConfType_model_object=experimentWideConfType_model.objects.create(termotaxis=termotaxisExperimentWideType_model_object, **interaction)
                        except:
                            try:
                                galvanotaxis = interaction['galvanotaxis']
                                galvanotaxisExperimentWideType_model_object=galvanotaxisExperimentWideType_model.objects.create(**galvanotaxis)
                                del interaction['galvanotaxis']
                                experimentWideConfType_model_object = experimentWideConfType_model.objects.create(galvanotaxis=galvanotaxisExperimentWideType_model_object, **interaction)
                            except:
                                try:
                                    phototaxis = interaction['phototaxis']
                                    phototaxisExperimentWideType_model_object=phototaxisExperimentWideType_model.objects.create(**phototaxis)
                                    del interaction['phototaxis']
                                    experimentWideConfType_model_object = experimentWideConfType_model.objects.create(phototaxis=phototaxisExperimentWideType_model_object, **interaction)
                                except KeyError as e:
                                    logger.debug ("Key error, no key for experimentWideConf available" + secure_exception_to_str(e))
                                    #experimentWideConfType_model_object = experimentWideConfType_model.objects.create(**interaction)
                experimentWideConf_list.append (experimentWideConfType_model_object)
            del experiment_definition ['experimentWideConf']
        except KeyError as e:
            logger.debug ("Key error, no experimentWideConf available" + secure_exception_to_str(e))


        experiment_definition_object = experimentType_model ()
        experiment_definition_object.description = experiment_definition ['description']
        experiment_definition_object.experimentDuration = experiment_definition ['experimentDuration']
        experiment_definition_object.save()
        for interactionAtSpecificTime in interactionAtSpecificTime_list:
            experiment_definition_object.interactionAtSpecificTime.add (interactionAtSpecificTime.pk)
        for interactionFromt0tot1 in interactionFromt0tot1_list:
            experiment_definition_object.interactionFromt0tot1.add (interactionFromt0tot1.pk)
        for experimentWideConf in experimentWideConf_list:
            experiment_definition_object.experimentWideConf.add (experimentWideConf.pk)
        behaviourExperimentType = behaviourExperimentType_model.objects.create(experimentDefinition=experiment_definition_object,environmentDefinition=environmentType_object,**validated_data)
        return behaviourExperimentType