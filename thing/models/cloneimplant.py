from django.db import models

from thing.models.clone import Clone
from thing.models.implant import Implant


class CloneImplant(models.Model):
    clone = models.ForeignKey(Clone, related_name="implants", on_delete=models.CASCADE)
    implant = models.ForeignKey(Implant, related_name="implants")
