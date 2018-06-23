from datetime import datetime, timedelta

from .apitask import APITask

from evething import local_settings

from thing.esi import ESI
from thing.models import ESIToken
from thing.tasks.esi import ESI_CharacterInfo


class ESI_ClearInvalidTokens(APITask):
    name = "thing.esi.clear_invalid_keys"


    def run(self):
        # Generate async update tasks for any ESI Token that hasn't been updated recently
        tokens = ESIToken.objects.filter(
            status=True
        )
        deleted = 0
        for token in tokens:
            api = ESI(token)
            if not api._refresh_access_token():
                print "Deleting token for %s" % token.character.name
                token.delete()
                deleted = deleted + 1
        print "Cleared %s ESI tokens" % deleted