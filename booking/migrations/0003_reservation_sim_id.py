# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20160906_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='sim_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
