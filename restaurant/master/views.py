
from urllib import request
from django.shortcuts import render,redirect

from .forms import Customerform, Itemform
from django.http import HttpResponseRedirect

from .models import *

# def home(request):
#     pass

def homeview(request):
    return render(request,'master/home.html')


# def itemview(request, pk=None):
#     print(pk)
#     if request.method =='POST':
#         form = Itemform(request.POST)
#         if form.is_valid():
#             Item.objects.create(**form.cleaned_data)
#         return redirect(itemview)

    # elif request.method == 'GET':
    #     form = Itemform
    #     if pk!=None:
    #         item_to_delete = Item.objects.get(id=pk)
    #         item_to_delete.delete()
    #     list2 = list(Item.objects.all().values())
            
        
        # return render(request,'master/item_form.html',{'form' :form,'lists': list2})

# def itemupdate(request,pk):
#     ls = Item.objects.get(id=pk)
#     form = Itemform(instance=ls)

#     if request.method == 'POST':
#         form = Itemform(request.POST,instance=ls)
#         if form.is_valid():
#             form.save()
#             return redirect('/items/')

#     context = {'form':form}
    
#     return render(request,'master/update_item.html',context)




# def customerview(request,pk=None):   
    # all = Customer.objects.all().values  ###
    # print(all)
    # if request.method =='POST':
    #     form = Customerform(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         Customer.objects.create(**form.cleaned_data)
            
        # return redirect(customerview)

    # elif request.method == 'GET':
    #     form = Customerform
    #     if pk!=None:
    #         item_to_delete = Customer.objects.get(id=pk)
    #         item_to_delete.delete()
    #     cust_list = list(Customer.objects.all().values('id', 'customer_name', 'customer_contact', 'item_details__item_name'))
            
        
        # return render(request,'master/customer_form.html',{'form' :form,'key1': cust_list})


# def customerupdate(request,pk):
    
#     ls = Customer.objects.get(id=pk)
#     form = Customerform(instance=ls)

#     if request.method == 'POST':
#         form = Customerform(request.POST,instance=ls)
#         if form.is_valid():
#             form.save()
#             return redirect('/customer/')

#     context = {'form':form}
    
#     return render(request,'master/update_customer.html',context)


##------------------class based views by generic----------------------------------------##

from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.views import View

# class ItemCreateView(CreateView):
#     model= Item
#     form_class= Itemform
#     template_name="master/item_form.html"
#     success_url="/item-list/"

# class ItemListView(ListView):
#     model = Item
#     template_name = "master/listview_temp.html"

# class ItemDeleteView(DeleteView):
#     model = Item
#     success_url="/item-list/"
#     template_name = "master/listview_temp.html"


##=-----------------------------------class based simple view------------------------------------------------##

# class Classitemview(View):

#     def get(self,request,pk=None):
#         form = Itemform
#         if pk!=None:
#             item_to_delete = Item.objects.get(id=pk)
#             item_to_delete.delete()
#         list2 = list(Item.objects.all().values())
#         return render(request,'master/item_form.html',{'form' :form,'lists': list2})

#     def post(self,request,pk=None):
#         form = Itemform(request.POST)
#         if form.is_valid():
#             Item.objects.create(**form.cleaned_data)
#         return redirect('class-view')


##-----------------------------------by inheriting another class---------------------------------------------###

class Generalview(View):

    def get (self , request ,*args, **kwargs):
        form = self.form_class
        object_list = list(self.model.objects.all().values(*self.fields))
        page = {
            'form':form,
            'object_list':object_list
        }
        return render(request,self.template_name,page)


    def post (self , request ,pk =None,*args, **kwargs):

        if pk == None:
            form =self.form_class(request.POST)
            if form.is_valid():
                self.model.objects.create(**form.cleaned_data)

        else:
            object = self.model.objects.get(id=pk)
            if request.POST.get ('method')=='delete':
                object.delete()
        
            elif request.POST.get('method')=='edit':
                form = self.form_class(instance=object)
                return render(request,self.template_edit,{'form':form,'object':object})

            elif request.POST.get('method')=='update':
                form = self.form_class(request.POST,instance=object)
                if form.is_valid():
                    form.save()   

        return self.get(request,*args,**kwargs)











class Classitemview(Generalview):
    form_class = Itemform
    template_name = 'master/item_form.html'
    model = Item
    # success_url = 'class-item-view'
    fields = ['id', 'item_name','item_category','item_cost','company_name']
    template_edit = 'master/update_item.html'


class Classcustomerview(Generalview):
    form_class = Customerform
    template_name = 'master/customer_form.html'
    model = Customer
    # success_url = 'class-customer-view'
    fields = ['id', 'customer_name','customer_contact','item_details__item_name']
    template_edit = 'master/update_customer.html'