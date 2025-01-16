from django.db import models
from django.contrib.auth.models import User

# Post Models


class Post(models.Model):
    # Post models for making posts on website.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_post = models.ImageField(
        upload_to="images/", default='media/images/books-1246674_1280_ksuj7m'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} {self.user.username}'
