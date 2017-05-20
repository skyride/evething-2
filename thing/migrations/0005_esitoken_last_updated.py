# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0004_station_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='esitoken',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(1, 1, 1, 1, 0), auto_now=True),
            preserve_default=True,
        ),
    ]
