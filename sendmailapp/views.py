from django.shortcuts import render
from rest_framework import generics, status, permissions
from .serializers import SerializersEmailModel
from .models import EmailModel
from rest_framework.response import Response
from django.conf import settings
from django.core.mail import send_mail

# Class holding the function for sending email to the admin of the website


class EmailSending(generics.CreateAPIView):
    serializer_class = SerializersEmailModel
    queryset = EmailModel.objects.all()
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = SerializersEmailModel(data=request.data)
        if serializer.is_valid():
            mail = serializer.save()
            self.send_email(mail)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_email(self, mail):
        subject = f'Mail from {mail.name}'
        message = (
            f'Name: {mail.name}\n\n'
            f'Email: {mail.email_user}\n\n'
            f'About: {mail.show_alternativ}\n'
            f'Description: {mail.descriptions}'
        )

        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail(
             subject,
             message,
             from_email,
             recipient_list,
             fail_silently=False,
        )
