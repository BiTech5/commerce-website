from django.shortcuts import render,redirect
from . import models
from django.contrib.auth.models import User
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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def signup(request):
    if request.method=='POST':
        first_name=request.POST.get('first')
        last_name=request.POST.get('last')
        email=request.POST.get('email')
        username=request.POST.get('username')
        passw=request.POST.get('password1')
        data=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=passw)
        data.save()
        return redirect('login')
    return render(request,'signup.html')

def cart(request):
    return render(request,'cart.html')

def product_detail(request,slug):
    detail=models.Product.objects.get(slug=slug)
    return render(request,'detail.html',{"detail":detail})

def checkout(request):
    return render(request,'checkout.html')