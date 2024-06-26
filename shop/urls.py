from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('contact-us/',views.contact,name='contact'),
    path('about-us/',views.about,name='about'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('cart/',views.cart,name='cart'),
    path('detail/<slug>/',views.product_detail,name='detail'),
    path('checkout/',views.checkout,name='checkout'),
    path('logout/',views.logout,name='logout'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
     path('cart/increase/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]