from django.urls import path
from . import views
from .views import *

urlpatterns = [ 
     path('generate-password/', views.generate_and_send_password, name='generate-password'),    
     path('home/', views.index, name='home'),  # Home page route
     path('api/log-number/', views.log_number_endpoint, name='log_number_endpoint'),
     path('api/reset-table/<str:table>', ResetTableView.as_view(), name='reset_view')
    
]
