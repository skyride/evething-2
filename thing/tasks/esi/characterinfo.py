import json

from datetime import datetime, timedelta

from django.db import transaction
from django.db.models import Sum, F, FloatField

from .apitask import APITask

from thing.esi_enums import *
from thing.esi import ESI
from thing.models import Character, CharacterConfig, CharacterDetails, Item, System, Station, \
                         CharacterSkill, SkillQueue, Corporation, Faction, FactionStanding, \
                         CorporationStanding, Asset, System, InventoryFlag, AssetSummary, \
                         IndustryJob, MarketOrder, Clone, CloneImplant

# This task effectively replaces the characterInfo and characterSheet calls
class ESI_CharacterInfo(APITask):
    name = "thing.esi.character_info"
    api = None

    @transaction.atomic
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


        ## Assets
        assets = self.api.get("/characters/$id/assets/")
        asset_map = map(lambda x: x['item_id'], assets)

        for asset in assets:
            db_asset = Asset.objects.filter(asset_id=asset['item_id'])
            if len(db_asset) == 1:
                db_asset = db_asset[0]
            else:
                db_asset = Asset(character=character, asset_id=asset['item_id'], item_id=asset['type_id'])

            # Names aren't in ESI atm for some reason
            db_asset.name = ""
            db_asset.inv_flag_id = PersonalLocationFlagEnum[asset['location_flag']].value

            db_asset.singleton = asset['is_singleton']
            if asset['is_singleton']:
                db_asset.quantity = 1
                db_asset.raw_quantity = -1
            else:
                db_asset.quantity = asset['quantity']
                db_asset.raw_quantity = 0

            # Calculate parent and location
            # Try asset
            if asset['location_id'] in asset_map:
                db_asset.parent = asset['location_id']
                db_asset.station = None
                db_asset.system = None
                db_asset.save()
                continue
            # Try station
            if Station.get_or_create(asset['location_id'], self.api) != None:
                station = Station.objects.get(id=asset['location_id'])
                db_asset.station = station
                db_asset.system_id = station.system_id
                db_asset.save()
                continue
            # Try solar system
            if System.objects.filter(id=asset['location_id']).count() > 0:
                db_asset.station = None
                db_asset.system_id = asset['location_id']
                db_asset.save()
                continue

        # Fix station/system values for parented assets
        def resolve_location(asset):
            if asset.station == None:
                #print "%s/%s" % (asset.parent, asset.asset_id)
                parent = Asset.objects.get(asset_id=asset.parent)
                if parent.station_id != None:
                    asset.station_id = parent.station_id
                    asset.system_id = parent.system_id
                    asset.save()
                    return (parent.station_id, parent.system_id)
                else:
                    station_id, system_id = resolve_location()
                    asset.station_id = station_id
                    asset.system_id = system_id
                    asset.save()
                    return (station_id, system_id)
            else:
                return None

        for asset in Asset.objects.filter(character=character, station=None):
            try:
                resolve_location(asset)
            except Exception:
                pass

        # Delete all assets not in the map
        Asset.objects.filter(character=character).exclude(asset_id__in=asset_map).delete()

        # Rebuild asset summary
        AssetSummary.objects.filter(character=character).delete()
        summaries = Station.objects.filter(asset__character=character).annotate(
                total_items=Sum("asset__quantity"),
                total_volume=Sum(
                    F('asset__quantity') * F('asset__item__volume'), output_field=FloatField()
                ),
                total_value=Sum(
                    F('asset__quantity') * F('asset__item__sell_price'), output_field=FloatField()
                )
        )
        for summary in summaries:
            db_summary = AssetSummary(
                character=character,
                system_id=summary.system_id,
                station_id=summary.id,
                total_items=summary.total_items,
                total_volume=summary.total_volume,
                total_value=summary.total_value
            )
            db_summary.save()


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


        ## Industry
        jobs = self.api.get("/characters/$id/industry/jobs/")
        for job in jobs:
            db_job = IndustryJob.objects.filter(job_id=job['job_id'])
            if len(db_job) == 1:
                db_job = db_job[0]
            else:
                db_job = IndustryJob(
                    job_id=job['job_id'],
                    installer_id=job['installer_id'],
                    activity=job['activity_id'],
                    output_location_id=job['output_location_id'],
                    runs=job['runs'],
                    team_id=0,  # This doesn't exist anymore so it's not in ESI
                    licensed_runs=job['licensed_runs'],
                    duration=job['duration'],
                    start_date=self.parse_api_date(job['start_date']),
                    end_date=self.parse_api_date(job['end_date']),
                    pause_date=datetime(0001, 1, 1, 1, 0),
                    completed_date=datetime(0001, 1, 1, 1, 0),
                    blueprint_id=job['blueprint_type_id'],
                    character=character,
                    corporation=None,
                    product_id=job['product_type_id'],

                    # POSes are getting removed soon so we're just going to
                    # assume the facility is a station/structure
                    system_id=Station.get_or_create(job['facility_id'], self.api).system_id
                )

            # Update other values
            db_job.status = IndustryJobStatusEnum[job['status']].value

            if "completed_date" in job:
                db_job.completed_date = self.parse_api_date(job['completed_date'])
            if "pause_date" in job:
                db_job.pause_date = self.parse_api_date(job['pause_date'])

            db_job.save()


        ## Orders
        orders = self.api.get("/characters/$id/orders/")
        for order in orders:
            db_order = MarketOrder.objects.filter(order_id=order['order_id'])
            if len(db_order) == 1:
                db_order = db_order[0]
            else:
                db_order = MarketOrder(
                    order_id=order['order_id'],
                    character=character,
                    creator_character_id=character.id,
                    escrow=order['escrow'],
                    buy_order=order['is_buy_order'],
                    volume_entered=order['volume_total'],
                    corp_wallet_id=None,
                    item_id=order['type_id'],
                    station=Station.get_or_create(order['location_id'], self.api)
                )

            db_order.price = order['price']
            db_order.total_price = order['price'] * order['volume_remain']
            db_order.volume_remaining = order['volume_remain']
            db_order.minimum_volume = order['min_volume']
            db_order.issued = self.parse_api_date(order['issued'])
            db_order.expires = db_order.issued + timedelta(days=order['duration'])
            db_order.save()


        ## Clones
        clones = self.api.get("/characters/$id/clones/")
        # Delete existing clones
        Clone.objects.filter(character=character).delete()
        if "jump_clones" in clones:
            for clone in clones['jump_clones']:
                db_clone = Clone(
                    character=character,
                    location=Station.get_or_create(clone['location_id'], self.api)
                )
                db_clone.save()

                if "implants" in clone:
                    for implant_id in clone['implants']:
                        db_implant = CloneImplant(
                            clone=db_clone,
                            item_id=implant_id
                        )
                        db_implant.save()



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
