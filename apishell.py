from thing.esi import ESI
from thing.models.esitoken import ESIToken
from thing.tasks import ESI_CharacterInfo

token = ESIToken.objects.get(name="Capri Sun KraftFoods")
