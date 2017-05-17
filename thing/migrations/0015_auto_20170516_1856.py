# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0014_auto_20170515_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='lastupdated',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 16, 18, 56, 37, 155399), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='station',
            name='structure',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='station',
            name='id',
            field=models.BigIntegerField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
