# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behaviouralExperimentDefinition', '0004_auto_20160623_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experimenttype_model',
            name='experimentDuration',
            field=models.PositiveIntegerField(default=10000),
            preserve_default=True,
        ),
    ]
