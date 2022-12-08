from django.db import models


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

    mobile_number = models.PositiveIntegerField()
    code = models.PositiveIntegerField()
    tag = models.CharField(max_length=25)
    timezone = models.CharField(max_length=32, choices=TIMEZONES,
                                default='UTC')


class Message(models.Model):
    creating_date = models.DateTimeField()
    status = models.CharField(max_length=25)
    message_id = models.ForeignKey(Mailing_List, on_delete=models.CASCADE, related_name='messages')
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')

