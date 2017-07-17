from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from datetime import datetime
import uuid
User = settings.AUTH_USER_MODEL

def generate_new_uuid():
    return str(uuid.uuid4())

class behaviourExperimentType_model(models.Model):
    # BE CAREFUL About migrations that add unique fields !!!!!!!!!!!!! e.g. UUID
    # https: // docs.djangoproject.com / en / 1.9 / howto / writing - migrations /  # migrations-that-add-unique-fields
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    about = models.CharField(max_length=60, blank=True)    
    public = models.BooleanField (default = False, blank=True)
    public_set_date = models.DateTimeField (default=datetime.now)
    description = models.TextField(max_length=1000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, related_name='behaviouralExperiment_own')
    users_with_access = models.ManyToManyField (User, related_name='behaviouralExperiment_accessable', through = 'shareBehaviouralExperiment')    
    experimentDefinition = models.ForeignKey("experimentType_model")
    environmentDefinition = models.ForeignKey("environmentType_model")
    class Meta:       
        #unique_together = ("creator","experimentDefinition","environmentDefinition")        
        ordering = ["-created"]
    def __unicode__(self):
        return "id: %s" % (self.uuid, )
    def save(self, *args, **kwargs):
        if self.uuid is not None:
            try:
                orig = behaviourExperimentType_model.objects.get(uuid=self.uuid)
                if orig.public != self.public:
                    self.public_set_date = datetime.now()
            except: #If it is the first time that is being created then .get() fails and throws an exception
                pass
        super(behaviourExperimentType_model, self).save(*args, **kwargs)
    
####  ENVIRONMENT ##########
class environmentType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    description = models.TextField(max_length=1000, blank=True)
    wormStatus = models.ForeignKey("wormStatusType_model")
    plateConfiguration = models.ForeignKey("plateConfigurationType_model")
    obstacle = models.ManyToManyField("obstacleLocationType_model",blank=True)
    crowding = models.ForeignKey("crowdingType_model")
    envTemp = models.FloatField(('Environmental Temperature'), default=20)
    #class Meta:
        #unique_together = ()
    def __unicode__(self):
        return "id: %s" % (self.uuid, )
    
class wormStatusType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    xCoordFromPlateCentre = models.FloatField(blank=False)
    yCoorDFromPlateCentre = models.FloatField(blank=False)
    angleRelativeXaxis = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(6.28318)],blank=False)        
    wormData = models.ForeignKey("wormDataType_model")
    #class Meta:
        #unique_together = ("xCoordFromPlateCentre","yCoorDFromPlateCentre","angleRelativeXaxis","wormData")
    def __unicode__(self):
        return "id: %s" % (self.uuid, )
class wormDataType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    MALE = 'M'
    FEMALEHERMAPHRODITES = 'FH'
    GENDERTYPE = (        
            (MALE,"Male"),
            (FEMALEHERMAPHRODITES,"Female Hermaphrodites"),	
    )    
    gender = models.CharField(max_length=60, blank=False,choices=GENDERTYPE, default=FEMALEHERMAPHRODITES)
    age = models.PositiveIntegerField(blank=False)
    stageOfLifeCycle = models.PositiveIntegerField(blank=False,validators=[MinValueValidator(1),MaxValueValidator(4)])    
    timeOffFood = models.PositiveIntegerField(blank=False)
    #class Meta:
        #unique_together = ("gender","age","stageOfLifeCycle","timeOffFood")
    def __unicode__(self):
        return "id: %s" % (self.uuid, )
    
class crowdingType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    #These parameters wormsDistributionInPlate and wormsInPlate are fo 
    wormsDistributionInPlate = models.CharField(max_length=60, blank=True) 
    wormsInPlate = models.PositiveIntegerField(validators=[MinValueValidator(1)],default=1,blank=False,)
    #class Meta:
        #unique_together = ("wormsDistributionInPlate","wormsInPlate")
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

