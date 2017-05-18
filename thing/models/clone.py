from django.db import models

from thing.models.character import Character
from thing.models.station import Station


class Clone(models.Model):
    character = models.ForeignKey(Character, related_name="clones", on_delete=models.CASCADE)
    location = models.ForeignKey(Station, null=True)
    last_updated = models.DateTimeField(auto_now=True)
