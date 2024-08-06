from django.core.management.base import BaseCommand
from myapp.services import fetch_emails

class Command(BaseCommand):
    help = 'Import emails'

    def handle(self, *args, **options):
        fetch_emails()
        self.stdout.write(self.style.SUCCESS('Successfully imported emails'))
