# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from thing.models import Contract

# We need to delete duplicate contract IDs before we make it a unique field
def delete_contract_duplicates_forward(apps, schema_editor):
    ids = Contract.objects.all().values_list('contract_id', flat=True).distinct()

    for contract_id in ids:
        contracts = Contract.objects.filter(contract_id=contract_id)

        if contracts.count() > 1:
            itercontracts = iter(contracts)
            next(itercontracts)

            for contract in itercontracts:
                contract.delete()


def delete_contract_duplicates_reverse(apps, schema_editor):
    pass



class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0022_auto_20170824_1956'),
    ]

    operations = [
        migrations.RunPython(
            delete_contract_duplicates_forward,
            delete_contract_duplicates_reverse
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_id',
            field=models.IntegerField(unique=True, db_index=True),
            preserve_default=True,
        ),
    ]
