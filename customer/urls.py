from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:id>/', views.customer_detail, name= 'customer_detail'),
]