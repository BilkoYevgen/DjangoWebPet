from django.conf import settings
from django.conf.urls.static import static

from .views import *
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('login/', loging, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('email_verification/', email_verification, name='email_verification'),
    path('logout/', logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns = [
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)