from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='products'),
    path('single/', single, name='single'),
]