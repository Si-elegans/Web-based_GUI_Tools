# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lems_ui', '0002_lems2fpgajob_syn_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='lemselement',
            name='library_public',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lemselement',
            name='component_data',
            field=models.TextField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lemsmodel',
            name='library_public',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
