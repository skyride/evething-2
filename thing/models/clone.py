from django.db import models

from thing.models.character import Character
from django.db.models import Sum
from thing.models.station import Station


class Clone(models.Model):
    character = models.ForeignKey(Character, related_name="clones", on_delete=models.CASCADE)
    name = models.CharField(max_length=64, default="")
    location = models.ForeignKey(Station, related_name="clones", null=True)
    last_updated = models.DateTimeField(auto_now=True)


    def get_implants_value(self):
        return self.implants.aggregate(total=Sum('implant__item__sell_price'))['total']
