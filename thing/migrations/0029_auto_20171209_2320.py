# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0028_auto_20170919_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='item',
            field=models.ForeignKey(default=None, to='thing.Item', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='station',
            name='name',
            field=models.CharField(default=b'**UNKNOWN**', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='station',
            name='system',
            field=models.ForeignKey(default=None, to='thing.System', null=True),
            preserve_default=True,
        ),
    ]
