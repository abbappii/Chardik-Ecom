from django.contrib import admin

from inventory.models import Purchase,Supplier

admin.site.register(Supplier)

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['ref_code','date_of_purchase','supplier']
admin.site.register(Purchase,PurchaseAdmin)
