from django.db import models

class EmailMessage(models.Model):
    subject = models.CharField(max_length=255)
    sender = models.CharField(max_length=255)
    body = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
