# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0002_auto_20170519_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailmessage',
            name='to_characters',
            field=models.ManyToManyField(related_name='+', to='thing.Character'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='home_sort_descending',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='home_sort_order',
            field=models.CharField(default=b'totalsp', max_length=12, choices=[(b'charname', b'Character name'), (b'corpname', b'Corporation name'), (b'totalsp', b'Total SP'), (b'wallet', b'Wallet balance')]),
            preserve_default=True,
        ),
    ]
