from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    data=models.Product.objects.all()
    return render(request,'main.html',{"data":data})

def contact(request):
    return render(request,'contact.html')