from django.contrib import messages
from django.shortcuts import render, redirect

from appointments.models import Doctor
from services.models import Service
from .forms import ContactRequestForm


def home(request):
    services = Service.objects.filter(is_active=True)[:6]
    doctors = Doctor.objects.filter(is_active=True)[:4]

    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение успешно отправлено.')
            return redirect('main:home')
    else:
        form = ContactRequestForm()

    context = {
        'services': services,
        'doctors': doctors,
        'form': form,
    }
    return render(request, 'main/home.html', context)


def about(request):
    doctors = Doctor.objects.filter(is_active=True)
    return render(request, 'main/about.html', {'doctors': doctors})


def contacts(request):
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение успешно отправлено.')
            return redirect('main:contacts')
    else:
        form = ContactRequestForm()

    return render(request, 'main/contacts.html', {'form': form})