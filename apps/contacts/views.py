from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from apps.contacts.forms import GenerateForm
from apps.contacts.models import Contact
from apps.contacts.services.delete import delete
from apps.contacts.services.generate_and_save import generate_and_save


class ContactView(ListView):
    model = Contact


class ContactCreate(CreateView):
    model = Contact
    fields = (
        "name",
        "phone",
    )
    success_url = reverse_lazy("contacts:contacts_list")


class ContactUpdate(UpdateView):
    model = Contact
    fields = (
        "name",
        "phone",
    )
    success_url = reverse_lazy("contacts:contacts_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy("contacts:contacts_list")


def generate_contacts_view(request):
    form = GenerateForm(request.POST)
    if form.is_valid():
        amount = form.cleaned_data["amount"]
        generate_and_save(amount)

    return render(
        request=request,
        template_name="contacts/generate_contacts.html",
        context=dict(
            contacts_list=Contact.objects.all(),
            form=form,
        ),
    )


def delete_all_contacts(request):
    delete()
    return redirect("contacts:contacts_list")


def joke(request):
    return render(request, "contacts/joke.html")
