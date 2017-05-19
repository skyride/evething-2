# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blueprintproduct',
            name='item',
            field=models.ForeignKey(to='thing.Item', db_constraint=False),
        ),
    ]
