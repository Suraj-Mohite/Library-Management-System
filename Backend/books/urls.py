from django.urls import path
from books.views import BooksApiView,SingleBookApiView,CreateBooksApiView

urlpatterns = [
    path('api/books/',BooksApiView.as_view() ),
    path('api/book/',CreateBooksApiView.as_view() ),
    path('api/book/<int:pk>/',SingleBookApiView.as_view() ),
]