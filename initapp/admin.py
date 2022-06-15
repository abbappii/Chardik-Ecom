from django.contrib import admin

# Register your models here.
from .models import ContactUs

class ContactAdmin(admin.ModelAdmin):
    list_display = ['email','personName']

admin.site.register(ContactUs,ContactAdmin)