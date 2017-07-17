# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behaviouralExperimentDefinition', '0005_auto_20160623_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemicaltype_model',
            name='chemical_name',
            field=models.CharField(default=b'None', max_length=60, choices=[(b'None', b'None'), (b'NaCl', b'Sodium chloride'), (b'biotin', b'Biotin'), (b'ethanol', b'Ethanol'), (b'butanone', b'Butanone'), (b'CuSO4', b'Copper sulphate'), (b'SDS - Sodium dodecyl sulfate', b'Sodium dodecyl sulfate'), (b'quinine', b'Quinine'), (b'benzaldehyde', b'Benzaldehyde'), (b'diacetyl', b'Diacetyl'), (b'NaN3', b'Sodium azide')]),
            preserve_default=True,
        ),
    ]
