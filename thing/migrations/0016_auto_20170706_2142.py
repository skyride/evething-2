# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0015_auto_20170706_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractitem',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contractitem',
            name='raw_quantity',
            field=models.IntegerField(default=None, null=True),
            preserve_default=True,
        ),
    ]
