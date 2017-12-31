from .apitask import APITask

from thing.esi import ESI

from thing.models import ServerStatus


class ESI_ServerStatus(APITask):
    name = "thing.esi.server_status"
    api = None


    def run(self):
        self.api = ESI()

        if ServerStatus.objects.all().count() == 0:
            db_status = ServerStatus()
        else:
            db_status = ServerStatus.objects.all()[0]

        status = self.api.get("/v1/status/")
        if status != None:
            db_status.online = True
            db_status.players = status['players']
            db_status.start_time = self.parse_api_date(status['start_time'])
            db_status.server_version = status['server_version']
            db_status.save()
        else:
            db_status.online = False
            db_status.save()
