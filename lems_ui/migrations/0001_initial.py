# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lems2FpgaJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sim_type', models.PositiveIntegerField()),
                ('status', models.PositiveIntegerField()),
                ('lems2fpga_code', models.PositiveIntegerField(null=True, blank=True)),
                ('lems2fpga_message', models.TextField(null=True, blank=True)),
                ('lems2fpga_job_id', models.TextField(null=True, blank=True)),
                ('out_of_date', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LemsElement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('lems_elem', models.CharField(max_length=256)),
                ('description', models.TextField(null=True, blank=True)),
                ('public', models.BooleanField(default=False)),
                ('xml', models.TextField()),
                ('dynamics_text', models.TextField(null=True, blank=True)),
                ('from_file', models.CharField(max_length=256)),
                ('extends', models.CharField(max_length=256, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LemsModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('public', models.BooleanField(default=False)),
                ('json', models.TextField()),
                ('model_type', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LemsTypeTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ParameterisedModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('json_data', models.TextField()),
                ('model', models.ForeignKey(to='lems_ui.LemsModel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='share_LemsModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shared_date', models.DateTimeField(auto_now_add=True)),
                ('lemsModel', models.ForeignKey(to='lems_ui.LemsModel')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='share_lemsmodel',
            unique_together=set([('user', 'lemsModel')]),
        ),
        migrations.AddField(
            model_name='lemselement',
            name='tags',
            field=models.ManyToManyField(to='lems_ui.LemsTypeTag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lems2fpgajob',
            name='lems_model',
            field=models.ForeignKey(to='lems_ui.LemsModel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lems2fpgajob',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
