from django.db import models

from thing.models.clone import Clone
from thing.models.item import Item


class CloneImplant(models.Model):
    clone = models.ForeignKey(Clone, related_name="implants", on_delete=models.CASCADE)
    item = models.ForeignKey(Item)