class obstacleLocationType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    xCoordFromPlateCentre = models.FloatField(blank=False)
    yCoorDFromPlateCentre = models.FloatField(blank=False)
    Stiffness = models.FloatField(validators=[MinValueValidator(0)],blank=False)
    CYLINDER = 'CY'
    CUBE = 'CU'
    HEXAGON = 'HE'
    SHAPETYPE = (        
        (CYLINDER,"cylinder"),
        (CUBE,"cube"),
        (HEXAGON,"hexagon"),
    )    
    shape = models.CharField(max_length=60, blank=False,choices=SHAPETYPE, default=CYLINDER)
    Cylinder = models.ForeignKey("CylinderType_model",null=True, blank=True)
    Cube = models.ForeignKey("CubeType_model",null=True, blank=True)
    Hexagon = models.ForeignKey("HexagonType_model",null=True, blank=True)
    #class Meta:
        #unique_together = ("shape","xCoordFromPlateCentre","yCoorDFromPlateCentre","angleRelativeXaxis","Stiffness","Cylinder","Cube","Hexagon","Hair")
    def __unicode__(self):
        return "id: %s" % (self.uuid,)

class plateConfigurationType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    WATER = 'W'
    GELATIN = 'G'
    AGAR = 'A'
    BOTTOMMATERIALTYPE = (        
            (WATER,"water"),
            (GELATIN,"gelatin"),
            (AGAR,"agar"),
    )    
    lid = models.BooleanField(blank=False,default=False)
    bottomMaterial = models.CharField (max_length=60, blank=False,choices=BOTTOMMATERIALTYPE, default=AGAR)
    dryness = models.FloatField(blank=False,validators=[MinValueValidator(0)])
    CYLINDER = 'CY'
    CUBE = 'CU'
    HEXAGON = 'HE'
    SHAPETYPE = (        
        (CYLINDER,"cylinder"),
        (CUBE,"cube"),
        (HEXAGON,"hexagon"),             
    )    
    shape = models.CharField(max_length=60, blank=False,choices=SHAPETYPE, default=CYLINDER)
    Cylinder = models.ForeignKey("CylinderType_model",null=True, blank=True)
    Cube = models.ForeignKey("CubeType_model",null=True, blank=True)
    Hexagon = models.ForeignKey("HexagonType_model",null=True, blank=True)  
    #class Meta:
        #unique_together = ("lid","bottomMaterial","dryness","shape","Cylinder","Cube","Hexagon")
    
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

class CubeType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    depth = models.FloatField(validators=[MinValueValidator(0)],blank=False)
    side1Length = models.FloatField(validators=[MinValueValidator(0)],blank=False)
    side2Length = models.FloatField(validators=[MinValueValidator(0)],blank=False)
    #class Meta:
        #unique_together = ("depth", "side1Length", "side2Length")
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

class CylinderType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    length = models.FloatField(validators=[MinValueValidator(0)], blank=False)
    radius = models.FloatField(validators=[MinValueValidator(0)], blank=False)

    #class Meta:
        #unique_together = ("length", "radius")
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

class HexagonType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    depth = models.FloatField(validators=[MinValueValidator(0)],blank=False)
    sideLength = models.FloatField(validators=[MinValueValidator(0)],blank=False)    
    #class Meta:
        #unique_together = ("depth", "sideLength")
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

##### EXPERIMENT ####

class experimentType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    #It is possible to have different elements of interaction    
    description = models.TextField(max_length=1000, blank=True)
    experimentDuration = models.PositiveIntegerField(blank=False, default=10000)
#   The following ManyToManyField relations do not have an explicit definition table since we do not see need to associate extra data to the relationship
#   https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ManyToManyField
    #    
    #GE: Check how can we ensure that at least one of them is defined
    #
    interactionAtSpecificTime = models.ManyToManyField("interactionAtSpecificTimeType_model",blank=True, null=True )
    interactionFromt0tot1 = models.ManyToManyField("interactionFromt0tot1Type_model",blank=True, null=True)
    experimentWideConf = models.ManyToManyField("experimentWideConfType_model",blank=True, null=True)
    #class Meta:
        #unique_together = ()
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

