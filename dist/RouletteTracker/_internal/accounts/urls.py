# accounts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('api/login', views.login_endpoint, name='login_endpoint'),
    path('register/', views.register, name='register'),
    path('api/register', views.register_endpoint, name='register_endpoint')
   
]