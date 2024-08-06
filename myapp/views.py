from rest_framework import viewsets
from myapp.models import EmailMessage
from myapp.serializers import EmailMessageSerializer

class EmailMessageViewSet(viewsets.ModelViewSet):
    queryset = EmailMessage.objects.all()
    serializer_class = EmailMessageSerializer
