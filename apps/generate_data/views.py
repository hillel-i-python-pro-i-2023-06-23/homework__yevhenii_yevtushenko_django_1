from django.shortcuts import render

from apps.generate_data.genetate_user import generate_users


# Create your views here.


def generate_user(request, users_count: int):
    users = generate_users(users_count)

    return render(request, "generate_user.html", {"users": users})
