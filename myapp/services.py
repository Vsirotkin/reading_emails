import imapclient
import pyzmail
from django.conf import settings

from myapp.models import EmailMessage

def fetch_emails():
    imap_server = imapclient.IMAPClient('imap.gmail.com', ssl=True, port=993)
    imap_server.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)
    imap_server.select_folder('INBOX')

    messages = imap_server.search(['ALL'])
    for uid, message_data in imap_server.fetch(messages, ['BODY[]']).items():
        email_message = pyzmail.PyzMessage.factory(message_data[b'BODY[]'])
        subject = email_message.get_subject()
        sender = email_message.get_address('from')

        # Проверка наличия текстовой части
        if email_message.text_part is not None:
            body = email_message.text_part.get_payload().decode(email_message.text_part.charset)
        elif email_message.html_part is not None:
            body = email_message.html_part.get_payload().decode(email_message.html_part.charset)
        else:
            body = ""  # или другое значение по умолчанию

        # Сохранение сообщения в базу данных
        EmailMessage.objects.create(subject=subject, sender=sender, body=body)

    imap_server.logout()
