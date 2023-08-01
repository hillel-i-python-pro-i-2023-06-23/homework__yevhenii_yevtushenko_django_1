from django.views.generic import ListView

from apps.contacts.models import Contact


class ContactView(ListView):
    model = Contact
