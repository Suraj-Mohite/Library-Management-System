from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from books.models import BookInfo
from books.serializers import BooksSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser,AllowAny
# Create your views here.

class BooksApiView(APIView):
    serializer_class=BooksSerializer
    authentication_classes=[SessionAuthentication,]
    permission_classes=[AllowAny,]

    def get(self,request,format=None):
        data=BookInfo.objects.all()
        serializer=self.serializer_class(data,many=True)
        serialized_data=serializer.data
        return Response(serialized_data,status=status.HTTP_200_OK)

class CreateBooksApiView(APIView):
    serializer_class=BooksSerializer
    authentication_classes=[SessionAuthentication,]
    permission_classes=[IsAdminUser,]
    
    def post(self,request,format=None):
        print(request.data)
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data=serializer.data
            return Response(serialized_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class SingleBookApiView(APIView):
    serializer_class=BooksSerializer
    authentication_classes=[SessionAuthentication,]
    permission_classes=[IsAdminUser,]

    def get_object(self,pk):
        try:
            return BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        serializer=self.serializer_class(self.get_object(pk))
        serialized_data=serializer.data
        return Response(serialized_data,status=status.HTTP_200_OK)
    
    def put(self,request,pk,format=None):
        book=self.get_object(pk)
        serializer=self.serializer_class(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data=serializer.data
            return Response(serialized_data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        book=self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)