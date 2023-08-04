from django.urls import path
from . import views

app_name = "Contacts"

urlpatterns = [
    path("list/", views.ContactView.as_view(), name="contacts_list"),
    path("create/", views.ContactCreate.as_view(), name="contacts_create"),
    path("delete/<int:pk>/", views.ContactDelete.as_view(), name="contacts_delete"),
]
