from rest_framework import serializers
from .models import Comments

# Comments serializers
class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    post_name = serializers.CharField(source='post.title', read_only=True)
    class Meta:
        model = Comments
        fields = ['post_name','post','comment','created_at','username','id']

# Comments serializers
class CommentContentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    post = serializers.CharField(read_only=True)
    class Meta:
        model = Comments
        fields = ['post','comment','created_at','username','id']        