from django.db.models import Sum
from .models import Basket

def cart_quantity(request):
    if request.user.is_authenticated:
        basket_count = Basket.objects.filter(user=request.user).aggregate(Sum('quantity'))['quantity__sum'] or 0
    else:
        basket_count = 0
    return {'basket_count': basket_count}