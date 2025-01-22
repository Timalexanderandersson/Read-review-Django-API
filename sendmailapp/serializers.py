from rest_framework import serializers
from .model import EmailModel

# Serializers for sendmailapp

class SerializersEmailModel(serializers.ModelSerializer):

    class Meta:
        model = EmailModel
        fields = [
            "name",
            "email_user",
            "show_alternativ",
            "descriptions",
            "created_at",
            
        ]
