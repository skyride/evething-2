# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0003_esitoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='esitoken',
            name='access_token',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='esitoken',
            name='refresh_token',
            field=models.CharField(default='', max_length=320),
            preserve_default=False,
        ),
    ]
