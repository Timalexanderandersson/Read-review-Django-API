from rest_framework import serializers
from .models import Comments


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    post_id = serializers.CharField(source='post.title', read_only=True)
    class Meta:
        model = Comments
        fields = ['post_id','post','comment','created_at','username',]