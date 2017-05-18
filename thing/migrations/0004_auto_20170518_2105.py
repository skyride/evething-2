# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0003_auto_20170517_0027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('character', models.ForeignKey(related_name='clones', to='thing.Character')),
                ('location', models.ForeignKey(to='thing.Station')),
            ],
        ),
        migrations.AlterField(
            model_name='industryjob',
            name='status',
            field=models.IntegerField(choices=[(1, b'Active'), (2, b'Paused (Facility Offline)'), (3, b'Ready'), (102, b'Cancelled'), (104, b'Delivered'), (105, b'Failed'), (999, b'Unknown')]),
        ),
    ]
