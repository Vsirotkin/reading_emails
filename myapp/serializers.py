from rest_framework import serializers
from myapp.models import EmailMessage

class EmailMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailMessage
        fields = ['id', 'subject', 'sender', 'body', 'received_at']
