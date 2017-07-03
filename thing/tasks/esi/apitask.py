import datetime

from celery import Task
from celery.task.control import broadcast
from celery.utils.log import get_task_logger

from thing.models.esitoken import ESIToken
from thing.esi import ESI


class APITask(Task):
    abstract = True

    contract_types = {
        "unknown": "unknown",
        "item_exchange": "Item Exchange",
        "auction": "Auction",
        "courier": "Courier",
        "loan": "Loan"
    }

    contract_states = {
        "outstanding": "Outstanding",
        "in_progress": "In Progress",
        "finished_issuer": "Completed",
        "finished_contractor": "Completed",
        "finished": "Completed",
        "cancelled": "Cancelled",
        "rejected": "Rejected",
        "failed": "Failed",
        "deleted": "Deleted",
        "reversed": "Reversed"
    }

    def get_api(self, token_id):
        token = ESIToken.objects.get(id=token_id)
        return ESI(token)


    def parse_api_date(self, date):
        return datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
