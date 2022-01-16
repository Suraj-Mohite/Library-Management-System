from django.contrib import admin

from books.models import BookInfo

# Register your models here.
@admin.register(BookInfo)
class bookInfoAdmin(admin.ModelAdmin):
    list_display=['id','title','author','price','publisher']