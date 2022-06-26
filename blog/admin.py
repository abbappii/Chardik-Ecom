from django.contrib import admin

from blog.database.blog import Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','is_active']
admin.site.register(Blog,BlogAdmin)

