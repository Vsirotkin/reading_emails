class Command(BaseCommand):
    help = 'Clear all email messages from the database'

    def handle(self, *args, **kwargs):
        EmailMessage.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared email messages'))
