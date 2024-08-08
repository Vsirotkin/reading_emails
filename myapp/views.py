from django.shortcuts import render
from django.core.paginator import Paginator

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
    email_messages = EmailMessage.objects.all().order_by('-sent_date')
    message_count = email_messages.count()
    paginator = Paginator(email_messages, 3)  # Показывать 3 сообщения на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': email_messages,
        'message_count': message_count,
    }
    return render(request, 'myapp/email_list.html', context)

