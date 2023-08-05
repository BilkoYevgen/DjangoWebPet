from .views import *
from django.urls import path

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('page/<int:page>/', products, name='paginator'),
    path('<str:product_name>/', get_category, name='get_category'),
    path('baskets/add/<int:product_id>/', add_to_basket, name="add_to_basket"),
    path('baskets/remove/<int:basket_id>/', remove_from_basket, name="remove_from_basket"),
]