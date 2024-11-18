from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from .models import Comments
from .serializers import CommentSerializer

# Comment list
class CommentList(APIView):
    """
    Function for GET commentlists and convert to JSON data.
    """
    def get(self, request):
        comments = Comments.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

