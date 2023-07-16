from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from sneakers.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('products/', include('sneakers.urls', namespace="products")),
    path('users/', include('users.urls', namespace='users')),
    path('contacts/', contacts, name='contacts'),
    path('campaings/', campaings, name='campaings'),
    path('services/', services, name='services'),
    path('brands/', brands, name='brands'),
    path('about/', about, name='about'),
    path('faq/', faq, name='faq'),
    path('terms/', terms, name='terms'),
    path('payments/', payments, name='payments'),
    path('shipping/', shipping, name='shipping'),
]

if settings.DEBUG:
    urlpatterns = [
        path("__debug__/", include("debug_toolbar.urls")),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