## Experiments at specific time
class interactionAtSpecificTimeType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    # Only one of them at each object
    #name = models.CharField(max_length=60, blank=True)
    description = models.TextField(max_length=1000, blank=True, default='No description provided')
    eventTime = models.FloatField(blank=False, default=100)
    MECHANOSENSATION = 'MS'
    CHEMOTAXIS ='CT'
    TERMOTAXIS ='TT'
    GALVANOTAXIS = 'GT'
    PHOTOTAXIS = 'PT'
    EXPERIMENTCATEGORY = ( 
        (MECHANOSENSATION,"mechanosensation"),
        (CHEMOTAXIS,"chemotaxis"),
        (TERMOTAXIS,"termotaxis"),
        (GALVANOTAXIS,"galvanotaxis"),
        (PHOTOTAXIS,"phototaxis"),
    )
    experimentCategory = models.CharField(max_length=60, blank=False,choices=EXPERIMENTCATEGORY, default=MECHANOSENSATION)
    #GE: Revise to force the user to fill one of the followings
    mechanosensation = models.ForeignKey("mechanosensationTimeEventType_model", blank=True, null=True)
    chemotaxis = models.ForeignKey("chemotaxisTimeEventType_model", blank=True, null=True)
    termotaxis = models.ForeignKey("termotaxisTimeEventType_model",  blank=True, null=True)
    galvanotaxis = models.ForeignKey("galvanotaxisTimeEventType_model", blank=True, null=True)
    phototaxis = models.ForeignKey("phototaxisTimeEventType_model", blank=True, null=True)
    #name = models.CharField(max_length=60, blank=True)
    #class Meta:
        #unique_together = ("eventTime","mechanosensation","chemotaxis","termotaxis","galvanotaxis", "phototaxis")
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

class mechanosensationTimeEventType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    description = models.TextField(max_length=1000, blank=True)
    PLATETAP = 'PT'
    DIRECTWORMTOUCH = 'DWT'
    INTERACTIONOPTIONS = (        
        (PLATETAP,"plateTap"),
        (DIRECTWORMTOUCH,"directWormTouch"),
    )    
    interactionType = models.CharField(max_length=60, blank=False,choices=INTERACTIONOPTIONS, default=DIRECTWORMTOUCH)
    directTouch = models.ForeignKey("directTouchType_model", blank=True, null=True)
    plateTap = models.ForeignKey("plateTapType_model", blank=True, null=True)
    #class Meta:
        #unique_together = ()
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

class directTouchType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    EYEBROW = 'EB'
    VONFREYHAIR = 'VFH'
    PLATINIUMWIRE = 'PW'
    TOUCHINSTRUMENTTYPE = (        
            (EYEBROW,"Eyebrow"),
            (VONFREYHAIR,"Von Frey hair"),
            (PLATINIUMWIRE,"Platinium wire"),
    )
    directTouchInstrument = models.CharField(max_length=60, blank=False, choices=TOUCHINSTRUMENTTYPE, default=EYEBROW)    
    touchDistance = models.FloatField(blank=False, validators=[MinValueValidator(0),MaxValueValidator(1.0)])
    touchAngle = models.FloatField(blank=False, validators=[MinValueValidator(0),MaxValueValidator(360)])
    appliedForce = models.FloatField(blank=False,validators=[MinValueValidator(0),
                                    MaxValueValidator(100)])   
    #class Meta:
        #unique_together = ("directTouchInstrument", "appliedForce","touchDistance","touchAngle")
    def __unicode__(self):
        return "id: %s" % (self.uuid, )
    
class plateTapType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    appliedForce = models.FloatField(blank=False,validators=[MinValueValidator(0),
                                    MaxValueValidator(100)]) #In the GUI the max is 1 to reflect 1mN, I'll leave it to 100 to avoid breaking if we make slight changes to support a bit more
    #class Meta:
        #unique_together = ()
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

