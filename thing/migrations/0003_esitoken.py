# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0002_auto_20160126_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='ESIToken',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('status', models.BooleanField(default=True)),
                ('characterID', models.IntegerField()),
                ('name', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
