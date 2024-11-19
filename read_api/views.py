from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def api_views(request):
    return Response(
        {'message':'This is the Read&review API',}
    )