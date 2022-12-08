from django.shortcuts import render
from rest_framework import viewsets

from .models import Mailing_List, Client, Message
from .serializer import MailingSerializer, ClientSerializer, MessageSerializer

# Create your views here.


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class MailingViewSet(viewsets.ModelViewSet):
    serializer_class = MailingSerializer
    queryset = Mailing_List.objects.all()

