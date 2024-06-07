from django.shortcuts import render
from . import models
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    data=models.Product.objects.all()
    return render(request,'main.html',{"data":data})

def contact(request):
    return render(request,'contact.html')

def about(request):
    about_us=models.AboutUs.objects.all()
    return render(request,'about_us.html',{'about_us':about_us})

def login(request):
    return render(request,'login.html')


def signup(request):
    return render(request,'signup.html')

def cart(request):
    return render(request,'cart.html')