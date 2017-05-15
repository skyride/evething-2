# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0011_auto_20170515_0254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='esitoken',
            name='expires',
        ),
    ]
