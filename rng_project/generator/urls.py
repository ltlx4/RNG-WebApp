from django.urls import path
from .views import Generator

urlpatterns = [
    path('', Generator.as_view(), name='index'),
] 
