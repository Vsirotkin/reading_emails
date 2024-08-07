from django.shortcuts import render

from rest_framework import viewsets
from myapp.models import EmailMessage
from myapp.serializers import EmailMessageSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class EmailMessageViewSet(viewsets.ModelViewSet):
    queryset = EmailMessage.objects.all()
    serializer_class = EmailMessageSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "emails",
            {
                "type": "email_message",
                "message": instance.body
            }
        )


def email_list(request):
    email_messages = EmailMessage.objects.all()
    return render(request, 'myapp/email_list.html', {'email_messages': email_messages})
