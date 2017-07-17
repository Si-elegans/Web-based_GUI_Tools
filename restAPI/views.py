from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from behaviouralExperimentDefinition.models import *
from booking.models import Reservation, PE_results, PE_results_files,share_pe_results,share_rb_results
from cenet.models import share_CENetwork
from lems_ui.models import  share_LemsModel
from restAPI.serializers import *
from spirit.models import User
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated


class AllowPostAll_ListOnly_Admins_Permissions(permissions.BasePermission):

    def has_permission(self, request, view):

        # Allow get requests for all
        if request.method == 'POST':
            return True
        elif request.user.is_superuser:
            return True
        else:
            return False
# ViewSets define the view behavior.

class reservation_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = reservation_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)

class reservation_ViewSet(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = reservation_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)
    
class shareBehaviouralExperiment_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = shareBehaviouralExperiment.objects.all()
    serializer_class = shareBehaviouralExperiment_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class shareBehaviouralExperiment_ViewSet(generics.ListCreateAPIView):
    queryset = shareBehaviouralExperiment.objects.all()
    serializer_class = shareBehaviouralExperiment_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class share_pe_results_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = share_pe_results.objects.all()
    serializer_class = share_pe_results_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class share_pe_results_ViewSet(generics.ListCreateAPIView):
    queryset = share_pe_results.objects.all()
    serializer_class = share_pe_results_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class share_rb_results_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = share_rb_results.objects.all()
    serializer_class = share_rb_results_serializer
    permission_classes = (IsAuthenticated,)

class share_rb_results_ViewSet(generics.ListCreateAPIView):
    queryset = share_rb_results.objects.all()
    serializer_class = share_rb_results_serializer
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class share_neuronmodels_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = share_LemsModel.objects.all()
    serializer_class = share_LemsModel_serializer
    permission_classes = (IsAuthenticated,)

class share_neuronmodels_ViewSet(generics.ListCreateAPIView):
    queryset = share_LemsModel.objects.all()
    serializer_class = share_LemsModel_serializer
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class share_networkmodels_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = share_CENetwork.objects.all()
    serializer_class = share_CENetwork_serializer
    permission_classes = (IsAuthenticated,)

class share_networkmodels_ViewSet(generics.ListCreateAPIView):
    queryset = share_CENetwork.objects.all()
    serializer_class = share_CENetwork_serializer
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

    #Problems with PUT from python requests against Django Rest Framework?
    #Add a trailing slash at the end!! 
    #http://stackoverflow.com/questions/30671808/django-rest-framework-empty-request-data
    #def update(self, request, pk = None):
    #    print pk
    #    print request.stream.read()
    #    #print str(request.data)
    #    
    #def get_queryset(self):
    #    if self.request.method == 'PUT':
    #        print 'self.request.GET=>',self.request.GET
    #        print 'self.request.POST=>',self.request.POST
    #        print 'self.request.body=>',self.request.body
    #    queryset = Reservation.objects.all()
    #    return queryset
       

##behaviouralExperimentDefinition##  


class CubeType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CubeType_model.objects.all()
    serializer_class = CubeType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class CubeType_ViewSet(generics.ListCreateAPIView):
    queryset = CubeType_model.objects.all()
    serializer_class = CubeType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class CylinderType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CylinderType_model.objects.all()
    serializer_class = CylinderType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)

class CylinderType_ViewSet(generics.ListCreateAPIView):
    queryset = CylinderType_model.objects.all()
    serializer_class = CylinderType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class HexagonType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HexagonType_model.objects.all()
    serializer_class = HexagonType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class HexagonType_ViewSet(generics.ListCreateAPIView):
    queryset = HexagonType_model.objects.all()
    serializer_class = HexagonType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)
    
class behaviourExperimentType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = behaviourExperimentType_model.objects.all()
    serializer_class = behaviourExperimentType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)

