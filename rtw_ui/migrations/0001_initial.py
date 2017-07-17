# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cenet', '0005_auto_20160801_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='RTW',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('variable', models.CharField(max_length=256)),
                ('startTime', models.FloatField()),
                ('endTime', models.FloatField()),
                ('samplingInterval', models.FloatField()),
                ('neuron', models.ForeignKey(to='cenet.Neuron')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RTW_CONF',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('public', models.BooleanField(default=False)),
                ('json', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('network', models.ForeignKey(to='cenet.CENetwork')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
