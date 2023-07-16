from .views import *
from django.urls import path

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('single/', single, name='single'),
    # path('<int:product_id>', single, name='single'),
]