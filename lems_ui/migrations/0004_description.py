# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lems_ui', '0003_lib_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='lemsmodel',
            name='description',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='lemselement',
            name='library_public',
        ),
        migrations.RemoveField(
            model_name='lemsmodel',
            name='library_public',
        ),
        migrations.AlterField(
            model_name='lemselement',
            name='tags',
            field=models.ManyToManyField(to='lems_ui.LemsTypeTag', blank=True),
            preserve_default=True,
        ),
    ]
