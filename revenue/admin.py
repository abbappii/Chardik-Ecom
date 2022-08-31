from django.contrib import admin
from revenue.models import (
    RevenueHistory
)

# Register your models here.
class radmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(RevenueHistory, radmin)
