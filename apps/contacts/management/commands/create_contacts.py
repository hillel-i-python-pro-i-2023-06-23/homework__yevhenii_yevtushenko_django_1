from django.core.management import BaseCommand

from apps.contacts.services.generate_contacts import generate_contacts


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--amount",
            type=int,
            help="Indicates the number of contacts to be created",
            default=5,
        )

    def handle(self, *args, **options):
        amount: int = options["amount"]

        for contact in generate_contacts(amount):
            contact.save()
            self.stdout.write(self.style.SUCCESS(f"Contact {contact.name} was created successfully"))
