# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thing', '0024_auto_20170918_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='EveAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=32)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.AlterField(
            model_name='esitoken',
            name='account',
            field=models.ForeignKey(default=None, to='thing.EveAccount', null=True),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
