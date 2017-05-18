# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0004_auto_20170518_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='CloneImplant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clone', models.ForeignKey(related_name='implants', to='thing.Clone')),
                ('item', models.ForeignKey(to='thing.Item')),
            ],
        ),
    ]
