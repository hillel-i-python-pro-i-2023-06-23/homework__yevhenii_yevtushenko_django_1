from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", views.index, name="index"),
]
