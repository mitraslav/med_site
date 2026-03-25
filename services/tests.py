from django.test import TestCase
from .models import Service


class ServiceModelTest(TestCase):
    def test_service_str(self):
        service = Service.objects.create(
            title='УЗИ',
            short_description='Краткое описание',
            full_description='Полное описание услуги',
            price=1500,
            is_active=True,
        )
        self.assertEqual(str(service), 'УЗИ')
