import os
import requests
import pytz
import datetime
from dotenv import load_dotenv

from .models import Message, Client, Mailing_List

load_dotenv()
URL = os.getenv("URL")
TOKEN = os.getenv("TOKEN")


def send_message(self, data, client_id, mailing_id, url=URL, token=TOKEN):
    mail = Mailing_List.objects.get(pk=mailing_id)
    client = Client.objects.get(pk=client_id)
    timezone = pytz.timezone(client.timezone)
    now = datetime.datetime.now(timezone)

    if mail.time_start <= now.time() <= mail.time_end:
        header = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'}
        try:
            requests.post(url=url + str(data['id']), headers=header, json=data)
        except requests.exceptions.RequestException as exc:

            raise self.retry(exc=exc)
        else:

            Message.objects.filter(pk=data['id']).update(sending_status='Sent')
    else:
        time = 24 - (int(now.time().strftime('%H:%M:%S')[:2]) -
                     int(mail.time_start.strftime('%H:%M:%S')[:2]))

        return self.retry(countdown=60 * 60 * time)
