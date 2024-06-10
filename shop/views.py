from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . import models
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    data=models.Product.objects.all()
    return render(request,'main.html',{"data":data})
@login_required(login_url='/login/')
def contact(request):
    return render(request,'contact.html')
@login_required(login_url='/login/')
def about(request):
    about_us=models.AboutUs.objects.all()
    return render(request,'about_us.html',{'about_us':about_us})

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
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
    if request.user.is_authenticated:
        return redirect('home')
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
def logout(request):
    auth.logout(request)
    return redirect('login')
@login_required(login_url='/login/')
def cart(request):
    cart_items = models.Cart.objects.filter(user=request.user)
    total_price = sum(item.product.dis_price * item.quantity for item in cart_items)
    
    context = {
        'cart_items': cart_items,
    }
    return render(request,'cart.html',context)
@login_required(login_url='/login/')
def product_detail(request,slug):
    detail=models.Product.objects.get(slug=slug)
    return render(request,'detail.html',{"detail":detail})
@login_required(login_url='/login/')
def checkout(request):
    return render(request,'checkout.html')


def add_to_cart(request, product_id):
    product = get_object_or_404(models.Product, id=product_id)
    user = request.user

    cart_item, created = models.Cart.objects.get_or_create(user=user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


def increase_quantity(request, item_id):
    cart_item = get_object_or_404(models.Cart, id=item_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

def decrease_quantity(request, item_id):
    cart_item = get_object_or_404(models.Cart, id=item_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(models.Cart, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')