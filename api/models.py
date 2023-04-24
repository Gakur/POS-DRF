from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Store(models.Model) :
    item_name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    item_quantity = models.PositiveIntegerField()
    item_buying_price = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.item_name   
    

class Inventory(models.Model):
    item_name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    item_quantity = models.PositiveIntegerField()
    rem_store = models.ForeignKey(Store, blank=True, null=True, on_delete=models.CASCADE,)

    class Meta:
        ordering = ('item_name',)
        verbose_name = 'inventory'

    def __str__(self):
        return self.item_name   

class Debts(models.Model):
    item_name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    item_quantity = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    debtors_name = models.CharField(max_length=150, unique=False)
    phone_number = PhoneNumberField(blank= True, null=False, unique=True)

    def __str__(self):
        return self.debtors_name
    
class Sales(models.Model):
    item_name = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    item_quantity = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()

    def __str__(self):
        return self.item_name
    
    def add_amount(self):
        amount = self.item_name.selling_price * self.item_quantity
        total_price = total_price + amount
        sales.save()
        return True
    

class Receipts(models.Model):
    item_name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    item_quantity = models.PositiveIntegerField() 
    total_cost =models.PositiveIntegerField(default=0)
    # tendered = ()
    # change = ()


class ReceiptVAT(models.Model):
    item_name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    item_quantity = models.PositiveIntegerField()
    vatable_amt = models.PositiveIntegerField()
    vat_amt = models.PositiveIntegerField()
    total_amount = models.PositiveIntegerField()
    # tendered = ()
    # change = ()


class Profits(models.Model):
    buying_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    profit = models.PositiveIntegerField()      

    def __str__(self):
        return self.profit