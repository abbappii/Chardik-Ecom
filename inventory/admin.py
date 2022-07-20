from django.contrib import admin

from inventory.models import Purchase,Supplier

from inventory.bank_model.baccounts import BankAccounts

admin.site.register(Supplier)

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['ref_code','date_of_purchase','supplier']
admin.site.register(Purchase,PurchaseAdmin)

# Bank accounts 
class BankAccountsAdmin(admin.ModelAdmin):
    list_display = ['id','bank_name', 'amount','is_active']

admin.site.register(BankAccounts, BankAccountsAdmin)

