from django.test import TestCase
from myapp.models import EmailMessage
from django.db import transaction, IntegrityError

class DatabaseIntegrationTests(TestCase):
    def setUp(self):
        # Создайте тестовые данные для использования в тестах
        self.email = EmailMessage.objects.create(
            subject="Test Subject",
            sent_date="2023-01-01T12:00:00Z",
            received_date="2023-01-01T12:05:00Z",
            body="Test Body",
            attachments="path/to/attachment.jpg"
        )

    def test_data_insertion(self):
        # Проверка корректности сохранения данных в базу данных
        self.assertEqual(EmailMessage.objects.count(), 1)
        self.assertEqual(self.email.subject, "Test Subject")

    def test_data_retrieval(self):
        # Проверка корректности извлечения данных из базы данных
        retrieved_email = EmailMessage.objects.get(subject="Test Subject")
        self.assertEqual(retrieved_email.body, "Test Body")

    def test_transaction_atomicity(self):
        # Проверка транзакций и атомарности операций
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                EmailMessage.objects.create(
                    subject="Test Subject",
                    sent_date="2023-01-01T12:00:00Z",
                    received_date="2023-01-01T12:05:00Z",
                    body="Test Body",
                    attachments="path/to/attachment.jpg"
                )
                # Вызываем исключение для проверки атомарности транзакции
                raise IntegrityError("Simulated integrity error")

        # Убедитесь, что данные не были сохранены из-за ошибки
        self.assertEqual(EmailMessage.objects.count(), 1)
