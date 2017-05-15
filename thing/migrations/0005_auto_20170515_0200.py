# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0004_auto_20170515_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='esitoken',
            name='corporationID',
            field=models.IntegerField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='esitoken',
            name='token_type',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='esitoken',
            name='characterID',
            field=models.IntegerField(default=None),
            preserve_default=True,
        ),
    ]
