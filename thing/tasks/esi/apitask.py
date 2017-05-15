from celery import Task
from celery.task.control import broadcast
from celery.utils.log import get_task_logger

from thing.models.esitoken import ESIToken
from thing.esi import ESI


class APITask(Task):
    abstract = True

    def get_api(self, token_id):
        token = ESIToken.objects.get(id=token_id)
        return ESI(token)
