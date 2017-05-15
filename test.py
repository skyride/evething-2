from thing.esi import ESI
from thing.models.esitoken import ESIToken

token = ESIToken.objects.get(name="Capri Sun KraftFoods")
api = ESI(token)
#api._refresh_access_token()
#print api.get("/characters/93417038/assets/")
#print api.get("/characters/93637573/assets/")
print api.get("/characters/$id/clones")
#print api.post("/characters/$id/cspa/", data={"characters": [93637573]})
