import json

from .apitask import APITask

from thing.esi import ESI
from thing.models import Character, CharacterConfig, CharacterDetails, Item, System, Station, \
                         CharacterSkill, SkillQueue, Corporation, Faction, FactionStanding, \
                         CorporationStanding

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

        ## Character Data
        characterID = self.api.token.characterID
        public = self.api.get("/characters/$id/")

        # Get or create character object
        try:
            character = Character.objects.select_related('config', 'corporation', 'details').get(pk=characterID)
        except Character.DoesNotExist:
            character = Character()
            character.id = characterID
        character.name = public['name']
        character.corporation = Corporation.get_or_create(public['corporation_id'])

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
        #clones = self.api.get("/characters/$id/clones/")
        location = self.api.get("/characters/$id/location/")
        ship = self.api.get("/characters/$id/ship/")

        # Populate the database
        balance = float((wallet for wallet in wallets if wallet['wallet_id'] == 1000).next()['balance']) / 100
        charDetails.wallet_balance = balance
        # Lmao ESI doesn't have character attributes yet
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
        self.api.token.character = character
        self.api.token.save()


        ## Skills
        skills = self.api.get("/characters/$id/skills/")
        for skill in skills['skills']:
            db_skill = CharacterSkill.objects.filter(character=character, skill_id=skill['skill_id'])
            if len(db_skill) == 1:
                db_skill = db_skill[0]
            else:
                db_skill = CharacterSkill(character=character, skill_id=skill['skill_id'])

            db_skill.level = skill['current_skill_level']
            db_skill.points = skill['skillpoints_in_skill']
            db_skill.save()

        queue = self.api.get("/characters/$id/skillqueue/")
        try:
            for skill in queue:
                db_skill = SkillQueue.objects.filter(character=character, skill=skill['skill_id'])
                if len(db_skill) == 1:
                    db_skill = db_skill[0]
                else:
                    db_skill = SkillQueue(character=character, skill_id=skill['skill_id'])

                db_skill.start_time = self.parse_api_date(skill['start_date'])
                db_skill.end_time = self.parse_api_date(skill['finish_date'])
                db_skill.start_sp = skill['training_start_sp']
                db_skill.end_sp = skill['level_end_sp']
                db_skill.to_level = skill['finished_level']
                db_skill.save()

            # Remove skills that are no longer in queue
            queue_map = map(lambda x: x['skill_id'], queue)
            SkillQueue.objects.filter(character=character).exclude(skill_id__in=queue_map).delete()
        except KeyError:
            # This character isn't training, wipe the queue
            SkillQueue.objects.filter(character=character).delete()


        ## Standings
        standings = self.api.get("/characters/$id/standings/")

        factions = filter(lambda x: x['from_type'] == "faction", standings)
        for faction in factions:
            factionstanding = FactionStanding.objects.filter(character=character, faction_id=faction['from_id'])
            if len(factionstanding) == 1:
                factionstanding = factionstanding[0]
            else:
                factionstanding = FactionStanding(character=character, faction_id=faction['from_id'])

            factionstanding.standing = faction['standing']
            factionstanding.save()

        npc_corps = filter(lambda x: x['from_type'] == "npc_corp", standings)
        for npc_corp in npc_corps:
            corpstanding = CorporationStanding.objects.filter(character=character, corporation_id=npc_corp['from_id'])
            if len(corpstanding) == 1:
                corpstanding = corpstanding[0]
            else:
                corpstanding = CorporationStanding(character=character, corporation_id=npc_corp['from_id'])

            corpstanding.standing = npc_corp['standing']
            corpstanding.save()


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
                str_type = Item.objects.get(id=structure['type_id'])
                return "%s (%s)" % (structure['name'], str_type.name)
            except Exception:
                return ""

        return ""
