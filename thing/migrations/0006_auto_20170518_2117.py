# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0005_cloneimplant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clone',
            name='location',
            field=models.ForeignKey(to='thing.Station', null=True),
        ),
    ]
