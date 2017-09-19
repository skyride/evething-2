# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0027_auto_20170918_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='ref_type',
            field=models.CharField(max_length=64, db_index=True),
            preserve_default=True,
        ),
    ]
