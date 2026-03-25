from django.urls import path
from .views import appointment_create, my_appointments

app_name = "appointments"

urlpatterns = [
    path("create/", appointment_create, name="appointment_create"),
    path("my/", my_appointments, name="my_appointments"),
]
