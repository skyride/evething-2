from django.db import models

from django.contrib.auth.models import User

class ESIToken(models.Model):
    access_token = models.CharField(max_length=128)
    refresh_token = models.CharField(max_length=320)

    user = models.ForeignKey(User)
    status = models.BooleanField(default=True)
    added = models.DateTimeField(auto_now_add=True)

    token_type = models.CharField(max_length=32)
    characterID = models.IntegerField(default=None, null=True)
    corporationID = models.IntegerField(default=None, null=True)
    name = models.CharField(max_length=64)

    class Meta:
        app_label = 'thing'
