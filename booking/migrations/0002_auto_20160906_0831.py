# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='error_admin_updates',
            field=models.TextField(default=b'', max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reservation',
            name='error_code',
            field=models.TextField(default=b'', max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(default=b'WAITING', max_length=1000, choices=[(b'WAITING', b'WAITING'), (b'WAITING_START', b'WAITING_START'), (b'CONFIGURING', b'CONFIGURING'), (b'CONFIGURING_INTERFACE_MANAGER', b'CONFIGURING_INTERFACE_MANAGER'), (b'CONFIGURING_PHYSICS_ENGINE', b'CONFIGURING_PHYSICS_ENGINE'), (b'RUNNING', b'RUNNING'), (b'PAUSED', b'PAUSED'), (b'WAITING_UPLOAD', b'WAITING_UPLOAD'), (b'WAITING_CONTEXT', b'WAITING_CONTEXT'), (b'WAITING_RESUME', b'WAITING_RESUME'), (b'DONE', b'DONE'), (b'ABORTED', b'ABORTED'), (b'ERROR', b'ERROR')]),
            preserve_default=True,
        ),
    ]
