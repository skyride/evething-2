# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0019_auto_20170706_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='name',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
    ]
