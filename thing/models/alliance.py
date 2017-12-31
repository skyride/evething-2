# ------------------------------------------------------------------------------
# Copyright (c) 2010-2013, EVEthing team
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#     Redistributions of source code must retain the above copyright notice, this
#       list of conditions and the following disclaimer.
#     Redistributions in binary form must reproduce the above copyright notice,
#       this list of conditions and the following disclaimer in the documentation
#       and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
# OF SUCH DAMAGE.
# ------------------------------------------------------------------------------

from datetime import datetime, timedelta

from django.db import models


class Alliance(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    short_name = models.CharField(max_length=5)
    last_updated = models.DateTimeField(auto_now=True, default=datetime(0001, 1, 1, 1, 0))

    class Meta:
        app_label = 'thing'


    @staticmethod
    def get_or_create(alliance_id):
        from thing.esi import ESI
        api = ESI()

        db_alliance = Alliance.objects.filter(id=alliance_id)
        if len(db_alliance) == 0:
            alliance = api.get("/v3/alliances/%s/" % alliance_id)
            db_alliance = Alliance(
                id=alliance_id,
                name=alliance['name'],
                short_name=alliance['ticker']
            )
            db_alliance.save()

            return db_alliance
        else:
            db_alliance = db_alliance[0]
            if db_alliance.last_updated < datetime.now() - timedelta(days=2):
                alliance = api.get("/v3/alliances/%s/" % alliance_id)
                db_alliance.name = alliance['name']
                db_alliance.short_name = alliance['ticker']
                db_alliance.save()

            return db_alliance
