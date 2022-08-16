from django.forms import ModelForm
from.models import *


class Itemform(ModelForm):
    class Meta:
        model = Item
        fields = ('item_name','item_category','item_cost','company_name')

class Customerform(ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_name','customer_contact')

