from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('card/', views.cart_page, name='card'),
    path('product/', views.shop_page, name='product'),


]
