from django.contrib import admin
from django.urls import path
from . import views
from . views import *   # for class based view import view

urlpatterns = [
    path('', views.homeview ,name='home'),
    # path('items/', views.itemview ,name='items-list'),
    # path('items/<pk>', views.itemview ,name='items-delete'),
    # path('update-items/<str:pk>', views.itemupdate ,name='items-update'),
    # path('customer/', views.customerview ,name='customer-list'),
    # path('customer/<pk>', views.customerview ,name='customer-delete'),
    # path('update-customer/<str:pk>', views.customerupdate ,name='customer-update'),


    #class based views
    # path('view-item/',ItemCreateView.as_view()),
    # path('item-list/',ItemListView.as_view()),
    # path('item-delete/<pk>',ItemDeleteView.as_view(),name='delete_item')

#simple view
path('class-item-view/',Classitemview.as_view(),name='class-item-view'),
path('class-item-update/<pk>',Classitemview.as_view(),name='class-item-update'),
path('class-item-delete/<pk>',Classitemview.as_view(),name='class-item-delete'),
path('class-customer-view/',Classcustomerview.as_view(),name='class-customer-view'),
path('class-customer-delete/<pk>',Classcustomerview.as_view(),name='class-customer-delete'),
path('class-customer-update/<pk>',Classcustomerview.as_view(),name='class-customer-update'),


]
