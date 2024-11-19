from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Comments
from .serializers import CommentSerializer
from read_api.permissions import UserOrReadOnly


# Comment list
class CommentList(APIView):
    """
    Function for GET commentlists and convert to JSON data.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        comments = Comments.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Function for posting commentlists and convert to JSON data.
        """
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Comment content
class CommentContent(APIView):
    serializer_class = CommentSerializer
    permission_classes = [UserOrReadOnly]

    def comment_object(self, pk):
        """
        Function to GET comment by the pk, and if not found 404 error.
        """
        try:
            comment = Comments.objects.get(pk=pk)
            self.check_object_permissions(self.request, comment)
            return comment
        except Comments.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Function get to convert the comment to JSON
        404 if validation fail.
        """
        comment = self.comment_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Function for PUT for updating comments. and convert to JSON
        404 if validation fail.
        """
        comment = self.comment_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Function for deleting a Comment.
        """
        comment = self.comment_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
