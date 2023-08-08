from apps.contacts.models import Contact


def delete():
    Contact.objects.all().delete()
