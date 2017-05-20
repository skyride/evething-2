from .apitask import APITask

from thing.esi import ESI

from thing.models import *


class ESI_MailFetchTask(APITask):
    name = "thing.esi.mail_fetch_task"
    api = None


    def run(self, token_id, mail):
        token = ESIToken.objects.get(id=token_id)
        self.api = ESI(token)
        character = token.character

        to_characters = map(
            lambda x: Character.get_or_create(x['recipient_id']),
            filter(
                lambda x: x['recipient_type'] == "character",
                mail['recipients']
            )
        )
        to_corp_or_alliance_id = filter(
            lambda x: x['recipient_type'] in ["corporation", "alliance"],
            mail['recipients']
        )
        if len(to_corp_or_alliance_id) == 0:
            to_corp_or_alliance_id = 0
        else:
            to_corp_or_alliance_id = to_corp_or_alliance_id[0]['recipient_id']

        to_list_id = filter(
            lambda x: x['recipient_type'] == "mailing_list",
            mail['recipients']
        )
        if len(to_list_id) == 0:
            to_list_id = 0
        else:
            to_list_id = to_list_id[0]['recipient_id']

        body = self.api.get("/characters/$id/mail/%s/" % mail['mail_id'])

        try:
            Character.get_or_create(mail['from'])
        except Exception:
            pass

        db_mail = MailMessage(
            character=character,
            message_id=mail['mail_id'],
            sender_id=mail['from'],
            sent_date=self.parse_api_date(mail['timestamp']),
            title=mail['subject'],
            #to_characters=to_characters,
            to_corp_or_alliance_id=to_corp_or_alliance_id,
            to_list_id=to_list_id,
            body=body['body'].replace("<br>", "\n"),
            read=mail['is_read']
        )
        db_mail.save()
