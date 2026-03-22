from django.contrib import admin
from .models import Doctor, Appointment


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization', 'experience', 'is_active')
    list_filter = ('is_active', 'specialization')
    search_fields = ('full_name', 'specialization')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'doctor',
        'service',
        'appointment_date',
        'appointment_time',
        'status',
    )
    list_filter = ('status', 'appointment_date', 'doctor')
    search_fields = (
        'user__username',
        'doctor__full_name',
        'service__title',
    )