class chemotaxisTimeEventType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    description = models.TextField(max_length=1000, blank=True)
    DYNAMICDROPTEST = 'DDT'
    CHEMOTAXISOPTIONS = (
        (DYNAMICDROPTEST,"Dynamic drop test"),
    )    
    chemotaxisType = models.CharField(max_length=60, blank=False,choices=CHEMOTAXISOPTIONS, default=DYNAMICDROPTEST)
    dynamicDropTestConf = models.ForeignKey("dynamicDropTestType_model", blank=True, null=True)
    #class Meta:
        #unique_together = ()
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

class staticPointSourceType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    dropQuantity = models.FloatField(blank=False,)    
    chemical = models.ForeignKey("chemicalType_model",blank=False)
    chemicalConcentration = models.FloatField(blank=False)  
    xCoordFromPlateCentre = models.FloatField(blank=False)
    yCoordFromPlateCentre = models.FloatField(blank=False)    
    #class Meta:
        #unique_together = ("dropQuantity","chemical","chemicalConcentration","xCoordFromPlateCentre","yCoordFromPlateCentre")
    def __unicode__(self):
        return "id: %s" % (self.uuid, )


class dynamicDropTestType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    dropQuantity = models.FloatField(blank=False,)
    chemical = models.ForeignKey("chemicalType_model",blank=False)
    chemicalConcentration = models.FloatField(blank=False)
    xCoordFromPlateCentre = models.FloatField(blank=False)
    yCoordFromPlateCentre = models.FloatField(blank=False)
    #class Meta:
        #unique_together = ("dropQuantity","chemical","chemicalConcentration","xCoordFromPlateCentre","yCoordFromPlateCentre")
    def __unicode__(self):
        return "id: %s" % (self.uuid, )
    
class chemicalType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    '''
    From NeuronsIDtable-NTU-EditV3.xlsx (Si elegans GDrive)
        lysine
        cAMP
        biotin
        Na+
        Cl-
        heavy metals
        copper
        cadmium
        SDS - Sodium dodecyl sulfate
        quinine
    '''

    NONE = 'None'
    NACL = 'NaCl'
    BIOTIN = 'biotin'
    ETHANOL = 'ethanol'
    BUTANONE = 'butanone'
    COPPERSULPHATE = 'CuSO4'
    SODIUMDODECYLSULFATE = 'SDS - Sodium dodecyl sulfate'
    QUININE = 'quinine'  # C20H24N2O2
    BENZALDEHYDE='benzaldehyde'
    DIACETYL='diacetyl'
    SODIUMAZIDE='NaN3'

    CHEMICALS = (
        (NONE, 'None'),
        (NACL, "Sodium chloride"),
        (BIOTIN, "Biotin"),
        (ETHANOL, "Ethanol"),
        (BUTANONE, "Butanone"),
        (COPPERSULPHATE, "Copper sulphate"),
        (SODIUMDODECYLSULFATE, "Sodium dodecyl sulfate"),
        (QUININE, "Quinine"),
        (BENZALDEHYDE, "Benzaldehyde"),
        (DIACETYL, "Diacetyl"),
        (SODIUMAZIDE, "Sodium azide"),
    )
    diffusionCoefficient = models.FloatField (blank=False, default=0)
    chemical_name = models.CharField(max_length=60, blank=False, choices=CHEMICALS, default=NONE)
    isVolatile = models.BooleanField(blank=False, default=False)
    #GE: How can I make a validation so that In case in not volatile this should be empty     
    volatilitySpeed = models.FloatField(validators=[MinValueValidator(0)],blank=True,null=True) 
    #class Meta:
        #unique_together = ("isVolatile","volatilitySpeed","chemical_name")
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

class termotaxisTimeEventType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    #Add a type selector if an experiment type of this is added
    #Add a foreign key to the defined experiment model
    #class Meta:
        #unique_together = ()
    def __unicode__(self):
        return "id: %s" % (self.uuid )

class pointSourceHeatAvoidanceType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    temperature = models.FloatField(blank=False) #Understood as Celsius
    #We consider worm size as 1
    heatPointDistance = models.FloatField(blank=False, validators=[MinValueValidator(0),MaxValueValidator(1)])

    # heatPointAngle we are not considering it. We will consider that heat is exposed perpendicular to the worm and in a small distance to the worm
    # heatPointAngle = models.FloatField(blank=False, validators=[MinValueValidator(0),MaxValueValidator(6.28318)])
    #class Meta:
        #unique_together = ("temperature","heatPointDistance","heatPointAngle")
    def __unicode__(self):
        return "id: %s" % (self.uuid, )   

