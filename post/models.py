from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    # Post models for making posts on website.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image_post = models.ImageField(
        upload_to="images/", default='book-front-page_rt7nvr'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} {self.user.username}'
