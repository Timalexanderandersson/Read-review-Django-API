from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

class PostTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="mafe", password="monkeyman123")
        self.client.login(username="mafe", password="monkeyman123")
        self.url = reverse("post")
        self.data = {
            "title":"wow",
            "content":"wow",
        }
        
    def test_if_posting_works(self):
        answer = self.client.post(self.url, self.data, format="json")
        self.assertEqual(answer.status_code, status.HTTP_201_CREATED)
        self.assertTrue(self.url, self.data)


class SignInUser(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="timovealexander", password="monkey123mokey",)
        self.url = '/dj-rest-auth/login/'
        self.data = {
            'username': 'timovealexander',
            'password':'monkey123mokey',
            
        }
    def test_for_login_is_valid(self):
         answer = self.client.post(self.url, self.data, format="json")
         self.assertEqual(answer.status_code, status.HTTP_200_OK)
          