class behaviourExperimentType_ViewSet(generics.ListCreateAPIView):
    queryset = behaviourExperimentType_model.objects.all()
    serializer_class = behaviourExperimentType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class chemicalType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = chemicalType_model.objects.all()
    serializer_class = chemicalType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class chemicalType_ViewSet(generics.ListCreateAPIView):
    queryset = chemicalType_model.objects.all()
    serializer_class = chemicalType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class chemotaxisExperimentWideType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = chemotaxisExperimentWideType_model.objects.all()
    serializer_class = chemotaxisExperimentWideType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class chemotaxisExperimentWideType_ViewSet(generics.ListCreateAPIView):
    queryset = chemotaxisExperimentWideType_model.objects.all()
    serializer_class = chemotaxisExperimentWideType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class chemotaxisQuadrants_1_Type_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = chemotaxisQuadrantsType_1_model.objects.all()
    serializer_class = chemotaxisQuadrants_1_Type_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class chemotaxisQuadrants_1_Type_ViewSet(generics.ListCreateAPIView):
    queryset = chemotaxisQuadrantsType_1_model.objects.all()
    serializer_class = chemotaxisQuadrants_1_Type_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class chemotaxisQuadrants_2_Type_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = chemotaxisQuadrantsType_2_model.objects.all()
    serializer_class = chemotaxisQuadrants_2_Type_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class chemotaxisQuadrants_2_Type_ViewSet(generics.ListCreateAPIView):
    queryset = chemotaxisQuadrantsType_2_model.objects.all()
    serializer_class = chemotaxisQuadrants_2_Type_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class chemotaxisQuadrants_4_Type_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = chemotaxisQuadrantsType_4_model.objects.all()
    serializer_class = chemotaxisQuadrants_4_Type_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class chemotaxisQuadrants_4_Type_ViewSet(generics.ListCreateAPIView):
    queryset = chemotaxisQuadrantsType_4_model.objects.all()
    serializer_class = chemotaxisQuadrants_4_Type_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class chemotaxisTimeEventType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = chemotaxisTimeEventType_model.objects.all()
    serializer_class = chemotaxisTimeEventType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class chemotaxisTimeEventType_ViewSet(generics.ListCreateAPIView):
    queryset = chemotaxisTimeEventType_model.objects.all()
    serializer_class = chemotaxisTimeEventType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class chemotaxisTimet0tot1Type_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = chemotaxisTimet0tot1Type_model.objects.all()
    serializer_class = chemotaxisTimet0tot1Type_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class chemotaxisTimet0tot1Type_ViewSet(generics.ListCreateAPIView):
    queryset = chemotaxisTimet0tot1Type_model.objects.all()
    serializer_class = chemotaxisTimet0tot1Type_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class crowdingType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = crowdingType_model.objects.all()
    serializer_class = crowdingType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class crowdingType_ViewSet(generics.ListCreateAPIView):
    queryset = crowdingType_model.objects.all()
    serializer_class = crowdingType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)
    
class directTouchType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = directTouchType_model.objects.all()
    serializer_class = directTouchType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class directTouchType_ViewSet(generics.ListCreateAPIView):
    queryset = directTouchType_model.objects.all()
    serializer_class = directTouchType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)
    
class staticPointSourceType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = staticPointSourceType_model.objects.all()
    serializer_class = staticPointSourceType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class staticPointSourceType_ViewSet(generics.ListCreateAPIView):
    queryset = staticPointSourceType_model.objects.all()
    serializer_class = staticPointSourceType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class electricShockType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = electricShockType_model.objects.all()
    serializer_class = electricShockType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class electricShockType_ViewSet(generics.ListCreateAPIView):
    queryset = electricShockType_model.objects.all()
    serializer_class = electricShockType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class dynamicDropTestType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = dynamicDropTestType_model.objects.all()
    serializer_class = dynamicDropTestType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class dynamicDropTestType_ViewSet(generics.ListCreateAPIView):
    queryset = dynamicDropTestType_model.objects.all()
    serializer_class = dynamicDropTestType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class environmentType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = environmentType_model.objects.all()
    serializer_class = environmentType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class environmentType_ViewSet(generics.ListCreateAPIView):
    queryset = environmentType_model.objects.all()
    serializer_class = environmentType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class experimentType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = experimentType_model.objects.all()
    serializer_class = experimentType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)

