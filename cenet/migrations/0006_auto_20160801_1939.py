# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cenet', '0005_auto_20160801_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='neuron',
            name='fpga_is',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cenetwork',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 1, 19, 39, 57, 959000), auto_now=True),
            preserve_default=True,
        ),
    ]
