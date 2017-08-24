from datetime import datetime, timedelta

from .apitask import APITask

from evething import local_settings

from thing.models import ESIToken
from thing.tasks.esi import ESI_CharacterInfo


class ESI_CharacterUpdateSpawner(APITask):
    name = "thing.esi.character_update_spawner"


    def run(self):
        # Generate async update tasks for any ESI Token that hasn't been updated recently
        tokens = ESIToken.objects.filter(
            status=True,
            last_updated__lte=datetime.now() - timedelta(minutes=local_settings.ESI_UPDATE_INTERVAL)
        )
        for token in tokens:
            ESI_CharacterInfo().delay(token.id)
            print "Queued token update for token id %s" % token.id
            token.save()
