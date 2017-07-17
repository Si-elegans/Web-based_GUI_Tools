from rest_framework import routers, serializers, viewsets
from behaviouralExperimentDefinition.models import *
from booking.models import Reservation, PE_results, PE_results_files,share_pe_results,share_rb_results
from lems_ui.models import share_LemsModel
from cenet.models import share_CENetwork
from spirit.models import User
from restAPI.serializers_nested import *

###############behaviouralExperimentDefinition##########

class CubeType_serializer(serializers.ModelSerializer):    
    class Meta:
        model = CubeType_model
        exclude = ()
        lookup_field = 'uuid'

class CylinderType_serializer(serializers.ModelSerializer):
    class Meta:
        model = CylinderType_model
        exclude = ()
        lookup_field = 'uuid'

class HexagonType_serializer(serializers.ModelSerializer):
    class Meta:
        model = HexagonType_model
        exclude = ()
        lookup_field = 'uuid'
        
class behaviourExperimentType_serializer(serializers.ModelSerializer):

    class Meta:
        model = behaviourExperimentType_model
        exclude = ()
        lookup_field = 'uuid'
        
class behaviourExperimentFullType_serializer(serializers.ModelSerializer):

    class Meta:
        model = behaviourExperimentType_model
        exclude = ()
        depth = 10
        lookup_field = 'uuid'


class chemicalType_serializer(serializers.ModelSerializer):
    class Meta:
        model = chemicalType_model
        exclude = ()
        lookup_field = 'uuid'

class chemotaxisExperimentWideType_serializer(serializers.ModelSerializer):
    class Meta:
        model = chemotaxisExperimentWideType_model
        exclude = ()
        lookup_field = 'uuid'

class chemotaxisQuadrants_1_Type_serializer(serializers.ModelSerializer):
    class Meta:
        model = chemotaxisQuadrantsType_1_model
        exclude = ()
        lookup_field = 'uuid'

class chemotaxisQuadrants_2_Type_serializer(serializers.ModelSerializer):
    class Meta:
        model = chemotaxisQuadrantsType_2_model
        exclude = ()
        lookup_field = 'uuid'

class chemotaxisQuadrants_4_Type_serializer(serializers.ModelSerializer):
    class Meta:
        model = chemotaxisQuadrantsType_4_model
        exclude = ()
        lookup_field = 'uuid'

class chemotaxisTimeEventType_serializer(serializers.ModelSerializer):
    class Meta:
        model = chemotaxisTimeEventType_model
        exclude = ()
        lookup_field = 'uuid'

class chemotaxisTimet0tot1Type_serializer(serializers.ModelSerializer):
    class Meta:
        model = chemotaxisTimet0tot1Type_model
        exclude = ()
        lookup_field = 'uuid'

class crowdingType_serializer(serializers.ModelSerializer):
    class Meta:
        model = crowdingType_model
        exclude = ()
        lookup_field = 'uuid'

class directTouchType_serializer(serializers.ModelSerializer):
    class Meta:
        model = directTouchType_model
        exclude = ()
        lookup_field = 'uuid'

class staticPointSourceType_serializer(serializers.ModelSerializer):
    class Meta:
        model = staticPointSourceType_model
        exclude = ()
        lookup_field = 'uuid'

class dynamicDropTestType_serializer(serializers.ModelSerializer):
    class Meta:
        model = dynamicDropTestType_model
        exclude = ()
        lookup_field = 'uuid'

class electricShockType_serializer(serializers.ModelSerializer):
    class Meta:
        model = electricShockType_model
        exclude = ()
        lookup_field = 'uuid'


class environmentType_serializer(serializers.ModelSerializer):
    class Meta:
        model = environmentType_model
        exclude = ()
        lookup_field = 'uuid'

class experimentType_serializer(serializers.ModelSerializer):
    class Meta:
        model = experimentType_model
        exclude = ()
        lookup_field = 'uuid'


class experimentWideConfType_serializer(serializers.ModelSerializer):
    class Meta:
        model = experimentWideConfType_model
        exclude = ()
        lookup_field = 'uuid'

class galvanotaxisExperimentWideType_serializer(serializers.ModelSerializer):
    class Meta:
        model = galvanotaxisExperimentWideType_model
        exclude = ()
        lookup_field = 'uuid'

class galvanotaxisTimeEventType_serializer(serializers.ModelSerializer):
    class Meta:
        model = galvanotaxisTimeEventType_model
        exclude = ()
        lookup_field = 'uuid'

class galvanotaxisTimet0tot1Type_serializer(serializers.ModelSerializer):
    class Meta:
        model = galvanotaxisTimet0tot1Type_model
        exclude = ()
        lookup_field = 'uuid'

class interactionAtSpecificTimeType_serializer(serializers.ModelSerializer):
    class Meta:
        model = interactionAtSpecificTimeType_model
        exclude = ()
        lookup_field = 'uuid'

