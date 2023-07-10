from .views import *
from django.urls import path

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('products/', products),
    path('single/', single),
]