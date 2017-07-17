# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cenet', '0004_cenetwork_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cenetwork',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 1, 16, 39, 40, 234000), auto_now=True),
            preserve_default=True,
        ),
    ]
