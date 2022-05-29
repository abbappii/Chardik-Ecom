
from django.contrib import admin
from accounts.models.user_model import (
    User
)
from accounts.models.profile import Profile,UserPermission

admin.site.register(User)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','get_permission','customer_ID']
admin.site.register(Profile,ProfileAdmin)
admin.site.register(UserPermission)

