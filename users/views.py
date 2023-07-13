from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')

def profile(request):
    return render(request, 'users/profile.html')

def email_verification(request):
    return render(request, 'users/email_verification.html')