# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0016_auto_20170706_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractitem',
            name='id',
            field=models.BigIntegerField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
