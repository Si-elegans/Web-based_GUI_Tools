# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lems_ui', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lems2fpgajob',
            name='syn_ids',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
