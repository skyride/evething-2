# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0021_auto_20170824_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='characterdetails',
            old_name='jump_fatigue_expire_date',
            new_name='fatigue_expire_date',
        ),
    ]