class experimentType_ViewSet(generics.ListCreateAPIView):
    queryset = experimentType_model.objects.all()
    serializer_class = experimentType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class experimentWideConfType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = experimentWideConfType_model.objects.all()
    serializer_class = experimentWideConfType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class experimentWideConfType_ViewSet(generics.ListCreateAPIView):
    queryset = experimentWideConfType_model.objects.all()
    serializer_class = experimentWideConfType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class galvanotaxisExperimentWideType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = galvanotaxisExperimentWideType_model.objects.all()
    serializer_class = galvanotaxisExperimentWideType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class galvanotaxisExperimentWideType_ViewSet(generics.ListCreateAPIView):
    queryset = galvanotaxisExperimentWideType_model.objects.all()
    serializer_class = galvanotaxisExperimentWideType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class galvanotaxisTimeEventType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = galvanotaxisTimeEventType_model.objects.all()
    serializer_class = galvanotaxisTimeEventType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class galvanotaxisTimeEventType_ViewSet(generics.ListCreateAPIView):
    queryset = galvanotaxisTimeEventType_model.objects.all()
    serializer_class = galvanotaxisTimeEventType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class galvanotaxisTimet0tot1Type_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = galvanotaxisTimet0tot1Type_model.objects.all()
    serializer_class = galvanotaxisTimet0tot1Type_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class galvanotaxisTimet0tot1Type_ViewSet(generics.ListCreateAPIView):
    queryset = galvanotaxisTimet0tot1Type_model.objects.all()
    serializer_class = galvanotaxisTimet0tot1Type_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class interactionAtSpecificTimeType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = interactionAtSpecificTimeType_model.objects.all()
    serializer_class = interactionAtSpecificTimeType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)

class interactionAtSpecificTimeType_ViewSet(generics.ListCreateAPIView):
    queryset = interactionAtSpecificTimeType_model.objects.all()
    serializer_class = interactionAtSpecificTimeType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class interactionFromt0tot1Type_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = interactionFromt0tot1Type_model.objects.all()
    serializer_class = interactionFromt0tot1Type_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class interactionFromt0tot1Type_ViewSet(generics.ListCreateAPIView):
    queryset = interactionFromt0tot1Type_model.objects.all()
    serializer_class = interactionFromt0tot1Type_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class linearThermalGradientType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = linearThermalGradientType_model.objects.all()
    serializer_class = linearThermalGradientType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class linearThermalGradientType_ViewSet(generics.ListCreateAPIView):
    queryset = linearThermalGradientType_model.objects.all()
    serializer_class = linearThermalGradientType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class mechanosensationExpWideType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = mechanosensationExpWideType_model.objects.all()
    serializer_class = mechanosensationExpWideType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class mechanosensationExpWideType_ViewSet(generics.ListCreateAPIView):
    queryset = mechanosensationExpWideType_model.objects.all()
    serializer_class = mechanosensationExpWideType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class mechanosensationTimeEventType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = mechanosensationTimeEventType_model.objects.all()
    serializer_class = mechanosensationTimeEventType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class mechanosensationTimeEventType_ViewSet(generics.ListCreateAPIView):
    queryset = mechanosensationTimeEventType_model.objects.all()
    serializer_class = mechanosensationTimeEventType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class mechanosensationTimet0tot1Type_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = mechanosensationTimet0tot1Type_model.objects.all()
    serializer_class = mechanosensationTimet0tot1Type_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class mechanosensationTimet0tot1Type_ViewSet(generics.ListCreateAPIView):
    queryset = mechanosensationTimet0tot1Type_model.objects.all()
    serializer_class = mechanosensationTimet0tot1Type_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class obstacleLocationType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = obstacleLocationType_model.objects.all()
    serializer_class = obstacleLocationType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class obstacleLocationType_ViewSet(generics.ListCreateAPIView):
    queryset = obstacleLocationType_model.objects.all()
    serializer_class = obstacleLocationType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class osmoticRingType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = osmoticRingType_model.objects.all()
    serializer_class = osmoticRingType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class osmoticRingType_ViewSet(generics.ListCreateAPIView):
    queryset = osmoticRingType_model.objects.all()
    serializer_class = osmoticRingType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class phototaxisExperimentWideType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = phototaxisExperimentWideType_model.objects.all()
    serializer_class = phototaxisExperimentWideType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class phototaxisExperimentWideType_ViewSet(generics.ListCreateAPIView):
    queryset = phototaxisExperimentWideType_model.objects.all()
    serializer_class = phototaxisExperimentWideType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class phototaxisTimeEventType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = phototaxisTimeEventType_model.objects.all()
    serializer_class = phototaxisTimeEventType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class phototaxisTimeEventType_ViewSet(generics.ListCreateAPIView):
    queryset = phototaxisTimeEventType_model.objects.all()
    serializer_class = phototaxisTimeEventType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class phototaxisTimet0tot1Type_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = phototaxisTimet0tot1Type_model.objects.all()
    serializer_class = phototaxisTimet0tot1Type_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class phototaxisTimet0tot1Type_ViewSet(generics.ListCreateAPIView):
    queryset = phototaxisTimet0tot1Type_model.objects.all()
    serializer_class = phototaxisTimet0tot1Type_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class plateConfigurationType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = plateConfigurationType_model.objects.all()
    serializer_class = plateConfigurationType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)

