from accounts.models.initials import InitModels
from django.conf import settings
from django.db import models
from orders.database.cart import Cart


'''
Order
'''


# Order Models
class Order (InitModels):
    user = models.ForeignKey( settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    orderItems = models.ManyToManyField(Cart)
    ordered = models.BooleanField(default=False)
    paymentId=models.CharField(max_length=264, blank=True, null=True)
    orderId=models.CharField(max_length=264, blank=True, null=True)

    # get total price for all of the items from cart
    def get_totals(self):
        total=0
        for order_item in self.orderItems.all():
            total+=order_item.get_total()
        return total



'''
Coupon Class 
    { Coupon usage 
        - fixed Card Discount
        - Parcentage Discount
    }
    models 
    property 
'''

coupon_choices = (
    ('Fixed Cart Discount','Fixed Cart Discount'),
    ('Parcentage Discount', 'Parcentage Discount')

)

class Coupon(InitModels):
    coupon_name = models.CharField(max_length=100,null=True,verbose_name=
        "Coupon Name")
    coupon_type = models.CharField(choices=coupon_choices,max_length=20,
        default=None,null=True,verbose_name="Coupon Type")
    coupon_amount = models.FloatField(null=True,default=0.00,
        verbose_name="Coupon Amount")
    free_shipping = models.BooleanField(default=False,null=True,
        verbose_name="Free Shipping Allow ?")
    expire_date = models.DateField(null=True,blank=True,auto_now_add=False)
    minimum_user = models.IntegerField(default=0,null=True,blank=True,verbose_name=
        "Minimum Users")
    minimum_sale = models.IntegerField(null=True,blank=True,verbose_name=
        "Minimum Sale")
    maximum_sale = models.IntegerField(null=True,blank=True,verbose_name=
        "Maximum Sale")


    def __str__(self):
        return str(self.coupon_name)

    class Meta:
        verbose_name_plural = "Coupon"
        app_label = "orders"



