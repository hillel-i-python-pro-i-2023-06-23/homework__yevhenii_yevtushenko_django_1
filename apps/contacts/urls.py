from django.urls import path
from . import views

app_name = "Contacts"

urlpatterns = [
    path("list/", views.ContactView.as_view(), name="contacts_list"),
    path("create/", views.ContactCreate.as_view(), name="contacts_create"),
    path("delete/<int:pk>/", views.ContactDelete.as_view(), name="contacts_delete"),
    path("update/<int:pk>/", views.ContactUpdate.as_view(), name="contacts_update"),
    path("generate/", views.generate_contacts_view, name="generate_contacts"),
    path("delete_all/", views.delete_all_contacts, name="delete_all"),
    path("joke/", views.joke, name="joke"),
]
