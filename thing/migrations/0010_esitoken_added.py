# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0009_auto_20170515_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='esitoken',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 15, 2, 49, 34, 563790), auto_now_add=True),
            preserve_default=False,
        ),
    ]
