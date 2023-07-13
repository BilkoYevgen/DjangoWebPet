from .views import *
from django.urls import path

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('single/', single, name='single'),
]