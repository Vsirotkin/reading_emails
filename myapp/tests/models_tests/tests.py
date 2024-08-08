from django.test import TestCase
from myapp.models import EmailMessage

class EmailMessageModelTest(TestCase):
    def test_create_email_message(self):
        email = EmailMessage.objects.create(
            subject="Test Subject",
            sent_date="2023-01-01T12:00:00Z",
            received_date="2023-01-01T12:05:00Z",
            body="Test Body",
            attachments="path/to/attachment.jpg"
        )
        self.assertEqual(email.subject, "Test Subject")
        self.assertEqual(email.body, "Test Body")