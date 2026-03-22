from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'doctor',
            'service',
            'appointment_date',
            'appointment_time',
            'comment',
        ]
        widgets = {
            'doctor': forms.Select(attrs={'class': 'form-select'}),
            'service': forms.Select(attrs={'class': 'form-select'}),
            'appointment_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'appointment_time': forms.TimeInput(
                attrs={'class': 'form-control', 'type': 'time'}
            ),
            'comment': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4}
            ),
        }