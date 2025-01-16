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
        upload_to="images/", default='https://res.cloudinary.com/dwxzdd3bf/image/upload/v1733151833/media/images/book-front-page_w2impn.webp'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} {self.user.username}'
