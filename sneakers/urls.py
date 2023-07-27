from .views import *
from django.urls import path

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('single/', single, name='single'),
    path('<str:product_name>', get_category, name='get_category'),
    path('mans/', mans, name='mans'),
    path('woman/', woman, name='woman'),
    path('kids/', kids, name='kids'),
    path('baskets/add/<int:product_id>', add_to_basket, name="add_to_basket"),
    path('baskets/remove/<int:basket_id>', remove_from_basket, name="remove_from_basket"),
]