class galvanotaxisTimeEventType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    #Add a type selector if an experiment type of this is added
    #Add a foreign key to the defined experiment model
    #class Meta:
        #unique_together = ()
    def __unicode__(self):
        return "id: %s" % (self.uuid, )
    
class phototaxisTimeEventType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    #Add a type selector if an experiment type of this is added
    #Add a foreign key to the defined experiment model
    #class Meta:
        #unique_together = ()
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

class electricShockType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    amplitude = models.FloatField (blank=False)
    shockDuration = models.PositiveIntegerField (blank = False)
    shockFrequency = models.FloatField  (blank = False) # Provide in shocks / sec
    #class Meta:y

        #unique_together = ("waveLength","intensity","lightingPointDistance","lightingPointAngle")
    def __unicode__(self):
        return "id: %s" % (self.uuid, )
    
class pointSourceLightType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    waveLength = models.FloatField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(255)])
    #Ask Kofi Categorical vs Wavelength in 10nm .- 1um?
    intensity = models.FloatField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(255)])
    #Ask Kofi
    #The intensity values used by most neuroscientist range from -3 to 0; (log I/20 mW). In my simulations I have been using values from 0 to 255.
    
    '''The values below refer to the point of the worm, considering the worm as a cylinder
    Worm's size is considered as 1. Therefore, the max value of lightingPointDistance is 1'''
    lightingPointDistance = models.FloatField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(1)])
    #lightingPointAngle we are not considering it. We will consider that light is exposed perpendicular to the plate
    #lightingPointAngle = models.FloatField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(6.28318)])
    '''lightBeamRadius is to have width value to calculate which neurons are lighted, if width=1 all worm is covered'''
    lightBeamRadius = models.FloatField(blank=False, default=0.1, validators=[MinValueValidator(0), MaxValueValidator(1)])
    
    #class Meta:
        #unique_together = ("waveLength","intensity","lightingPointDistance","lightingPointAngle")
    def __unicode__(self):
        return "id: %s" % (self.uuid, )
    
## Experiments from t0 to t1
class interactionFromt0tot1Type_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    description = models.TextField(max_length=1000, blank=True, default='No description provided')
    eventStartTime = models.FloatField(blank=False, default=100)
    eventStopTime = models.FloatField(blank=False, default=1000)
    MECHANOSENSATION = 'MS'
    CHEMOTAXIS ='CT'
    TERMOTAXIS ='TT'
    GALVANOTAXIS = 'GT'
    PHOTOTAXIS = 'PT'
    
    EXPERIMENTCATEGORY = ( 
        (MECHANOSENSATION,"mechanosensation"),
        (CHEMOTAXIS,"chemotaxis"),
        (TERMOTAXIS,"termotaxis"),
        (GALVANOTAXIS,"galvanotaxis"),
        (PHOTOTAXIS,"phototaxis"),
    )
    experimentCategory = models.CharField(max_length=60, blank=False,choices=EXPERIMENTCATEGORY, default=MECHANOSENSATION)
    #GE: Revise to force the user to fill one of the followings
    mechanosensation = models.ForeignKey("mechanosensationTimet0tot1Type_model", blank=True, null=True)
    chemotaxis = models.ForeignKey("chemotaxisTimet0tot1Type_model", blank=True, null=True)
    termotaxis = models.ForeignKey("termotaxisTimet0tot1Type_model", blank=True, null=True)
    galvanotaxis = models.ForeignKey("galvanotaxisTimet0tot1Type_model", blank=True, null=True)
    phototaxis = models.ForeignKey("phototaxisTimet0tot1Type_model", blank=True, null=True)
    #class Meta:
        #unique_together = ("eventStartTime","eventStopTime","mechanosensation","chemotaxis", "termotaxis","galvanotaxis", "phototaxis")
    def __unicode__(self):
        return "id: %s" % (self.uuid, )
    
