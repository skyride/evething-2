# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0020_auto_20170707_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='characterdetails',
            name='jump_fatigue_expire_date',
            field=models.DateTimeField(default=None, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='characterdetails',
            name='last_jump_date',
            field=models.DateTimeField(default=None, null=True),
            preserve_default=True,
        ),
    ]