class interactionFromt0tot1Type_serializer(serializers.ModelSerializer):
    class Meta:
        model = interactionFromt0tot1Type_model
        exclude = ()
        lookup_field = 'uuid'

class linearThermalGradientType_serializer(serializers.ModelSerializer):
    class Meta:
        model = linearThermalGradientType_model
        exclude = ()
        lookup_field = 'uuid'
        
class mechanosensationExpWideType_serializer(serializers.ModelSerializer):
    class Meta:
        model = mechanosensationExpWideType_model
        exclude = ()
        lookup_field = 'uuid'

class mechanosensationTimeEventType_serializer(serializers.ModelSerializer):
    class Meta:
        model = mechanosensationTimeEventType_model
        exclude = ()
        lookup_field = 'uuid'

class mechanosensationTimet0tot1Type_serializer(serializers.ModelSerializer):
    class Meta:
        model = mechanosensationTimet0tot1Type_model
        exclude = ()
        lookup_field = 'uuid'

class obstacleLocationType_serializer(serializers.ModelSerializer):
    class Meta:
        model = obstacleLocationType_model
        exclude = ()
        lookup_field = 'uuid'

class osmoticRingType_serializer(serializers.ModelSerializer):
    class Meta:
        model = osmoticRingType_model
        exclude = ()
        lookup_field = 'uuid'
                
class phototaxisExperimentWideType_serializer(serializers.ModelSerializer):
    class Meta:
        model = phototaxisExperimentWideType_model
        exclude = ()
        lookup_field = 'uuid'
        
class phototaxisTimeEventType_serializer(serializers.ModelSerializer):
    class Meta:
        model = phototaxisTimeEventType_model
        exclude = ()
        lookup_field = 'uuid'
        
class phototaxisTimet0tot1Type_serializer(serializers.ModelSerializer):
    class Meta:
        model = phototaxisTimet0tot1Type_model
        exclude = ()
        lookup_field = 'uuid'

class plateConfigurationType_serializer(serializers.ModelSerializer):
    class Meta:
        model = plateConfigurationType_model
        exclude = ()
        lookup_field = 'uuid'
        
class plateTapType_serializer(serializers.ModelSerializer):
    class Meta:
        model = plateTapType_model
        exclude = ()
        lookup_field = 'uuid'

class pointSourceHeatAvoidanceType_serializer(serializers.ModelSerializer):
    class Meta:
        model = pointSourceHeatAvoidanceType_model
        exclude = ()
        lookup_field = 'uuid'

class pointSourceLightType_serializer(serializers.ModelSerializer):
    class Meta:
        model = pointSourceLightType_model
        exclude = ()
        lookup_field = 'uuid'
        
class temperatureChangeInTimeType_serializer(serializers.ModelSerializer):
    class Meta:
        model = temperatureChangeInTimeType_model
        exclude = ()
        lookup_field = 'uuid'

class termotaxisExperimentWideType_serializer(serializers.ModelSerializer):
    class Meta:
        model = termotaxisExperimentWideType_model
        exclude = ()
        lookup_field = 'uuid'

class termotaxisTimeEventType_serializer(serializers.ModelSerializer):
    class Meta:
        model = termotaxisTimeEventType_model
        exclude = ()
        lookup_field = 'uuid'

class termotaxisTimet0tot1Type_serializer(serializers.ModelSerializer):
    class Meta:
        model = termotaxisTimet0tot1Type_model
        exclude = ()
        lookup_field = 'uuid'

class wormDataType_serializer(serializers.ModelSerializer):
    class Meta:
        model = wormDataType_model
        exclude = ()
        lookup_field = 'uuid'

    
class wormStatusType_serializer(serializers.ModelSerializer):
    class Meta:
        model = wormStatusType_model
        exclude = ()
        lookup_field = 'uuid'

class shareBehaviouralExperiment_serializer(serializers.ModelSerializer):
    class Meta:
        model = shareBehaviouralExperiment
        exclude = ()
        lookup_field = 'uuid'

class share_pe_results_serializer(serializers.ModelSerializer):
    class Meta:
        model = share_pe_results
        exclude = ()
        lookup_field = 'uuid'

class share_rb_results_serializer(serializers.ModelSerializer):
    class Meta:
        model = share_rb_results
        exclude = ()

class share_LemsModel_serializer(serializers.ModelSerializer):
    class Meta:
        model = share_LemsModel
        exclude = ()

class share_CENetwork_serializer(serializers.ModelSerializer):
    class Meta:
        model = share_CENetwork
        exclude = ()



###############reservation_serializer##########

class reservation_serializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        exclude = ()
        lookup_field = 'uuid'
        

class PE_results_serializer(serializers.ModelSerializer):
    class Meta:
        model = PE_results
        exclude = ()
        lookup_field = 'uuid'
   
class PE_results_files_serializer(serializers.ModelSerializer):
    class Meta:
        model = PE_results_files
        exclude = ()
        lookup_field = 'uuid'

