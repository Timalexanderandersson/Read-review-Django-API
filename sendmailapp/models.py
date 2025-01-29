from django.db import models

# Model for sending email from the website


class EmailModel(models.Model):

    name = models.CharField(max_length=150)
    email_user = models.EmailField()
    show_alternativ = models.CharField(choices=[
            ('books', 'Books'),
            ('jobs', 'Jobs'),
            ('reviews', 'Reviews'),
            ('other', 'Other'),
        ])
    descriptions = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'email from {self.name} about {self.show_alternativ}'
