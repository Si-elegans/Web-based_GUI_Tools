# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cenet', '0002_cenetwork_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='cenetwork',
            name='jobid',
            field=models.CharField(default=b'', max_length=64),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cenetwork',
            name='lems2fpga_message',
            field=models.TextField(default=False),
            preserve_default=True,
        ),
    ]
