from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeview ,name='home'),
    path('items/', views.itemview ,name='items-list'),
    path('items/<pk>', views.itemview ,name='items-delete'),
    path('update-items/<str:pk>', views.itemupdate ,name='items-update'),
    path('customer/', views.customerview ,name='customer-list'),
    path('customer/<pk>', views.customerview ,name='customer-delete'),
    path('update-customer/<str:pk>', views.customerupdate ,name='customer-update'),
]
