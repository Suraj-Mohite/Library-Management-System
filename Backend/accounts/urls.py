import imp

from django.urls import path,include


urlpatterns = [
    path('api/login/',include('rest_framework.urls')),
]
