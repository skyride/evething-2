# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0008_auto_20170515_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esitoken',
            name='characterID',
            field=models.IntegerField(default=None, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='esitoken',
            name='corporationID',
            field=models.IntegerField(default=None, null=True),
            preserve_default=True,
        ),
    ]
