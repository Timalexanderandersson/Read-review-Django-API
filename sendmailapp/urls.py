from django.urls import path
from .views import EmailSending

urlpatterns = [
    path("sendmail/", EmailSending.as_view(), name="mailsend"),
]
