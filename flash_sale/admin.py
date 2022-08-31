from django.contrib import admin
from flash_sale.models import (
    FlashSale,FlashProducts
)

# Register your models here.
admin.site.register(FlashSale)

# Flash Product Admin
class FlashProductAdmin(admin.ModelAdmin):
    list_display = ['id','flash_sale','flash_product','flash_price']
admin.site.register(FlashProducts,FlashProductAdmin)
