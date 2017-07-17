from django import forms
from behaviouralExperimentDefinition.models import *


class CubeType_form(forms.ModelForm):    
    class Meta:
        model = CubeType_model
        exclude = ()

class CylinderType_form(forms.ModelForm):
    class Meta:
        model = CylinderType_model
        exclude = ()


class HexagonType_form(forms.ModelForm):
    class Meta:
        model = HexagonType_model
        exclude = ()

class behaviourExperimentType_form(forms.ModelForm):

    class Meta:
        model = behaviourExperimentType_model
        exclude = ()

class chemicalType_form(forms.ModelForm):
    class Meta:
        model = chemicalType_model
        exclude = ()

class chemotaxisExperimentWideType_form(forms.ModelForm):
    class Meta:
        model = chemotaxisExperimentWideType_model
        exclude = ()



class chemotaxisTimeEventType_form(forms.ModelForm):
    class Meta:
        model = chemotaxisTimeEventType_model
        exclude = ()

class chemotaxisTimet0tot1Type_form(forms.ModelForm):
    class Meta:
        model = chemotaxisTimet0tot1Type_model
        exclude = ()

class crowdingType_form(forms.ModelForm):
    class Meta:
        model = crowdingType_model
        exclude = ()




class environmentType_form(forms.ModelForm):
    class Meta:
        model = environmentType_model
        exclude = ()

class experimentType_form(forms.ModelForm):
    class Meta:
        model = experimentType_model
        exclude = ()


class experimentWideConfType_form(forms.ModelForm):
    class Meta:
        model = experimentWideConfType_model
        exclude = ()

class galvanotaxisExperimentWideType_form(forms.Form):
    class Meta:
        model = galvanotaxisExperimentWideType_model
        exclude = ()

class galvanotaxisTimeEventType_form(forms.ModelForm):
    class Meta:
        model = galvanotaxisTimeEventType_model
        exclude = ()

class galvanotaxisTimet0tot1Type_form(forms.ModelForm):
    class Meta:
        model = galvanotaxisTimet0tot1Type_model
        exclude = ()

class interactionAtSpecificTimeType_form(forms.ModelForm):
    class Meta:
        model = interactionAtSpecificTimeType_model
        exclude = ()

class interactionFromt0tot1Type_form(forms.ModelForm):
    class Meta:
        model = interactionFromt0tot1Type_model
        exclude = ()

class directTouchType_form(forms.ModelForm):
    class Meta:
        model = directTouchType_model
        exclude = ()

class plateTapType_form(forms.ModelForm):
    class Meta:
        model = plateTapType_model
        exclude = ()

class mechanosensationExpWideType_form(forms.ModelForm):
    class Meta:
        model = mechanosensationExpWideType_model
        exclude = ()

class mechanosensationTimeEventType_form(forms.ModelForm):
    class Meta:
        model = mechanosensationTimeEventType_model
        exclude = ()

class mechanosensationTimet0tot1Type_form(forms.ModelForm):
    class Meta:
        model = mechanosensationTimet0tot1Type_model
        exclude = ()


class obstacleLocationType_form(forms.ModelForm):
    class Meta:
        model = obstacleLocationType_model
        exclude = ()


class osmoticRingType_form(forms.ModelForm):
    class Meta:
        model = osmoticRingType_model
        exclude = ()

class plateConfigurationType_form(forms.ModelForm):
    class Meta:
        model = plateConfigurationType_model
        exclude = ()

class pointSourceHeatAvoidanceType_form(forms.ModelForm):
    class Meta:
        model = pointSourceHeatAvoidanceType_model
        exclude = ()

class termotaxisTimeEventType_form(forms.ModelForm):
    class Meta:
        model = termotaxisTimeEventType_model
        exclude = ()

class termotaxisTimet0tot1Type_form(forms.ModelForm):
    class Meta:
        model = termotaxisTimet0tot1Type_model
        exclude = ()

class wormDataType_form(forms.ModelForm):
    class Meta:
        model = wormDataType_model
        exclude = ()

class wormStatusType_form(forms.ModelForm):
    class Meta:
        model = wormStatusType_model
        exclude = ()
