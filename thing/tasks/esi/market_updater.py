import requests
import untangle

from datetime import datetime, timedelta

from .apitask import APITask
from evething import local_settings

from thing.models import Item
from django.db.models import Sum, Count, Q
from django.core.paginator import Paginator


# Generates update tasks
class ESI_MarketUpdateSpawner(APITask):
    name = "thing.esi.market_update_spawner"


    def run(self):
        # Get objects to query
        items = Item.objects.filter(
            market_group_id__isnull=False,
            last_updated__lt=datetime.now() - timedelta(days=1)
        ).annotate(
            total_assets = Count('assets'),
            total_implants = Count('implant__implants')
        ).filter(
            Q(total_assets__gt=0) | Q(total_implants__gt=0)
        ).order_by(
            '-total_assets'
        ).all()

        # Generate market update tasks based on a paginated list
        paginator = Paginator(items, 100)
        task = ESI_MarketUpdateTask()
        for i in paginator.page_range:
            page = paginator.page(i)
            type_ids = map(lambda x: x.id, page)
            task.delay(type_ids)


        print "Market Update Spawner called for the update of %s items" % (items.count())



# Performs the actual updates
class ESI_MarketUpdateTask(APITask):
    name = "thing.esi.market_update_task"


    def run(self, type_ids):
        # Get the data from eve-central
        item_count = len(type_ids)
        type_ids = ",".join(map(str, type_ids))
        url = local_settings.PRICE_URL % type_ids
        r = requests.get(url)
        tree = untangle.parse(r.text)

        # Iterate over tree
        for item in tree.evec_api.marketstat.type:
            db_item = Item.objects.get(id=item['id'])
            db_item.sell_price = item.sell.percentile.cdata
            db_item.buy_price = item.buy.percentile.cdata
            db_item.save()

        print "Finished market update request of %s items" % item_count
