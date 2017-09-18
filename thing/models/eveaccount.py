from django.db import models
from django.contrib.auth.models import User


class EveAccount(models.Model):
    user = models.ForeignKey(User, related_name="accounts", on_delete=models.CASCADE)
    username = models.CharField(max_length=32)

    def slotOne(self):
        return self.tokens.order_by('characterID').first()

    def slotTwo(self):
        if self.tokens.count() > 1:
            return self.tokens.order_by('characterID')[1]

    def slotThree(self):
        if self.tokens.count() > 2:
            return self.tokens.order_by('characterID')[2]
