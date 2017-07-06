# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0017_auto_20170706_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='name',
            field=models.CharField(default=b'', max_length=64),
            preserve_default=True,
        ),
    ]
