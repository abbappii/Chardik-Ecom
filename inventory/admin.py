from django.contrib import admin

from inventory.models import Purchase,Supplier

from inventory.bank_model.baccounts import (
    BankAccounts, 
    DepositWithdraw,
    Name,
    Outlet,
    Expenses
    )

admin.site.register(Supplier)

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id','batch_no','date_of_purchase','supplier','Net_unitPrice']
admin.site.register(Purchase,PurchaseAdmin)

# Bank accounts 
class BankAccountsAdmin(admin.ModelAdmin):
    list_display = ['id','bank_name', 'amount','is_active']

admin.site.register(BankAccounts, BankAccountsAdmin)

# withdraw deposit admin 
class DepositWithdrawAdmin(admin.ModelAdmin):
    list_display = ['id','account','Reference','created_by']

admin.site.register(DepositWithdraw)

admin.site.register(Name)
admin.site.register(Outlet)
admin.site.register(Expenses)