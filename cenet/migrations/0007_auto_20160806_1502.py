# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cenet', '0006_auto_20160801_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='cenetwork',
            name='muscleModel',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cenetwork',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 6, 15, 2, 45, 979000), auto_now=True),
            preserve_default=True,
        ),
    ]