class mechanosensationTimet0tot1Type_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    #Add a type selector if an experiment type of this is added
    #Add a foreign key to the defined experiment model
    #class Meta:
        #unique_together = ()
    def __unicode__(self):
        return "id: %s" % (self.uuid, )   

    
class termotaxisTimet0tot1Type_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    description = models.TextField(max_length=1000, blank=True)
    TEMPERATURECHANGEINTIME = 'TC'
    POINTSOURCEHEATAVOIDANCE = 'PS'
    TERMOTAXISOPTIONS = (        
        (TEMPERATURECHANGEINTIME,"temperatureChangeInTime"),
        (POINTSOURCEHEATAVOIDANCE,"pointsourceheatavoidance"),
    )    
    termotaxisType = models.CharField(max_length=60, blank=False,choices=TERMOTAXISOPTIONS, default=TEMPERATURECHANGEINTIME)
    temperatureChangeInTime = models.ForeignKey("temperatureChangeInTimeType_model",blank=True, null=True)
    pointSourceHeatAvoidance = models.ForeignKey("pointSourceHeatAvoidanceType_model",blank=True, null=True)
    #class Meta:
        #unique_together = ()
    def __unicode__(self):
        return "id: %s" % (self.uuid, )
class temperatureChangeInTimeType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    initialTemperature = models.FloatField(blank=False,validators=[MinValueValidator(0)])    
    finalTemperature = models.FloatField(blank=False,validators=[MinValueValidator(0)])
    #class Meta:
        #unique_together = ("initialTemperature","finalTemperature")
    def __unicode__(self):
        return "id: %s" % (self.uuid, )
  
class chemotaxisTimet0tot1Type_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    #Add a type selector if an experiment type of this is added
    #Add a foreign key to the defined experiment model
    #class Meta:
        #unique_together = ()
    def __unicode__(self):
        return "id: %s" % (self.uuid )
    
class galvanotaxisTimet0tot1Type_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    description = models.TextField(max_length=1000, blank=True, default='')
    ELECTRICSHOCK = 'ES'
    GALVANOTAXISOPTIONS = (
        (ELECTRICSHOCK,"Electric shocks"),
    )
    galvanotaxisType = models.CharField(max_length=60, blank=False,choices=GALVANOTAXISOPTIONS, default=ELECTRICSHOCK)
    electricShockConf = models.ForeignKey("electricShockType_model", blank=True, null=True)
    def __unicode__(self):
        return "id: %s" % (self.uuid )
class phototaxisTimet0tot1Type_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    description = models.TextField(max_length=1000, blank=True)
    POINTSOURCELIGHT = 'PSL'
    PHOTOTAXISOPTIONS = (
        (POINTSOURCELIGHT,"pointsourcelight"),
    )
    phototaxisType = models.CharField(max_length=60, blank=False,choices=PHOTOTAXISOPTIONS, default=POINTSOURCELIGHT)
    pointSourceLightConf = models.ForeignKey("pointSourceLightType_model", blank=True, null=True)
    #class Meta:
        #unique_together = ()
    def __unicode__(self):
        return "id: %s" % (self.uuid, )


# Experiment wide experiment type

class experimentWideConfType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    description = models.TextField(max_length=1000, blank=True, default='No description provided')
    MECHANOSENSATION ='MS'
    CHEMOTAXIS = 'CT'
    TERMOTAXIS = 'TT'
    GALVANOTAXIS = 'GT'
    PHOTOTAXIS = 'PT'
    EXPERIMENTCATEGORY = ( 
        (MECHANOSENSATION,"mechanosensation"),
        (CHEMOTAXIS,"chemotaxis"),
        (TERMOTAXIS,"termotaxis"),
        (GALVANOTAXIS,"galvanotaxis"),
        (PHOTOTAXIS,"phototaxis"),
    )
    experimentCategory = models.CharField(max_length=60, blank=False,choices=EXPERIMENTCATEGORY, default=MECHANOSENSATION)
    #GE: Revise to force the user to fill one of the followings
    mechanosensation = models.ForeignKey("mechanosensationExpWideType_model", blank=True, null=True)
    chemotaxis = models.ForeignKey("chemotaxisExperimentWideType_model", blank=True, null=True)
    termotaxis = models.ForeignKey("termotaxisExperimentWideType_model", blank=True, null=True)
    galvanotaxis = models.ForeignKey("galvanotaxisExperimentWideType_model", blank=True, null=True)
    phototaxis = models.ForeignKey("phototaxisExperimentWideType_model", blank=True, null=True)
    #class Meta:
        #unique_together = ("mechanosensation","chemotaxis","termotaxis","galvanotaxis","phototaxis")
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

