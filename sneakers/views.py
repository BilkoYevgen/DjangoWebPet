from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'sneakers/index.html')

def contacts(request):
    return render(request, 'sneakers/contact.html')

def products(request):
    return render(request, 'sneakers/products.html')

def single(request):
    return render(request, 'sneakers/single-page.html')