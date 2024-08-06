import imapclient
import pyzmail
from django.conf import settings
from myapp.models import EmailMessage
from concurrent.futures import ThreadPoolExecutor
from django.db import transaction

def fetch_emails(limit=100, offset=0):
    imap_server = imapclient.IMAPClient('imap.gmail.com', ssl=True, port=993)
    imap_server.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)
    imap_server.select_folder('INBOX')

    # Получение всех UID сообщений
    all_uids = imap_server.search(['ALL'])
    
    # Определение диапазона UID для пагинации
    start_uid = all_uids[0] + offset
    end_uid = start_uid + limit - 1
    messages = imap_server.search(['UID', f'{start_uid}:{end_uid}'])

    email_messages = []

    def process_message(uid, message_data):
        email_message = pyzmail.PyzMessage.factory(message_data[b'BODY[]'])
        subject = email_message.get_subject()
        sender = email_message.get_address('from')
        body = email_message.text_part.get_payload().decode(email_message.text_part.charset) if email_message.text_part else ""
        email_messages.append(EmailMessage(subject=subject, sender=sender, body=body))

    with ThreadPoolExecutor(max_workers=10) as executor:
        for uid, message_data in imap_server.fetch(messages, ['BODY[]']).items():
            executor.submit(process_message, uid, message_data)

    with transaction.atomic():
        EmailMessage.objects.bulk_create(email_messages)

    imap_server.logout()

# Пример вызова функции с пагинацией
fetch_emails(limit=100, offset=0)
