# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0012_characterdetails_plex_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='show_clones',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
