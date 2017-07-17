# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
import booking.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('behaviouralExperimentDefinition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PE_results',
            fields=[
                ('uuid', models.CharField(default=booking.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('public', models.BooleanField(default=False)),
                ('public_set_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PE_results_files',
            fields=[
                ('uuid', models.CharField(default=booking.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('file_order', models.BigIntegerField()),
                ('results_file', models.FileField(default=b'', upload_to=booking.models.get_upload_path)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('pe_result', models.ForeignKey(related_name='pe_results_files', to='booking.PE_results')),
            ],
            options={
                'ordering': ['created'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RB_results',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('public', models.BooleanField(default=False)),
                ('public_set_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('uuid', models.CharField(default=booking.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('description', models.TextField(max_length=1000, blank=True)),
                ('worm_conf', models.BigIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.BigIntegerField(default=0)),
                ('resume_timestamp', models.BigIntegerField(default=0)),
                ('status', models.CharField(default=b'WAITING', max_length=1000, choices=[(b'WAITING', b'WAITING'), (b'WAITING_START', b'WAITING_START'), (b'CONFIGURING', b'CONFIGURING'), (b'CONFIGURING_INTERFACE_MANAGER', b'CONFIGURING_INTERFACE_MANAGER'), (b'CONFIGURING_PHYSICS_ENGINE', b'CONFIGURING_PHYSICS_ENGINE'), (b'RUNNING', b'RUNNING'), (b'PAUSED', b'PAUSED'), (b'WAITING_UPLOAD', b'WAITING_UPLOAD'), (b'WAITING_CONTEXT', b'WAITING_CONTEXT'), (b'WAITING_RESUME', b'WAITING_RESUME'), (b'DONE', b'DONE'), (b'ABORTED', b'ABORTED')])),
                ('creator', models.ManyToManyField(related_name='reservation_own', to=settings.AUTH_USER_MODEL)),
                ('experiment', models.ForeignKey(related_name='ReservedExperiment', to='behaviouralExperimentDefinition.behaviourExperimentType_model')),
                ('pe_result', models.OneToOneField(related_name='reservation_for_pe_result', null=True, blank=True, to='booking.PE_results')),
                ('rb_result', models.OneToOneField(related_name='reservation_for_rb_result', null=True, blank=True, to='booking.RB_results')),
            ],
            options={
                'ordering': ['created'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='share_pe_results',
            fields=[
                ('uuid', models.CharField(default=booking.models.generate_new_uuid, max_length=36, serialize=False, verbose_name=b'Unique Identifier', primary_key=True)),
                ('shared_date', models.DateTimeField(auto_now_add=True)),
                ('pe_results', models.ForeignKey(to='booking.PE_results')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='share_rb_results',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shared_date', models.DateTimeField(auto_now_add=True)),
                ('rb_results', models.ForeignKey(to='booking.RB_results')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='share_rb_results',
            unique_together=set([('user', 'rb_results')]),
        ),
        migrations.AlterUniqueTogether(
            name='share_pe_results',
            unique_together=set([('user', 'pe_results')]),
        ),
        migrations.AddField(
            model_name='rb_results',
            name='users_with_access',
            field=models.ManyToManyField(related_name='rb_results_accessable', through='booking.share_rb_results', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='pe_results_files',
            unique_together=set([('pe_result', 'file_order')]),
        ),
        migrations.AddField(
            model_name='pe_results',
            name='users_with_access',
            field=models.ManyToManyField(related_name='pe_results_accessable', through='booking.share_pe_results', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
