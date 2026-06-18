from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return HttpResponse("Home page")


def contact(request):
    return HttpResponse("Contact page")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("about/", contact),
]
