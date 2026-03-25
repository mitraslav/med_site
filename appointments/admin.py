from django.contrib import admin
from django.utils.html import format_html

from .models import Doctor, Appointment


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "specialization",
        "experience",
        "is_active",
        "photo_preview",
    )
    list_filter = ("is_active", "specialization")
    search_fields = ("full_name", "specialization")

    readonly_fields = ("photo_preview",)

    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "full_name",
                    "specialization",
                    "experience",
                    "description",
                    "is_active",
                )
            },
        ),
        (
            "Фотография",
            {
                "fields": (
                    "photo",
                    "photo_preview",
                )
            },
        ),
    )

    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="80" height="80" style="object-fit: cover; border-radius: 8px;" />',
                obj.photo.url,
            )
        return "Нет фото"

    photo_preview.short_description = "Превью фото"


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "doctor",
        "service",
        "appointment_date",
        "appointment_time",
        "status",
    )
    list_filter = ("status", "appointment_date", "doctor")
    search_fields = (
        "user__username",
        "doctor__full_name",
        "service__title",
    )
