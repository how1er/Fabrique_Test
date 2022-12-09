from django.db import models

from django.core.validators import RegexValidator


# Create your models here.

class Mailing_List(models.Model):
    start_time = models.DateTimeField()
    message = models.TextField()
    end_time = models.DateTimeField()
    mobile_code = models.CharField(max_length=11)
    tag = models.CharField(max_length=25)


class Client(models.Model):
    import pytz
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    phone_regex = RegexValidator(regex=r'^((7)+([0-9]){10})$',
                                 message="customer's phone number must be in the format 7XXXXXXXXXX (X is a number "
                                         "from 0 to 9)")
    phone_number = models.CharField(validators=[phone_regex], max_length=11, blank=True)
    code = models.PositiveIntegerField()
    tag = models.CharField(max_length=25)
    timezone = models.CharField(max_length=32, choices=TIMEZONES,
                                default='UTC')


class Message(models.Model):
    SENT = "sent"
    NO_SENT = "no sent"

    STATUS_CHOICES = [
        (SENT, "Sent"),
        (NO_SENT, "No sent"),
    ]

    creating_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES)
    message_id = models.ForeignKey(Mailing_List, on_delete=models.CASCADE, related_name='messages')
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')