class mechanosensationExpWideType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    #Add a type selector if an experiment type of this is added
    #Add a foreign key to the defined experiment model
    #class Meta:
        #unique_together = ()
    def __unicode__(self):
        return "id: %s" % (self.uuid, )
    

class termotaxisExperimentWideType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    description = models.TextField(max_length=1000, blank=True)
    LINEARTHERMALGRADIENT = 'LT'    
    TERMOTAXIS = (        
        (LINEARTHERMALGRADIENT,"linearThermalGradient"),        
    )    
    termotaxisType = models.CharField(max_length=60, blank=False,choices=TERMOTAXIS, default=LINEARTHERMALGRADIENT)
    linearThermalGradient = models.ForeignKey("linearThermalGradientType_model",blank=True, null=True)    
    #class Meta:
        #unique_together = ()
    def __unicode__(self):
        return "id: %s" % (self.uuid, )
    
class linearThermalGradientType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    temperatureRightHorizonal = models.FloatField(blank=False)
    temperatureLeftHorizontal = models.FloatField(blank=False)
    #class Meta:
        #unique_together = ("temperatureRightHorizonal","temperatureLeftHorizontal")
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

class chemotaxisExperimentWideType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    description = models.TextField(max_length=1000, blank=True)
    STATICPOINTSOURCE = 'SPS'
    CHEMICALQUADRANTS1 = 'CQ1'
    CHEMICALQUADRANTS2 = 'CQ2'
    CHEMICALQUADRANTS4 = 'CQ4'
    OSMOTICRING = 'OR'
    CHEMICALCATEGORY = (
            (STATICPOINTSOURCE,"Static point source"),
            (CHEMICALQUADRANTS1,"chemicalquadrants1"),
            (CHEMICALQUADRANTS2,"chemicalquadrants2"),
            (CHEMICALQUADRANTS4,"chemicalquadrants4"),
            (OSMOTICRING,"osmoticring"),            
        )
    chemicalCategory = models.CharField(max_length=60, blank=False,choices=CHEMICALCATEGORY, default=CHEMICALQUADRANTS1)
    staticPointSourceConf = models.ForeignKey("staticPointSourceType_model", blank=True, null=True)
    chemotaxisQuadrants1 = models.ForeignKey("chemotaxisQuadrantsType_1_model", blank=True, null=True)
    chemotaxisQuadrants2 = models.ForeignKey("chemotaxisQuadrantsType_2_model", blank=True, null=True)
    chemotaxisQuadrants4 = models.ForeignKey("chemotaxisQuadrantsType_4_model", blank=True, null=True)
    osmoticRing = models.ForeignKey("osmoticRingType_model", blank=True, null=True)
    #class Meta:
        #unique_together = ("chemicalCategory","chemotaxisQuadrants","osmoticRing")
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

class chemotaxisQuadrantsType_1_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    quadrantChemical = models.ForeignKey("chemicalType_model",related_name='access_quadrant_1_1', blank=False)
    quadrantChemicalConcentration = models.FloatField(blank=False) #Provide in 1 mol / l = Molar = 1M
    #class Meta:
        #unique_together = ("quadrantsPlacement","numberOfQuadrants","quadrantChemical","quadrantBarrierChemical","quadrantChemicalConcentration","quadrantBarrierChemicalConcentration" )
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

