# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0010_serverstatus_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='characterconfig',
            name='show_jumpclones',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
