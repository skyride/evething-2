# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thing', '0010_esitoken_added'),
    ]

    operations = [
        migrations.RenameField(
            model_name='esitoken',
            old_name='expires_on',
            new_name='expires',
        ),
        migrations.AddField(
            model_name='esitoken',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
