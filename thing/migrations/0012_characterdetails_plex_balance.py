# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0011_characterconfig_show_jumpclones'),
    ]

    operations = [
        migrations.AddField(
            model_name='characterdetails',
            name='plex_balance',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
