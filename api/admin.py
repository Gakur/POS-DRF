from django.contrib import admin
from .models import Store, Inventory, Debts, Sales, Receipts, ReceiptVAT, Profits

# Register your models here.
admin.site.register(Store)
admin.site.register(Inventory)
admin.site.register(Debts)
admin.site.register(Sales)
admin.site.register(Receipts)
admin.site.register(ReceiptVAT)
admin.site.register(Profits)

