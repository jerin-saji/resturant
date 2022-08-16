from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_category = models.CharField(max_length=50)
    item_cost = models.FloatField()
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_contact = models.CharField(max_length=10)
    item_details = models.ForeignKey(Item,on_delete=models.CASCADE,null=True,blank=True)
    

    def __str__(self):
        return self.customer_name


