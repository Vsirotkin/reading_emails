import logging
from django.core.management.base import BaseCommand
from myapp.services import fetch_emails

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Import emails'

    def handle(self, *args, **options):
        try:
            emails = fetch_emails()
            if not emails:
                logger.info("No emails to import")
            else:
                for email in emails:
                    logger.info(f"Imported email: {email.subject}")  # Используем точечную нотацию
                self.stdout.write(self.style.SUCCESS('Successfully imported emails'))
                logger.info('Successfully imported emails')
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing emails: {e}'))
            logger.error(f'Error importing emails: {e}', exc_info=True)
