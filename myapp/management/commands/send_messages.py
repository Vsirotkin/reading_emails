from django.core.management.base import BaseCommand
from myapp.models import EmailMessage
from django.utils import timezone

class Command(BaseCommand):
    help = 'Send test messages to the database'

    def handle(self, *args, **options):
        messages = [
            {
                'subject': f'Test Message {i+1}',
                'sent_date': timezone.now(),
                'received_date': timezone.now(),
                'body': f'This is the body of test message {i+1}.'
            }
            for i in range(10)
        ]

        for message in messages:
            EmailMessage.objects.create(
                subject=message['subject'],
                sent_date=message['sent_date'],
                received_date=message['received_date'],
                body=message['body']
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully sent message: {message["subject"]}'))

        self.stdout.write(self.style.SUCCESS('All messages sent successfully'))