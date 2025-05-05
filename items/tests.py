from django.test import TestCase

# Create your tests here.

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


class ItemPermissionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_authenticated_user_can_create_item(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post('/api/items/', {'title': 'Test Item', 'description': 'Test Description'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)