from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView
from sneakers.forms import ContactForm
from sneakers.models import Brand, Product, SliderImage, ProdImage, Basket
from django.db.models import Count, Q
from django.contrib import messages
from users.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

def get_product_count_by_gender(gender, exclude_kids=False):
    if exclude_kids:
        return Product.objects.filter(Q(gender=gender) | Q(gender='U'), is_kids=False, is_published=True).count()
    else:
        return Product.objects.filter(is_kids=True, is_published=True).count()


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
    context['products'] = Product.objects.filter(is_published=True)
    context['slider_image'] = SliderImage.objects.all()

    return render(request, 'sneakers/index.html', context)


def contacts(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            # Send the email
            send_mail(
                subject,
                f"From: {name}\nEmail: {email}\n\n{message}",
                'your_email@example.com',  # Sender's email address
                ['recipient@example.com'],  # List of recipient email addresses
                fail_silently=False,
            )
            messages.success(request, 'Your form was sent successfully sent')
            return HttpResponseRedirect(reverse('contacts'))
    else:
        form = ContactForm()
    return render(request, 'sneakers/contact.html', {'form': form})


def products(request, page=1):
    context = filter()
    context['image'] = ProdImage.objects.all()
    all_products = Product.objects.filter(is_published=True).order_by('id')
    per_page = 8

    paginator = Paginator(all_products, per_page)

    try:
        page_number = int(page)
    except ValueError:
        page_number = 1

    try:
        products_paginator = paginator.page(page_number)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)

    context['products'] = products_paginator
    context.update(brand_slice())

    return render(request, 'sneakers/products.html', context)


def get_category(request, product_name):
    context = filter()
    context.update(brand_slice())
    item = get_object_or_404(Product, name=product_name, is_published=True)
    context['item'] = item
    context['category'] = Product.objects.get(pk=item.id)
    context['image'] = ProdImage.objects.filter(product__name=product_name)

    return render(request, "sneakers/single-page.html", context)


class MansList(ListView):
    model = Product
    template_name = "sneakers/mans.html"
    context_object_name = "male_products"
    paginate_by = 8
    ordering = ['-id']

    def get_queryset(self):
        return Product.objects.filter(gender__in=['M', 'U'], is_kids=False, is_published=True).order_by(*self.ordering)

class WomansList(ListView):
    model = Product
    template_name = "sneakers/woman.html"
    context_object_name = "female_products"
    paginate_by = 8
    ordering = ['-id']
    def get_queryset(self):
        return Product.objects.filter(gender__in=['F', 'U'], is_kids=False, is_published=True).order_by(*self.ordering)


class KidsList(ListView):
    model = Product
    template_name = "sneakers/kids.html"
    context_object_name = "kids_products"
    paginate_by = 8
    ordering = ['-id']
    def get_queryset(self):
        return Product.objects.filter(is_kids=True, is_published=True).order_by(*self.ordering)


def search_view(request):
    template_name = 'sneakers/product_list.html'
    search_query = request.GET.get('q')

    product_filter = Q(name__icontains=search_query, is_published=True)
    brand_filter = Q(brand__name__icontains=search_query, is_published=True)

    queryset = Product.objects.filter(product_filter | brand_filter)

    context = {
        'object_list': queryset,
        'q': search_query,
    }

    return render(request, template_name, context)


@login_required
def add_to_basket(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    messages.success(request, "Added successfully")

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def remove_from_basket(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

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