class chemotaxisQuadrantsType_2_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    quadrant_1_Chemical = models.ForeignKey("chemicalType_model",related_name='access_quadrant_2_1', blank=False)
    quadrant_2_Chemical = models.ForeignKey("chemicalType_model",related_name='access_quadrant_2_2', blank=False)
    quadrant_1_ChemicalConcentration = models.FloatField(blank=False)#Provide in 1 mol / l = Molar = 1M
    quadrant_2_ChemicalConcentration = models.FloatField(blank=False)#Provide in 1 mol / l = Molar = 1M
    quadrantBarrierChemical = models.ForeignKey("chemicalType_model",related_name='access_quadrant_2_Barrier', blank=False)
    quadrantBarrierChemicalConcentration = models.FloatField(blank=False)#Provide in 1 mol / l = Molar = 1M
    #class Meta:
        #unique_together = ("quadrantsPlacement","numberOfQuadrants","quadrantChemical","quadrantBarrierChemical","quadrantChemicalConcentration","quadrantBarrierChemicalConcentration" )
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

class chemotaxisQuadrantsType_4_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    quadrant_1_Chemical = models.ForeignKey("chemicalType_model",related_name='access_quadrant_4_1', blank=False)
    quadrant_2_Chemical = models.ForeignKey("chemicalType_model",related_name='access_quadrant_4_2', blank=False)
    quadrant_3_Chemical = models.ForeignKey("chemicalType_model",related_name='access_quadrant_4_3', blank=False)
    quadrant_4_Chemical = models.ForeignKey("chemicalType_model",related_name='access_quadrant_4_4', blank=False)
    quadrant_1_ChemicalConcentration = models.FloatField(blank=False)#Provide in 1 mol / l = Molar = 1M
    quadrant_2_ChemicalConcentration = models.FloatField(blank=False)#Provide in 1 mol / l = Molar = 1M
    quadrant_3_ChemicalConcentration = models.FloatField(blank=False)#Provide in 1 mol / l = Molar = 1M
    quadrant_4_ChemicalConcentration = models.FloatField(blank=False)#Provide in 1 mol / l = Molar = 1M
    quadrantBarrierChemical = models.ForeignKey("chemicalType_model",related_name='access_quadrant_4_Barrier', blank=False)
    quadrantBarrierChemicalConcentration = models.FloatField(blank=False)#Provide in 1 mol / l = Molar = 1M
    #class Meta:
        #unique_together = ("quadrantsPlacement","numberOfQuadrants","quadrantChemical","quadrantBarrierChemical","quadrantChemicalConcentration","quadrantBarrierChemicalConcentration" )
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

class osmoticRingType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    ringChemical = models.ForeignKey("chemicalType_model", blank=False)
    chemicalConcentration = models.FloatField(blank=False) #Provide in 1 mol / l = Molar = 1M
    internalRadius = models.FloatField(blank=False,validators=[MinValueValidator(0)])
    externalRadius = models.FloatField(blank=False,validators=[MinValueValidator(0)])
    #class Meta:
        #unique_together = ("ringChemical","chemicalConcentration","externalRadius","internalRadius")    
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

class galvanotaxisExperimentWideType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    #Add a type selector if an experiment type of this is added
    #Add a foreign key to the defined experiment model
    #class Meta:
        #unique_together = ()
    def __unicode__(self):
        return "id: %s" % (self.uuid, )
    
class phototaxisExperimentWideType_model(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    #Add a type selector if an experiment type of this is added
    #Add a foreign key to the defined experiment model
    #class Meta:
        #unique_together = ()
    def __unicode__(self):
        return "id: %s" % (self.uuid, )

class shareBehaviouralExperiment(models.Model):
    uuid = models.CharField(('Unique Identifier'), max_length=36, primary_key=True, default=generate_new_uuid)
    user = models.ForeignKey(User)
    behaviouralExperiment = models.ForeignKey (behaviourExperimentType_model)    
    shared_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("user","behaviouralExperiment")
    def __unicode__(self):
           return "id: %s_%s" % (self.user,self.behaviouralExperiment )        


