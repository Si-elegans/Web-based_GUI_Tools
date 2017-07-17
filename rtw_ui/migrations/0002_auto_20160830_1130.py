# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtw_ui', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rtw_conf',
            name='metadata_init',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rtw_conf',
            name='metadata_rtw',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