class plateConfigurationType_ViewSet(generics.ListCreateAPIView):
    queryset = plateConfigurationType_model.objects.all()
    serializer_class = plateConfigurationType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class plateTapType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = plateTapType_model.objects.all()
    serializer_class = plateTapType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)

class plateTapType_ViewSet(generics.ListCreateAPIView):
    queryset = plateTapType_model.objects.all()
    serializer_class = plateTapType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class pointSourceLightType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = pointSourceLightType_model.objects.all()
    serializer_class = pointSourceLightType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class pointSourceLightType_ViewSet(generics.ListCreateAPIView):
    queryset = pointSourceLightType_model.objects.all()
    serializer_class = pointSourceLightType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class pointSourceHeatAvoidanceType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = pointSourceHeatAvoidanceType_model.objects.all()
    serializer_class = pointSourceHeatAvoidanceType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class pointSourceHeatAvoidanceType_ViewSet(generics.ListCreateAPIView):
    queryset = pointSourceHeatAvoidanceType_model.objects.all()
    serializer_class = pointSourceHeatAvoidanceType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)
    
class temperatureChangeInTimeType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = temperatureChangeInTimeType_model.objects.all()
    serializer_class = temperatureChangeInTimeType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class temperatureChangeInTimeType_ViewSet(generics.ListCreateAPIView):
    queryset = temperatureChangeInTimeType_model.objects.all()
    serializer_class = temperatureChangeInTimeType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class termotaxisExperimentWideType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = termotaxisExperimentWideType_model.objects.all()
    serializer_class = termotaxisExperimentWideType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    
class termotaxisExperimentWideType_ViewSet(generics.ListCreateAPIView):
    queryset = termotaxisExperimentWideType_model.objects.all()
    serializer_class = termotaxisExperimentWideType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class termotaxisTimeEventType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = termotaxisTimeEventType_model.objects.all()
    serializer_class = termotaxisTimeEventType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)

class termotaxisTimeEventType_ViewSet(generics.ListCreateAPIView):
    queryset = termotaxisTimeEventType_model.objects.all()
    serializer_class = termotaxisTimeEventType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)
    
#############################################
#Delete this after find and replace
#############################################

class termotaxisTimet0tot1Type_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = termotaxisTimet0tot1Type_model.objects.all()
    serializer_class = termotaxisTimet0tot1Type_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)

class termotaxisTimet0tot1Type_ViewSet(generics.ListCreateAPIView):
    queryset = termotaxisTimet0tot1Type_model.objects.all()
    serializer_class = termotaxisTimet0tot1Type_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class wormDataType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = wormDataType_model.objects.all()
    serializer_class = wormDataType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)

class wormDataType_ViewSet(generics.ListCreateAPIView):
    queryset = wormDataType_model.objects.all()
    serializer_class = wormDataType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)
    
class wormStatusType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = wormStatusType_model.objects.all()
    serializer_class = wormStatusType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)

class wormStatusType_ViewSet(generics.ListCreateAPIView):
    queryset = wormStatusType_model.objects.all()
    serializer_class = wormStatusType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)
    
########## NESTED    ##########


class wormStatus_nested_type_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = wormStatusType_model.objects.all()
    serializer_class = wormStatus_nested_type_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)

class wormStatus_nested_type_ViewSet(generics.ListCreateAPIView):
    queryset = wormStatusType_model.objects.all()
    serializer_class = wormStatus_nested_type_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class plateConfiguration_nested_type_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = plateConfigurationType_model.objects.all()
    serializer_class = plateConfiguration_nested_type_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)

class plateConfiguration_nested_type_ViewSet(generics.ListCreateAPIView):
    queryset = plateConfigurationType_model.objects.all()
    serializer_class = plateConfiguration_nested_type_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)
    
class environment_nested_type_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = environmentType_model.objects.all()
    serializer_class = environment_nested_type_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)

class environment_nested_type_ViewSet(generics.ListCreateAPIView):
    queryset = environmentType_model.objects.all()
    serializer_class = environment_nested_type_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)


class behaviourExperimentFullType_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = behaviourExperimentType_model.objects.all()
    serializer_class = behaviourExperimentFullType_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)

