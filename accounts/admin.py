
from django.contrib import admin
from accounts.models.user_model import (
    User
)
from accounts.models.profile import (
    Profile,UserPermission,BillingAddress
)

admin.site.register(User)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','customer_ID','get_permission_id']
admin.site.register(Profile,ProfileAdmin)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ['id','permission_name']
admin.site.register(UserPermission,PermissionAdmin)
admin.site.register(BillingAddress)

# admin.site.register(ShippingAddress)
