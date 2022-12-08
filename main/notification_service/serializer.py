from rest_framework import serializers
from .models import Client, Mailing_List, Message


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing_List
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
