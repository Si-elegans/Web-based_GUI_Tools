# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behaviouralExperimentDefinition', '0003_environmenttype_model_envtemp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interactionatspecifictimetype_model',
            name='eventTime',
            field=models.FloatField(default=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='interactionfromt0tot1type_model',
            name='eventStartTime',
            field=models.FloatField(default=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='interactionfromt0tot1type_model',
            name='eventStopTime',
            field=models.FloatField(default=1000),
            preserve_default=True,
        ),
    ]
