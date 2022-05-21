from accounts.models import InitModels
from django.conf import settings
from django.db import models
from orders.database.cart import Cart


'''
Order
'''


# Order Models
class Order (InitModels):
    user = models.ForeignKey( settings.AUTH_USER_MODEL,on_delete=models.CASCADE )
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

