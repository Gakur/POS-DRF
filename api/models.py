from django.db import models

# Create your models here.
class Store(models.Model) :
    item_name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    item_quantity = models.PositiveIntegerField()
    item_buying_price = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self    
    

class Inventory(models.Model):
    item_name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    item_quantity = models.PositiveIntegerField()

    class Meta:
        ordering = ('item_name')
        verbose_name = 'inventory'

    def __str__(self):
        return self.item_name    

class Debts(models.Model):
    item_name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    item_quantity = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    debtors_name = models.CharField(max_length=150, unique=False)
    phone_number = models.PhoneNumberField((""))

    def __str__(self):
        return self.debtors_name
    
class Sales(models.Model):
    item_name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    item_quantity = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()

    def __str__(self):
        return self.sales
    

class Receipts(models.Model):
    item_name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    item_quantity = models.PositiveIntegerField() 
    total_cost =models.PositiveIntegerField(default=0)
    # tendered = ()
    # change = ()


class ReceiptVAT(models.Model):
    item_name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    item_quantity = models.PositiveIntegerField()
    vatable_amt = ()
    vat_amt = ()
    total_amount = ()
    # tendered = ()
    # change = ()


class Profits(models.Model):
    buying_price = ()
    selling_price = ()
    profit = ()        
