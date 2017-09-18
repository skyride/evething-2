# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0025_auto_20170918_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esitoken',
            name='account',
            field=models.ForeignKey(related_name='tokens', default=None, to='thing.EveAccount', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eveaccount',
            name='user',
            field=models.ForeignKey(related_name='accounts', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='skillqueue',
            name='character',
            field=models.ForeignKey(related_name='skillqueue', to='thing.Character'),
            preserve_default=True,
        ),
    ]
