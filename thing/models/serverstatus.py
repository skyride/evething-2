from django.db import models


class ServerStatus(models.Model):
    online = models.BooleanField(default=False)
    players = models.IntegerField(default=0)
    start_time = models.DateTimeField()
    server_version = models.IntegerField()
