from datetime import date, timedelta, time

from django.contrib.auth.models import User
from django.test import TestCase

from appointments.forms import AppointmentForm
from appointments.models import Doctor
from services.models import Service


class AppointmentFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.doctor = Doctor.objects.create(
            full_name="Иванов Иван Иванович",
            specialization="Терапевт",
            experience=10,
            description="Опытный врач",
            is_active=True,
        )
        self.service = Service.objects.create(
            title="Консультация",
            short_description="Кратко",
            full_description="Полное описание",
            price=2000,
            is_active=True,
        )

    def test_appointment_form_valid(self):
        form_data = {
            "doctor": self.doctor.id,
            "service": self.service.id,
            "appointment_date": date.today() + timedelta(days=1),
            "appointment_time": time(10, 0),
            "comment": "Тестовая запись",
        }
        form = AppointmentForm(data=form_data)
        self.assertTrue(form.is_valid())
