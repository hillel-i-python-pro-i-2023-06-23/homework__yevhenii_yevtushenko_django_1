from django.shortcuts import render


def home_page(request):
    return render(request, "base/home_page.html", {"title": "Home page"})
