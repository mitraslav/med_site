from datetime import date, time

from django import forms

from .models import Appointment, Doctor
from services.models import Service


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "doctor",
            "service",
            "appointment_date",
            "appointment_time",
            "comment",
        ]
        widgets = {
            "doctor": forms.Select(attrs={"class": "form-select"}),
            "service": forms.Select(attrs={"class": "form-select"}),
            "appointment_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
            "appointment_time": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "type": "time",
                }
            ),
            "comment": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "При необходимости оставьте комментарий",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["doctor"].queryset = Doctor.objects.filter(is_active=True)
        self.fields["service"].queryset = Service.objects.filter(is_active=True)

        self.fields["doctor"].empty_label = "Выберите врача"
        self.fields["service"].empty_label = "Выберите услугу"

    def clean_appointment_date(self):
        appointment_date = self.cleaned_data["appointment_date"]
        if appointment_date < date.today():
            raise forms.ValidationError("Нельзя записаться на прошедшую дату.")
        return appointment_date

    def clean_appointment_time(self):
        appointment_time = self.cleaned_data["appointment_time"]

        start_time = time(8, 0)
        end_time = time(20, 0)

        if appointment_time < start_time or appointment_time > end_time:
            raise forms.ValidationError(
                "Запись возможна только в рабочее время: с 08:00 до 20:00."
            )
        return appointment_time

    def clean_comment(self):
        comment = self.cleaned_data.get("comment", "").strip()
        return comment

    def clean(self):
        cleaned_data = super().clean()
        doctor = cleaned_data.get("doctor")
        service = cleaned_data.get("service")
        appointment_date = cleaned_data.get("appointment_date")
        appointment_time = cleaned_data.get("appointment_time")

        if doctor and service and appointment_date and appointment_time:
            exists = Appointment.objects.filter(
                doctor=doctor,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
            ).exists()

            if exists:
                raise forms.ValidationError(
                    "На выбранные дату и время этот врач уже занят."
                )

        return cleaned_data
