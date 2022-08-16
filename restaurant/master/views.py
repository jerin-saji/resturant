from django.shortcuts import render,redirect

from .forms import Customerform, Itemform
from django.http import HttpResponseRedirect

from .models import *

# def home(request):
#     pass

def homeview(request):
    pass


def itemview(request, pk=None):
    print(pk)
    if request.method =='POST':
        form = Itemform(request.POST)
        if form.is_valid():
            Item.objects.create(**form.cleaned_data)
        return redirect(itemview)

    elif request.method == 'GET':
        form = Itemform
        if pk!=None:
            item_to_delete = Item.objects.get(id=pk)
            item_to_delete.delete()
        list2 = list(Item.objects.all().values())
            
        
        return render(request,'master/item_form.html',{'form' :form,'lists': list2})


def customerview(request,pk=None):   
    if request.method =='POST':
        form = Customerform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Customer.objects.create(**form.cleaned_data)
        return redirect(customerview)

    elif request.method == 'GET':
        if pk!=None:
            item_to_delete = Customer.objects.get(id=pk)
            item_to_delete.delete()
        form = Customerform
        cust_list = list(Customer.objects.all().values())
            
        
        return render(request,'master/customer_form.html',{'form' :form,'key1': cust_list})