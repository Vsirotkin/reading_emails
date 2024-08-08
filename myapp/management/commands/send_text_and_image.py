from django.core.management.base import BaseCommand
from myapp.models import EmailMessage
from django.utils import timezone
from django.core.files.base import File
from django.core.files.storage import default_storage
import os

class Command(BaseCommand):
    help = 'Send a message with an image attachment'

    def handle(self, *args, **kwargs):
        image_path = '/app/media/images/send_email.jpg'
        subject = 'Test Message with Attachment'
        body = 'This is the body of the test message with an attachment.'

        # Проверка, что файл существует и доступен
        if default_storage.exists(image_path):
            with default_storage.open(image_path, 'rb') as f:
                django_file = File(f)
                # Генерация безопасного имени файла
                safe_name = os.path.basename(image_path)
                email = EmailMessage(
                    subject=subject,
                    sent_date=timezone.now(),
                    received_date=timezone.now(),
                    body=body,
                    attachments=django_file
                )
                email.attachments.name = safe_name
                email.save()
                self.stdout.write(self.style.SUCCESS(f'Message with subject "{subject}" and attachment saved successfully.'))
        else:
            self.stdout.write(self.style.ERROR(f'File not found: {image_path}'))
