# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0013_esitoken_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esitoken',
            name='character',
            field=models.OneToOneField(related_name='esitoken', null=True, to='thing.Character'),
            preserve_default=True,
        ),
    ]
