from django.db import models

from thing.models.character import Character
from thing.models.station import Station


class Clone(models.Model):
    character = models.ForeignKey(Character, related_name="clones")
    location = models.ForeignKey(Station)
    last_updated = models.DateTimeField(auto_now=True)
