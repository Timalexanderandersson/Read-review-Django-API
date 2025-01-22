from django.shortcuts import render
from rest_framework import generics, status, permissions
from .serializers import SerializersEmailModel
from .models import EmailModel
from rest_framework.response import Response

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
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)    