class behaviourExperimentFullType_ViewSet(generics.ListCreateAPIView):
    queryset = behaviourExperimentType_model.objects.all()
    serializer_class = behaviourExperimentFullType_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)

class behaviourExperiment_nested_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = behaviourExperimentType_model.objects.all()
    serializer_class = behaviourExperiment_nested_type_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)

class behaviourExperiment_nested_type_ViewSet(generics.ListCreateAPIView):
    queryset = behaviourExperimentType_model.objects.all()
    serializer_class = behaviourExperiment_nested_type_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)
    def perform_create(self, serializer):
        #This is to feed behaviourExperiment_nested_type_serializer.create with the current user value as the model's creator field
        serializer.save(creator=self.request.user)
########## NESTED    ########## 



class PE_results_files_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PE_results_files.objects.all()
    serializer_class = PE_results_files_serializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'uuid'
    def pre_save(self, obj):
        obj.results_file = self.request.FILES.get('file')

class PE_results_files_ViewSet(generics.ListCreateAPIView):
    queryset = PE_results_files.objects.all()
    serializer_class = PE_results_files_serializer
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)
    lookup_field = 'uuid'
    def pre_save(self, obj):
        obj.results_file = self.request.FILES.get('file')


class PE_results_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PE_results.objects.all()
    serializer_class = PE_results_serializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)

class PE_results_ViewSet(generics.ListCreateAPIView):
    queryset = PE_results.objects.all()
    serializer_class = PE_results_serializer
    lookup_field = 'uuid'
    permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)
    

##Part of tutorial that are not needed when using ModelViewSet
#class JSONResponse(HttpResponse):
#    """
#    An HttpResponse that renders its content into JSON.
#    """
#    def __init__(self, data, **kwargs):
#        content = JSONRenderer().render(data)
#        kwargs['content_type'] = 'application/json'
#        super(JSONResponse, self).__init__(content, **kwargs)
#
#@csrf_exempt
#def behaviouralExperiment_list(request):
#    """
#    List all code snippets, or create a new snippet.
#    """
#    if request.method == 'GET':
#        behaviourExperiments = behaviourExperimentType_model.objects.all()
#        serializer = behaviourExperimentType_ViewSet(behaviourExperiments, many=True)
#        return JSONResponse(serializer.data)
#
#    elif request.method == 'POST':
#        data = JSONParser().parse(request)
#        serializer = behaviourExperimentType_ViewSet(data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return JSONResponse(serializer.data, status=201)
#        return JSONResponse(serializer.errors, status=400)
#@csrf_exempt
#def behaviouralExperiment_detail(request, pk):
#    """
#    Retrieve, update or delete a code snippet.
#    """
#    try:
#        behaviourExperiment= behaviourExperimentType_model.objects.get(pk=pk)
#    except behaviourExperiment.DoesNotExist:
#        return HttpResponse(status=404)
#
#    if request.method == 'GET':
#        serializer = behaviourExperimentType_ViewSet(behaviourExperiment)
#        return JSONResponse(serializer.data)
#
#    elif request.method == 'PUT':
#        data = JSONParser().parse(request)
#        serializer = behaviourExperimentType_ViewSet(behaviourExperiment, data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return JSONResponse(serializer.data)
#        return JSONResponse(serializer.errors, status=400)
#
#    elif request.method == 'DELETE':
#        behaviourExperiment.delete()
#        return HttpResponse(status=204)
#######################################################################
####### Examples to further allow / permission over List / Detail Views, got CubeList and CubeDetail Working, permissions below not tested
#######################################################################

# class CubeList(generics.ListCreateAPIView):
#     queryset = CubeType_model.objects.all()
#     serializer_class = CubeType_serializer
#     permission_classes = (AllowPostAll_ListOnly_Admins_Permissions,)
#
# class CubeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CubeType_model.objects.all()
#     serializer_class = CubeType_serializer
#     lookup_field = 'uuid'
#     permission_classes = (IsAuthenticated,)

# class CubePermissionsAll(permissions.BasePermission):
# """
# Owners of the object or admins can do anything.
# Everyone else can do nothing.
# """
#
#     def has_permission(self, request, view):
#         if request.user.is_staff:
#             return True
#         else:
#             return False
#
# class CubePermissionsObj(permissions.BasePermission):
# """
# Owners of the object or admins can do anything.
# Everyone else can do nothing.
# """
#
#     def has_object_permission(self, request, view, obj):
#         if request.user.is_staff:
#             return True
#
#         return obj == request.user