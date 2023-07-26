from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView
from sneakers.forms import ContactForm
from sneakers.models import Brand, Product, SliderImage, ProdImage
from django.db.models import Count, Q
from django.contrib import messages
import random

def get_product_count_by_gender(gender, exclude_kids=False):
    if exclude_kids:
        return Product.objects.filter(Q(gender=gender) | Q(gender='U'), is_kids=False).count()
    else:
        return Product.objects.filter(is_kids=True).count()


def filter():
    total_prod_female = get_product_count_by_gender('F', exclude_kids=True)
    total_prod_male = get_product_count_by_gender('M', exclude_kids=True)
    total_prod_kids = get_product_count_by_gender('U', exclude_kids=False)

    prod_filter = {
        'total_prod_female': total_prod_female,
        'total_prod_male': total_prod_male,
        'total_prod_kids': total_prod_kids,
    }

    return prod_filter

def brand_slice():
    all_brands = Brand.objects.all()
    ten_brands = all_brands[:5]
    next_brands = all_brands[5:10]

    brands = {
        'ten_brands': ten_brands,
        'next_brands': next_brands,
    }

    return brands

def index(request):
    context = filter()
    context['image'] = ProdImage.objects.all()
    context['products'] = Product.objects.all()
    context['slider_image'] = SliderImage.objects.all()

    return render(request, 'sneakers/index.html', context)


def contacts(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            # Process the form data here (e.g., send the email)
            name = request.POST["name"]
            email = request.POST["email"]
            subject = request.POST["subject"]
            message = request.POST["message"]
            messages.success(request, 'Your form was sent successfully sended')
            return HttpResponseRedirect(reverse('contacts'))
    else:
        form = ContactForm()
    return render(request, 'sneakers/contact.html', {'form': form})

def products(request):
    context = filter()
    latest_products = Product.objects.order_by('-id')[:8]
    context['last_products'] = latest_products
    context['image'] = ProdImage.objects.all()
    context['products'] = Product.objects.all()
    context.update(brand_slice())

    return render(request, 'sneakers/products.html', context)

def single(request):
    context = brand_slice()

    return render(request, 'sneakers/single-page.html', context)

def get_category(request, product_name):
    context = filter()
    context.update(brand_slice())
    item = Product.objects.get(name=product_name)
    context['item'] = item
    context['category'] = Product.objects.get(pk=item.id)

    return render(request, "sneakers/single-page.html", context)

def mans(request):
    male_products = Product.objects.filter(gender__in=['M', 'U'], is_kids=False)

    context = {
        'male_products': male_products
    }

    return render(request, "sneakers/mans.html", context)

def woman(request):
    female_products = Product.objects.filter(gender__in=['F', 'U'], is_kids=False)

    context = {
        'female_products': female_products
    }

    return render(request, "sneakers/woman.html", context)

def kids(request):
    kids_products = Product.objects.filter(is_kids=True)

    context = {
        'kids_products': kids_products
    }

    return render(request, "sneakers/kids.html", context)

def about(request):
    return render(request, "sneakers/about.html")

def faq(request):
    return render(request, "sneakers/faq.html")

def terms(request):
    return render(request, "sneakers/terms.html")

def payments(request):
    return render(request, "sneakers/payment.html")

def shipping(request):
    return render(request, "sneakers/shipping.html")

class Search(ListView):

    template_name = 'sneakers/product_list.html'

    def get_queryset(self):
        search_query = self.request.GET.get('q')

        product_filter = Q(name__icontains=search_query)
        brand_filter = Q(brand__name__icontains=search_query)

        return Product.objects.filter(product_filter | brand_filter)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context