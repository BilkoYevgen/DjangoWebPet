from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView
from sneakers.forms import ContactForm
from sneakers.models import Brand, Product, SliderImage
from django.db.models import Count, Q
from django.contrib import messages

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



def services(request):
    return HttpResponse("Under construction")

def brands(request):
    return HttpResponse("Under construction")

def about(request):
    return HttpResponse("Under construction")

def faq(request):
    return HttpResponse("Under construction")

def terms(request):
    return HttpResponse("Under construction")

def payments(request):
    return HttpResponse("Under construction")

def shipping(request):
    return HttpResponse("Under construction")

def campaings(request):
    return HttpResponse("Under construction")