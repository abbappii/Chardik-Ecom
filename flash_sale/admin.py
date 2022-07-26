from django.contrib import admin
from flash_sale.models import (
    FlashSale,FlashProducts
)

# Register your models here.
admin.site.register(FlashSale)
admin.site.register(FlashProducts)
