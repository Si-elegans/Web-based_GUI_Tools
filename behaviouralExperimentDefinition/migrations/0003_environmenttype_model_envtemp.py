# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behaviouralExperimentDefinition', '0002_remove_pointsourceheatavoidancetype_model_heatpointangle'),
    ]

    operations = [
        migrations.AddField(
            model_name='environmenttype_model',
            name='envTemp',
            field=models.FloatField(default=20, verbose_name=b'Environmental Temperature'),
            preserve_default=True,
        ),
    ]
