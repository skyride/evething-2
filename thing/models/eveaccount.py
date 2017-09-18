from django.db import models
from django.contrib.auth.models import User


class EveAccount(models.Model):
    user = models.ForeignKey(User, related_name="accounts", on_delete=models.CASCADE)
    username = models.CharField(max_length=32)


    # This is unreliable right now as skill queues aren't a good indicator of subscription status
    def is_subbed(self):
        for token in self.tokens.all():
            if token.character.is_training():
                return True
        return False

    def active_queues(self):
        queues = 0
        for token in self.tokens.all():
            if token.character.is_training():
                queues += 1
        return queues


    def slotOne(self):
        return self.tokens.order_by('characterID').first()

    def slotTwo(self):
        if self.tokens.count() > 1:
            return self.tokens.order_by('characterID')[1]

    def slotThree(self):
        if self.tokens.count() > 2:
            return self.tokens.order_by('characterID')[2]
