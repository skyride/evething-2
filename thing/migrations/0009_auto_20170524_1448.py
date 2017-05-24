# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0008_auto_20170522_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('players', models.IntegerField(default=0)),
                ('start_time', models.DateTimeField()),
                ('server_version', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='blueprintproduct',
            name='blueprint',
            field=models.ForeignKey(related_name='product', to='thing.Blueprint'),
            preserve_default=True,
        ),
    ]
