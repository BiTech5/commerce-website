from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('contact-us/',views.contact,name='contact'),
    path('about-us/',views.about,name='about'),
]