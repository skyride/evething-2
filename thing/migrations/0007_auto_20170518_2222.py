# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0006_auto_20170518_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterskill',
            name='character',
            field=models.ForeignKey(related_name='skills', to='thing.Character'),
        ),
    ]
