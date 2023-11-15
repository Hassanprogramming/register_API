from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Registration

class RegistrationAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('registration:register')
        self.cancel_url = reverse('registration:cancel_registration')

    def test_registration(self):
        data = {'first_name': 'John', 'last_name': 'Doe', 'national_id': '1234567890'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Registration.objects.count(), 1)

    def test_cancel_registration(self):
        registration = Registration.objects.create(first_name='John', last_name='Doe', national_id='1234567890')
        data = {'national_id': '1234567890'}
        response = self.client.post(self.cancel_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Registration.objects.count(), 1)

    def test_get_registration_list(self):
        response = self.client.get(reverse('registration:registration_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_canceled_registration_list(self):
        # Create a canceled registration
        canceled_registration = Registration.objects.create(
            first_name='Jane', last_name='Doe', national_id='0987654321', canceled=True
        )
        response = self.client.get(reverse('registration:registration_list') + '?filter=canceled')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, canceled_registration.first_name, status_code=status.HTTP_200_OK)
        self.assertContains(response, canceled_registration.last_name, status_code=status.HTTP_200_OK)
        self.assertContains(response, canceled_registration.national_id, status_code=status.HTTP_200_OK)
        self.assertContains(response, 'Canceled', status_code=status.HTTP_200_OK)