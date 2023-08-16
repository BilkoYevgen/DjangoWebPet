from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from sneakers.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('captcha/', include('captcha.urls')),

    path('products/', include('sneakers.urls', namespace="products")),
    path('users/', include('users.urls', namespace='users')),
    path('contacts/', contacts, name='contacts'),
    path('mans/', MansList.as_view(), name='mans'),
    path('woman/', WomansList.as_view(), name='woman'),
    path('kids/', KidsList.as_view(), name='kids'),
    path('about/', about, name='about'),
    path('faq/', faq, name='faq'),
    path('terms/', terms, name='terms'),
    path('payments/', payments, name='payments'),
    path('shipping/', shipping, name='shipping'),
    path('search/', search_view, name='search'),

    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/product/', SneakersViewSet.as_view()),
    path('api/v1/product/<int:pk>/', SneakersDetailViewSet.as_view()),
]

if settings.DEBUG:
    urlpatterns = [
        path("__debug__/", include("debug_toolbar.urls")),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

