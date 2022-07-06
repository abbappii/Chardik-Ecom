
from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.database.cart_order import Order

from utils.util import Util

@receiver(post_save,sender=Order)
def points_count(sender,instance, created,*args,**kwargs):
    if created:
        points_gained = Util.points_calculate(instance.total)

        try:
            profile = instance.customer
            profile.points_gained += points_gained
            profile.save()

        except Exception as e:
            pass