
from django.contrib import admin

from orders.database.order import Coupon


class CouponAdmin(admin.ModelAdmin):
    list_display = ['id','coupon_name','coupon_amount']

admin.site.register(Coupon,CouponAdmin)
