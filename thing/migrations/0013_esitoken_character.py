# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0012_remove_esitoken_expires'),
    ]

    operations = [
        migrations.AddField(
            model_name='esitoken',
            name='character',
            field=models.OneToOneField(null=True, to='thing.Character'),
            preserve_default=True,
        ),
    ]
