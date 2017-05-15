# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0005_auto_20170515_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='esitoken',
            name='expires_on',
            field=models.DateField(default="1970-01-01"),
            preserve_default=False,
        ),
    ]
