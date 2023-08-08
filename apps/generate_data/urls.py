from django.urls import path
from . import views

app_name = "generate_data"

urlpatterns = [
    path("<int:users_count>/", views.generate_user, name="generate-user"),
]
