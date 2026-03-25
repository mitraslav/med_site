from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import AppointmentForm
from .models import Appointment


@login_required
def appointment_create(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.success(request, "Вы успешно записались на приём.")
            return redirect("appointments:my_appointments")
    else:
        form = AppointmentForm()

    return render(request, "appointments/appointment_create.html", {"form": form})


@login_required
def my_appointments(request):
    appointments = Appointment.objects.filter(user=request.user).order_by(
        "-appointment_date",
        "-appointment_time",
    )
    return render(
        request,
        "appointments/my_appointments.html",
        {"appointments": appointments},
    )
