from django.urls import path
from . import views
from .views import *

urlpatterns = [
    
     path('', views.index, name='index'),  # Home page route
     path('api/log-number/<int:number>/', NumberPressView.as_view(), name='log_number'),
     path('api/reset-table/<str:table>', ResetTableView.as_view(), name='reset_view')
    
]
