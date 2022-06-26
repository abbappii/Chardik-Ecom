from django.contrib import admin

from .database.admin_post import AdminBlog
from .database.customer_post import CustomerBlog

# Register your models here.

class AdminBlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','is_active']
admin.site.register(AdminBlog,AdminBlogAdmin)

class CustomerBlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','is_active']
admin.site.register(CustomerBlog,CustomerBlogAdmin)
