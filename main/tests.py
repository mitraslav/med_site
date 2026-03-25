from django.test import TestCase
from django.urls import reverse


class MainViewsTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('main:home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get(reverse('main:about'))
        self.assertEqual(response.status_code, 200)

    def test_contacts_page_status_code(self):
        response = self.client.get(reverse('main:contacts'))
        self.assertEqual(response.status_code, 200)