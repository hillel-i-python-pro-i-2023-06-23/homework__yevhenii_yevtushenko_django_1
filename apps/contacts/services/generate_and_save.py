from apps.contacts.services.generate_contacts import generate_contacts


def generate_and_save(amount: int) -> None:
    for contact in generate_contacts(amount=amount):
        contact.save()
