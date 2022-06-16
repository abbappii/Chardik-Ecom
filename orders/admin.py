
from django.contrib import admin

from orders.database.coupon import (
    Coupon
)
from orders.database.cart_order import(
    OrderItem
)


class CouponAdmin(admin.ModelAdmin):
    list_display = ['id','coupon_name','coupon_amount']

admin.site.register(Coupon,CouponAdmin)

class OrderItem_admin(admin.ModelAdmin):
    list_display = ['id','customer','item','quantity','is_order']

admin.site.register(OrderItem,OrderItem_admin)
