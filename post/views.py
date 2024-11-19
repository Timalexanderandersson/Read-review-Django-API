from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from read_api.permissions import UserOrReadOnly


# Post list
class PostList(APIView):
    """
    Showing all of the book posts.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Function for adding a post.
        """
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Post content details
class PostContent(APIView):
    serializer_class = PostSerializer
    permission_classes = [UserOrReadOnly]

    def post_object(self, pk):
        """
        Function to GET post by the pk, and if not found 404 error.
        """
        try:
            post = Post.objects.get(pk=pk)
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Function get to convert the post to JSON
        404 if validation fail.
        """
        post = self.post_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Function for PUT for updating post pk. and convert to JSON
        404 if validation fail.
        """
        post = self.post_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Function for delete a post pk.
        """
        post = self.post_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

