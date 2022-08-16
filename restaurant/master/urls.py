from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeview ,name='home'),
    path('items/', views.itemview ,name='items-list'),
    path('items/<pk>', views.itemview ,name='items-delete'),
    path('customer', views.customerview ,name='customer-list'),
    path('customer/<pk>', views.customerview ,name='customer-delete'),
]
