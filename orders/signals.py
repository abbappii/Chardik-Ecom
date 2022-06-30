
from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.database.cart_order import Order

@receiver(post_save,sender=Order)
def points(sender,instance, created,*args,**kwargs):
    
    if created:
        if instance.order_total_price <= 1000:
            points_gained = 0.01 * instance.order_total_price
        elif instance.order_total_price >1000 and instance.order_total_price <= 3000:
            points_gained = 0.03 * instance.order_total_price
        elif instance.order_total_price >3000 and instance.order_total_price <= 5000:
            points_gained = 0.05 * instance.order_total_price
        elif instance.order_total_price >5000 and instance.order_total_price <= 10000:
            points_gained = 0.07 * instance.order_total_price
        else:
            points_gained = 0.08 * instance.order_total_price


    