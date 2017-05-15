import json

from .apitask import APITask

from thing.esi import ESI
from thing.models import Character, CharacterConfig, CharacterDetails, Item, System, Station

# This task effectively replaces the characterInfo and characterSheet calls
class ESI_CharacterInfo(APITask):
    name = "thing.esi.character_info"
    api = None

    def run(self, token_id):
        self.api = self.get_api(token_id)

        # Try for wallets to test our access
        wallets = self.api.get("/characters/$id/wallets/")
        if wallets == None:
            return None

        characterID = self.api.token.characterID
        public = self.api.get("/characters/$id/")

        # Get or create character object
        try:
            character = Character.objects.select_related('config', 'corporation', 'details').get(pk=characterID)
        except Character.DoesNotExist:
            character = Character()
            character.id = characterID
        character.name = public['name']

        # Get or create the detail/config objects
        try:
            charConfig = CharacterConfig.objects.get(character=character)
        except CharacterConfig.DoesNotExist:
            charConfig = CharacterConfig(character=character)

        try:
            charDetails = CharacterDetails.objects.get(character=character)
        except CharacterDetails.DoesNotExist:
            charDetails = CharacterDetails(character=character)


        # Perform the rest of the calls
        clones = self.api.get("/characters/$id/clones/")
        location = self.api.get("/characters/$id/location/")
        ship = self.api.get("/characters/$id/ship/")

        # Populate the database
        charDetails.wallet_balance = (wallet for wallet in wallets if wallet['wallet_id'] == 1000).next()['balance']
        # Lmao ESI doesn't have character attributes
        charDetails.cha_attribute = 1
        charDetails.int_attribute = 1
        charDetails.mem_attribute = 1
        charDetails.per_attribute = 1
        charDetails.wil_attribute = 1

        charDetails.security_status = public['security_status']
        charDetails.last_known_location = self.last_known_location(location)
        charDetails.ship_name = ship['ship_name']
        charDetails.ship_item = Item.objects.get(id=ship['ship_type_id'])

        # Save
        character.save()
        charDetails.save()
        charConfig.save()


    # Generates the last known location string
    def last_known_location(self, location):
        # Check for undocked in space
        if len(location) == 1:
            return System.objects.get(id=location['solar_system_id']).name

        if "station_id" in location:
            return Station.objects.get(id=location['station_id']).name

        if "structure_id" in location:
            try:
                structure = self.api.get("/universe/structures/%s/" % location['structure_id'])
                return structure['name']
            except Exception:
                return ""

        return ""
