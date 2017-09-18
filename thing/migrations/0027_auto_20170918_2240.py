# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0026_auto_20170918_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esitoken',
            name='account',
            field=models.ForeignKey(related_name='tokens', on_delete=django.db.models.deletion.SET_NULL, default=None, to='thing.EveAccount', null=True),
            preserve_default=True,
        ),
    ]
