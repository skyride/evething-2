# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0014_auto_20170530_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractitem',
            name='contract_id',
        ),
        migrations.AddField(
            model_name='contractitem',
            name='contract',
            field=models.ForeignKey(default=None, to='thing.Contract'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contract',
            name='buyout',
            field=models.DecimalField(default=0, max_digits=15, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='arg_id',
            field=models.BigIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='arg_name',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='owner1_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='owner2_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='reason',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='tax_amount',
            field=models.DecimalField(default=0, max_digits=14, decimal_places=2),
            preserve_default=True,
        ),
    ]
