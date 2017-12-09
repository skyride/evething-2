# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0029_auto_20171209_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='system',
            field=models.ForeignKey(to='thing.System', null=True),
            preserve_default=True,
        ),
    ]
