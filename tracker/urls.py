from django.urls import path
from .views import *

urlpatterns = [
    
     path('', IndexView.as_view(), name='index'),  # Home page route
     path('api/log-number/<int:number>/', NumberPressView.as_view(), name='log_number'),
    
]
