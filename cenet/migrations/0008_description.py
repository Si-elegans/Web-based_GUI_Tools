# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cenet', '0007_auto_20160806_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='cenetwork',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='neuron',
            old_name='fpga_is',
            new_name='fpga_id',
        ),
        migrations.AlterField(
            model_name='cenetwork',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 21, 16, 42, 27, 906840), auto_now=True),
            preserve_default=True,
        ),
    ]
