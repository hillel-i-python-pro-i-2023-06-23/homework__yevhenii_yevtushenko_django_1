from django.core.management import BaseCommand
from apps.contacts.models import Contact


class Command(BaseCommand):
    help = "Deletes all contacts from the database"

    def handle(self, *args, **options):
        Contact.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("All contacts were deleted successfully"))
