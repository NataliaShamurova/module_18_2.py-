from django.urls import path
from . import views

urlpatterns = [
    path('register/django', views.sign_up_by_django, name='register'),
    path('register/html', views.sign_up_by_html, name='register_html'),
]
