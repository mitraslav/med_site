from django.contrib import admin
from .models import ContactRequest


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at", "is_processed")
    list_filter = ("is_processed", "created_at")
    search_fields = ("name", "email")
