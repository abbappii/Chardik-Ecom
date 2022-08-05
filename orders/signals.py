
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from orders.database.cart_order import Order

from utils.util import Util

from django.utils import timezone
now = timezone.now()

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



'''
this function for get coupon count and validations check
'''

@receiver(pre_save, sender=Order)
def coupon_count(sender, instance, *args, **kwargs):
    
    try:

        if instance.coupon.coupon_count == instance.coupon.maximum_user:
                instance.coupon.is_active = False
                instance.coupon.save()

        elif instance.coupon is not None:
            instance.coupon.coupon_count += 1
            instance.coupon.save()
        else:
            pass 

    except Exception as e:
        print(e)