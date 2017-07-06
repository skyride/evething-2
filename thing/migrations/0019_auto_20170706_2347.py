# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0018_contract_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractitem',
            name='contract',
            field=models.ForeignKey(related_name='items', to='thing.Contract'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contractitem',
            name='included',
            field=models.BooleanField(default=False, db_index=True),
            preserve_default=True,
        ),
    ]
