# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0006_item_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='alliance',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(1, 1, 1, 1, 0), auto_now=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='corporation',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(1, 1, 1, 1, 0), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset',
            name='item',
            field=models.ForeignKey(related_name='assets', to='thing.Item'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cloneimplant',
            name='implant',
            field=models.ForeignKey(related_name='implants', to='thing.Implant'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='implant',
            name='item',
            field=models.OneToOneField(related_name='implant', primary_key=True, serialize=False, to='thing.Item'),
            preserve_default=True,
        ),
    ]
