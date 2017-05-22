# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0007_auto_20170520_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='cycle_time',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pin',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(1, 1, 1, 1, 0)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pin',
            name='installed',
            field=models.DateTimeField(default=datetime.datetime(1, 1, 1, 1, 0)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pin',
            name='last_launched',
            field=models.DateTimeField(default=datetime.datetime(1, 1, 1, 1, 0)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pin',
            name='quantity_per_cycle',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pin',
            name='schematic',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
