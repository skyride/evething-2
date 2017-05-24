import json

from thing.esi import ESI
from thing.models import *
from thing.tasks.esi import *

token = ESIToken.objects.get(name="Irn Bru AGBarr")
api = ESI(token)
#api._refresh_access_token()
#print api.get("/characters/93417038/assets/")
#print api.get("/characters/93637573/assets/")
#print api.get("/characters/$id/clones")
#print api.post("/characters/$id/cspa/", data={"characters": [93637573]})

#task = ESI_CharacterInfo()
#task.run(token.id)
#task = ESI_MarketUpdateSpawner()
#task = ESI_AllianceUpdateTask()
#task.run()
#ESI_ServerStatus().run()

#print Alliance.get_or_create(386292982)

#for token in ESIToken.objects.all():
#    print token.name
#    task.run(token.id)

#print json.dumps(api.get("/characters/$id/standings/"))
