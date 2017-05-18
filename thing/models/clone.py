from django.db import models

from thing.models.character import Character

class Clone(models.Model):
    character = models.ForeignKey(Character)
