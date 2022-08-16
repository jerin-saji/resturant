from django.shortcuts import render,redirect

from .forms import Customerform, Itemform

from .models import *

# def home(request):
#     pass

def homeview(request):
    pass

def itemsview(request):
    pass

def customerview(request):
    pass

def itemview(request,pk):
    if request.method =='POST':
        form = Itemform(request.POST)
        if form.is_valid():
            Item.objects.create(**form.cleaned_data)
        return redirect('itemview')

    elif request.method == 'GET':
        form = Itemform
        if pk!=None:
            item_to_delete = Item.objects.get(id=pk)
            item_to_delete ()
            list2 = list(Item.objects.all().values())
            
        
        return render(request,'item_form.html',{'form' :form,'lists': list2})


def customerview(request,pk):   
    if request.method =='POST':
        form = Customerform(request.POST)
        if form.is_valid():
            Item.objects.create(**form.cleaned_data)
        return redirect('customerview')

    elif request.method == 'GET':
        form = Customerform
        if pk!=None:
            item_to_delete = Customer.objects.get(id=pk)
            item_to_delete ()
            cust_list = list(Customer.objects.all().values())
            
        
        return render(request,'customer_form.html',{'form' :form,'key1': cust_list})