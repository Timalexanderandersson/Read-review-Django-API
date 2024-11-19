from rest_framework import serializers
from .models import Post

# Post serializers
class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Post
        fields = ['username','title','description','image_post', 'id',]