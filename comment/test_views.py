from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from post.models import Post

class CommentTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="mafe", password="monkeyman123")
        self.client.login(username="mafe", password="monkeyman123")
        self.post = Post.objects.create(title="hey", description="wow", user=self.user)
        self.url = reverse("comments")
        self.data = {
            "post": self.post.id,
            "comment":"wow",
        }
        
    def test_if_comment_works(self):
        answer = self.client.post(self.url, self.data, format="json")
        self.assertEqual(answer.status_code, status.HTTP_201_CREATED)
