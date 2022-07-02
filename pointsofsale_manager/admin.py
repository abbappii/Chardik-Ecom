from django.contrib import admin
from pointsofsale_manager.models import PointsOfSale
# Register your models here.

class PosAdmin(admin.ModelAdmin):
    list_display = ['id','outlet','user']
    ordering = ['-id']
admin.site.register(PointsOfSale,PosAdmin)