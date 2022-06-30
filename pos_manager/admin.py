from django.contrib import admin
from .models import OfflineSale

# Register your models here.

class OfflineSaleAdmin(admin.ModelAdmin):
    list_display = ['id','outlet','user','product','is_active']
    ordering = ['-id']

admin.site.register(OfflineSale,OfflineSaleAdmin)
