from django.db import models

class EmailMessage(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    sent_date = models.DateTimeField(null=True, blank=True, default=None)
    received_date = models.DateTimeField(null=True, blank=True, default=None)  # Добавлено значение по умолчанию None
    body = models.TextField(default='')  # Установите значение по умолчанию
    attachments = models.FileField(upload_to='attachments/', blank=True, null=True)  # Хранение списка прикреплённых файлов

    def __str__(self):
        return self.subject
