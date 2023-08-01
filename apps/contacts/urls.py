from django.urls import path
from . import views

app_name = "Contacts"

urlpatterns = [
    path("list/", views.ContactView.as_view(), name="contacts_list"),
    path("delete/", views.ContactDeleteView.as_view(), name="contact_delete"),
]
