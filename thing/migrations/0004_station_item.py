# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0003_auto_20170519_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='item',
            field=models.ForeignKey(to='thing.Item', null=True),
            preserve_default=True,
        ),
    ]
