# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0030_auto_20171209_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetsummary',
            name='system',
            field=models.ForeignKey(to='thing.System', null=True),
            preserve_default=True,
        ),
    ]
