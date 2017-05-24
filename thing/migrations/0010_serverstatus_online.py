# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0009_auto_20170524_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverstatus',
            name='online',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
