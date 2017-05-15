# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0007_auto_20170515_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esitoken',
            name='expires_on',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
