from rest_framework import serializers

from books.models import BookInfo

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookInfo
        fields='__all__'