from django.core.management.base import BaseCommand
from myapp.models import EmailMessage
from django.utils import timezone

class Command(BaseCommand):
    help = 'Send test messages to the database'

    def handle(self, *args, **options):
        messages = [
            {
                'subject': 'Test Message 1',
                'sent_date': timezone.now(),
                'received_date': timezone.now(),
                'body': 'This is the first test message.'
            },
            {
                'subject': 'Test Message 2',
                'sent_date': timezone.now(),
                'received_date': timezone.now(),
                'body': 'This is the second test message.'
            },
            {
                'subject': 'Test Message 3',
                'sent_date': timezone.now(),
                'received_date': timezone.now(),
                'body': 'This is the third test message.'
            },
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