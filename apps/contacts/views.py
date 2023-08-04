from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from apps.contacts.models import Contact


class ContactView(ListView):
    model = Contact


class ContactCreate(CreateView):
    model = Contact
    fields = (
        "name",
        "phone",
    )
    success_url = reverse_lazy("contacts:contacts_list")


class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy("contacts:contacts_list")
