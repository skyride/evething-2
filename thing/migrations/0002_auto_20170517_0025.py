# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0001_squashed_0015_auto_20170516_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='system',
            field=models.ForeignKey(to='thing.System', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='esitoken',
            name='access_token',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='esitoken',
            name='added',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='esitoken',
            name='refresh_token',
            field=models.CharField(max_length=320),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='esitoken',
            name='token_type',
            field=models.CharField(max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='esitoken',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
