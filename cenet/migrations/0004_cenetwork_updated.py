# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cenet', '0003_auto_20160727_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='cenetwork',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 27, 21, 58, 24, 661000), auto_now=True),
            preserve_default=True,
        ),
    ]
