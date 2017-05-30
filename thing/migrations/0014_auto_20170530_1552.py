# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0013_userprofile_show_clones'),
    ]

    operations = [
        migrations.AddField(
            model_name='clone',
            name='name',
            field=models.CharField(default=b'', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='clone',
            name='location',
            field=models.ForeignKey(related_name='clones', to='thing.Station', null=True),
            preserve_default=True,
        ),
    ]
