from collections.abc import Iterator

from faker import Faker

from apps.contacts.models import Contact


faker = Faker()


def generate_contact() -> Contact:
    name = faker.first_name()
    phone = faker.phone_number()
    return Contact(name=name, phone=phone)


def generate_contacts(amount: int) -> Iterator[Contact]:
    for _ in range(amount):
        yield generate_contact()
