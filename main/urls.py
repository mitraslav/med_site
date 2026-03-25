from django.urls import path
from .views import home, about, contacts

app_name = "main"

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contacts/", contacts, name="contacts"),
]
