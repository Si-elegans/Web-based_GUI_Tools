# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import behaviouralExperimentDefinition.models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='behaviourExperimentType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('about', models.CharField(max_length=60, blank=True)),
                ('public', models.BooleanField(default=False)),
                ('public_set_date', models.DateTimeField(default=datetime.datetime.now)),
                ('description', models.TextField(max_length=1000, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(related_name='behaviouralExperiment_own', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='chemicalType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('diffusionCoefficient', models.FloatField(default=0)),
                ('chemical_name', models.CharField(default=b'cAMP', max_length=60, choices=[(b'Lys', b'Lysine'), (b'BIOTIN', b'Biotin'), (b'cAMP', b'Cyclic adenosine monophosphate'), (b'Na+', b'Sodium ion'), (b'Cl-', b'Chlorine ion'), (b'HM', b'Heavy metals'), (b'Cu', b'Copper'), (b'Cd', b'Cadmium'), (b'SDS', b'Sodium dodecyl sulfate'), (b'QUININE', b'Quinine')])),
                ('isVolatile', models.BooleanField(default=False)),
                ('volatilitySpeed', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='chemotaxisExperimentWideType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('description', models.TextField(max_length=1000, blank=True)),
                ('chemicalCategory', models.CharField(default=b'CQ1', max_length=60, choices=[(b'SPS', b'Static point source'), (b'CQ1', b'chemicalquadrants1'), (b'CQ2', b'chemicalquadrants2'), (b'CQ4', b'chemicalquadrants4'), (b'OR', b'osmoticring')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='chemotaxisQuadrantsType_1_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('quadrantChemicalConcentration', models.FloatField()),
                ('quadrantChemical', models.ForeignKey(related_name='access_quadrant_1_1', to='behaviouralExperimentDefinition.chemicalType_model')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='chemotaxisQuadrantsType_2_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('quadrant_1_ChemicalConcentration', models.FloatField()),
                ('quadrant_2_ChemicalConcentration', models.FloatField()),
                ('quadrantBarrierChemicalConcentration', models.FloatField()),
                ('quadrantBarrierChemical', models.ForeignKey(related_name='access_quadrant_2_Barrier', to='behaviouralExperimentDefinition.chemicalType_model')),
                ('quadrant_1_Chemical', models.ForeignKey(related_name='access_quadrant_2_1', to='behaviouralExperimentDefinition.chemicalType_model')),
                ('quadrant_2_Chemical', models.ForeignKey(related_name='access_quadrant_2_2', to='behaviouralExperimentDefinition.chemicalType_model')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='chemotaxisQuadrantsType_4_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('quadrant_1_ChemicalConcentration', models.FloatField()),
                ('quadrant_2_ChemicalConcentration', models.FloatField()),
                ('quadrant_3_ChemicalConcentration', models.FloatField()),
                ('quadrant_4_ChemicalConcentration', models.FloatField()),
                ('quadrantBarrierChemicalConcentration', models.FloatField()),
                ('quadrantBarrierChemical', models.ForeignKey(related_name='access_quadrant_4_Barrier', to='behaviouralExperimentDefinition.chemicalType_model')),
                ('quadrant_1_Chemical', models.ForeignKey(related_name='access_quadrant_4_1', to='behaviouralExperimentDefinition.chemicalType_model')),
                ('quadrant_2_Chemical', models.ForeignKey(related_name='access_quadrant_4_2', to='behaviouralExperimentDefinition.chemicalType_model')),
                ('quadrant_3_Chemical', models.ForeignKey(related_name='access_quadrant_4_3', to='behaviouralExperimentDefinition.chemicalType_model')),
                ('quadrant_4_Chemical', models.ForeignKey(related_name='access_quadrant_4_4', to='behaviouralExperimentDefinition.chemicalType_model')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='chemotaxisTimeEventType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('description', models.TextField(max_length=1000, blank=True)),
                ('chemotaxisType', models.CharField(default=b'DDT', max_length=60, choices=[(b'DDT', b'Dynamic drop test')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='chemotaxisTimet0tot1Type_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='crowdingType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('wormsDistributionInPlate', models.CharField(max_length=60, blank=True)),
                ('wormsInPlate', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CubeType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('depth', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('side1Length', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('side2Length', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CylinderType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('length', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('radius', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='directTouchType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('directTouchInstrument', models.CharField(default=b'EB', max_length=60, choices=[(b'EB', b'Eyebrow'), (b'VFH', b'Von Frey hair'), (b'PW', b'Platinium wire')])),
                ('touchDistance', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1.0)])),
                ('touchAngle', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6.28318)])),
                ('appliedForce', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='dynamicDropTestType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('dropQuantity', models.FloatField()),
                ('chemicalConcentration', models.FloatField()),
                ('xCoordFromPlateCentre', models.FloatField()),
                ('yCoordFromPlateCentre', models.FloatField()),
                ('chemical', models.ForeignKey(to='behaviouralExperimentDefinition.chemicalType_model')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='electricShockType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('amplitude', models.FloatField()),
                ('shockDuration', models.PositiveIntegerField()),
                ('shockFrequency', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='environmentType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('description', models.TextField(max_length=1000, blank=True)),
                ('crowding', models.ForeignKey(to='behaviouralExperimentDefinition.crowdingType_model')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='experimentType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('description', models.TextField(max_length=1000, blank=True)),
                ('experimentDuration', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='experimentWideConfType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('description', models.TextField(default=b'No description provided', max_length=1000, blank=True)),
                ('experimentCategory', models.CharField(default=b'MS', max_length=60, choices=[(b'MS', b'mechanosensation'), (b'CT', b'chemotaxis'), (b'TT', b'termotaxis'), (b'GT', b'galvanotaxis'), (b'PT', b'phototaxis')])),
                ('chemotaxis', models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.chemotaxisExperimentWideType_model', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='galvanotaxisExperimentWideType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='galvanotaxisTimeEventType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='galvanotaxisTimet0tot1Type_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('description', models.TextField(default=b'', max_length=1000, blank=True)),
                ('galvanotaxisType', models.CharField(default=b'ES', max_length=60, choices=[(b'ES', b'Electric shocks')])),
                ('electricShockConf', models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.electricShockType_model', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HexagonType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('depth', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('sideLength', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='interactionAtSpecificTimeType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('description', models.TextField(default=b'No description provided', max_length=1000, blank=True)),
                ('eventTime', models.FloatField()),
                ('experimentCategory', models.CharField(default=b'MS', max_length=60, choices=[(b'MS', b'mechanosensation'), (b'CT', b'chemotaxis'), (b'TT', b'termotaxis'), (b'GT', b'galvanotaxis'), (b'PT', b'phototaxis')])),
                ('chemotaxis', models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.chemotaxisTimeEventType_model', null=True)),
                ('galvanotaxis', models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.galvanotaxisTimeEventType_model', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='interactionFromt0tot1Type_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('description', models.TextField(default=b'No description provided', max_length=1000, blank=True)),
                ('eventStartTime', models.FloatField()),
                ('eventStopTime', models.FloatField()),
                ('experimentCategory', models.CharField(default=b'MS', max_length=60, choices=[(b'MS', b'mechanosensation'), (b'CT', b'chemotaxis'), (b'TT', b'termotaxis'), (b'GT', b'galvanotaxis'), (b'PT', b'phototaxis')])),
                ('chemotaxis', models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.chemotaxisTimet0tot1Type_model', null=True)),
                ('galvanotaxis', models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.galvanotaxisTimet0tot1Type_model', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='linearThermalGradientType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('temperatureRightHorizonal', models.FloatField()),
                ('temperatureLeftHorizontal', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='mechanosensationExpWideType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='mechanosensationTimeEventType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('description', models.TextField(max_length=1000, blank=True)),
                ('interactionType', models.CharField(default=b'DWT', max_length=60, choices=[(b'PT', b'plateTap'), (b'DWT', b'directWormTouch')])),
                ('directTouch', models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.directTouchType_model', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='mechanosensationTimet0tot1Type_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='obstacleLocationType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('xCoordFromPlateCentre', models.FloatField()),
                ('yCoorDFromPlateCentre', models.FloatField()),
                ('Stiffness', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('shape', models.CharField(default=b'CY', max_length=60, choices=[(b'CY', b'cylinder'), (b'CU', b'cube'), (b'HE', b'hexagon')])),
                ('Cube', models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.CubeType_model', null=True)),
                ('Cylinder', models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.CylinderType_model', null=True)),
                ('Hexagon', models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.HexagonType_model', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='osmoticRingType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('chemicalConcentration', models.FloatField()),
                ('internalRadius', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('externalRadius', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('ringChemical', models.ForeignKey(to='behaviouralExperimentDefinition.chemicalType_model')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='phototaxisExperimentWideType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='phototaxisTimeEventType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='phototaxisTimet0tot1Type_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('description', models.TextField(max_length=1000, blank=True)),
                ('phototaxisType', models.CharField(default=b'PSL', max_length=60, choices=[(b'PSL', b'pointsourcelight')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='plateConfigurationType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('lid', models.BooleanField(default=False)),
                ('bottomMaterial', models.CharField(default=b'A', max_length=60, choices=[(b'W', b'water'), (b'G', b'gelatin'), (b'A', b'agar')])),
                ('dryness', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('shape', models.CharField(default=b'CY', max_length=60, choices=[(b'CY', b'cylinder'), (b'CU', b'cube'), (b'HE', b'hexagon')])),
                ('Cube', models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.CubeType_model', null=True)),
                ('Cylinder', models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.CylinderType_model', null=True)),
                ('Hexagon', models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.HexagonType_model', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='plateTapType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('appliedForce', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='pointSourceHeatAvoidanceType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('temperature', models.FloatField()),
                ('heatPointDistance', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('heatPointAngle', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6.28318)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='pointSourceLightType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('waveLength', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(255)])),
                ('intensity', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(255)])),
                ('lightingPointDistance', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('lightBeamRadius', models.FloatField(default=0.1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='shareBehaviouralExperiment',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('shared_date', models.DateTimeField(auto_now_add=True)),
                ('behaviouralExperiment', models.ForeignKey(to='behaviouralExperimentDefinition.behaviourExperimentType_model')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='staticPointSourceType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('dropQuantity', models.FloatField()),
                ('chemicalConcentration', models.FloatField()),
                ('xCoordFromPlateCentre', models.FloatField()),
                ('yCoordFromPlateCentre', models.FloatField()),
                ('chemical', models.ForeignKey(to='behaviouralExperimentDefinition.chemicalType_model')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='temperatureChangeInTimeType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('initialTemperature', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('finalTemperature', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='termotaxisExperimentWideType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('description', models.TextField(max_length=1000, blank=True)),
                ('termotaxisType', models.CharField(default=b'LT', max_length=60, choices=[(b'LT', b'linearThermalGradient')])),
                ('linearThermalGradient', models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.linearThermalGradientType_model', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='termotaxisTimeEventType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='termotaxisTimet0tot1Type_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('description', models.TextField(max_length=1000, blank=True)),
                ('termotaxisType', models.CharField(default=b'TC', max_length=60, choices=[(b'TC', b'temperatureChangeInTime'), (b'PS', b'pointsourceheatavoidance')])),
                ('pointSourceHeatAvoidance', models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.pointSourceHeatAvoidanceType_model', null=True)),
                ('temperatureChangeInTime', models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.temperatureChangeInTimeType_model', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='wormDataType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('gender', models.CharField(default=b'FH', max_length=60, choices=[(b'M', b'Male'), (b'FH', b'Female Hermaphrodites')])),
                ('age', models.PositiveIntegerField()),
                ('stageOfLifeCycle', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('timeOffFood', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='wormStatusType_model',
            fields=[
                ('uuid', models.CharField(default=behaviouralExperimentDefinition.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('xCoordFromPlateCentre', models.FloatField()),
                ('yCoorDFromPlateCentre', models.FloatField()),
                ('angleRelativeXaxis', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6.28318)])),
                ('wormData', models.ForeignKey(to='behaviouralExperimentDefinition.wormDataType_model')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='sharebehaviouralexperiment',
            unique_together=set([('user', 'behaviouralExperiment')]),
        ),
        migrations.AddField(
            model_name='phototaxistimet0tot1type_model',
            name='pointSourceLightConf',
            field=models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.pointSourceLightType_model', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mechanosensationtimeeventtype_model',
            name='plateTap',
            field=models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.plateTapType_model', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='interactionfromt0tot1type_model',
            name='mechanosensation',
            field=models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.mechanosensationTimet0tot1Type_model', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='interactionfromt0tot1type_model',
            name='phototaxis',
            field=models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.phototaxisTimet0tot1Type_model', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='interactionfromt0tot1type_model',
            name='termotaxis',
            field=models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.termotaxisTimet0tot1Type_model', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='interactionatspecifictimetype_model',
            name='mechanosensation',
            field=models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.mechanosensationTimeEventType_model', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='interactionatspecifictimetype_model',
            name='phototaxis',
            field=models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.phototaxisTimeEventType_model', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='interactionatspecifictimetype_model',
            name='termotaxis',
            field=models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.termotaxisTimeEventType_model', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experimentwideconftype_model',
            name='galvanotaxis',
            field=models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.galvanotaxisExperimentWideType_model', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experimentwideconftype_model',
            name='mechanosensation',
            field=models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.mechanosensationExpWideType_model', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experimentwideconftype_model',
            name='phototaxis',
            field=models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.phototaxisExperimentWideType_model', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experimentwideconftype_model',
            name='termotaxis',
            field=models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.termotaxisExperimentWideType_model', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experimenttype_model',
            name='experimentWideConf',
            field=models.ManyToManyField(to='behaviouralExperimentDefinition.experimentWideConfType_model', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experimenttype_model',
            name='interactionAtSpecificTime',
            field=models.ManyToManyField(to='behaviouralExperimentDefinition.interactionAtSpecificTimeType_model', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experimenttype_model',
            name='interactionFromt0tot1',
            field=models.ManyToManyField(to='behaviouralExperimentDefinition.interactionFromt0tot1Type_model', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='environmenttype_model',
            name='obstacle',
            field=models.ManyToManyField(to='behaviouralExperimentDefinition.obstacleLocationType_model', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='environmenttype_model',
            name='plateConfiguration',
            field=models.ForeignKey(to='behaviouralExperimentDefinition.plateConfigurationType_model'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='environmenttype_model',
            name='wormStatus',
            field=models.ForeignKey(to='behaviouralExperimentDefinition.wormStatusType_model'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chemotaxistimeeventtype_model',
            name='dynamicDropTestConf',
            field=models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.dynamicDropTestType_model', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chemotaxisexperimentwidetype_model',
            name='chemotaxisQuadrants1',
            field=models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.chemotaxisQuadrantsType_1_model', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chemotaxisexperimentwidetype_model',
            name='chemotaxisQuadrants2',
            field=models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.chemotaxisQuadrantsType_2_model', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chemotaxisexperimentwidetype_model',
            name='chemotaxisQuadrants4',
            field=models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.chemotaxisQuadrantsType_4_model', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chemotaxisexperimentwidetype_model',
            name='osmoticRing',
            field=models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.osmoticRingType_model', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chemotaxisexperimentwidetype_model',
            name='staticPointSourceConf',
            field=models.ForeignKey(blank=True, to='behaviouralExperimentDefinition.staticPointSourceType_model', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='behaviourexperimenttype_model',
            name='environmentDefinition',
            field=models.ForeignKey(to='behaviouralExperimentDefinition.environmentType_model'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='behaviourexperimenttype_model',
            name='experimentDefinition',
            field=models.ForeignKey(to='behaviouralExperimentDefinition.experimentType_model'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='behaviourexperimenttype_model',
            name='users_with_access',
            field=models.ManyToManyField(related_name='behaviouralExperiment_accessable', through='behaviouralExperimentDefinition.shareBehaviouralExperiment', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
