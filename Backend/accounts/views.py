from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class LogoutApiView(APIView):
    def post(self,request,format=None):
        token=request.META['HTTP_AUTHORIZATION']
        print(token)
        return Response(status=status.HTTP_400_BAD_REQUEST) 