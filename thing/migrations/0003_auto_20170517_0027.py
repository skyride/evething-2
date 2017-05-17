# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0002_auto_20170517_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='system',
            field=models.ForeignKey(blank=True, to='thing.System', null=True),
            preserve_default=True,
        ),
    ]
