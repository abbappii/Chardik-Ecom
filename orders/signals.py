
from django.db.models.signals import post_save
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


@receiver(post_save, sender=Order)
def coupon_count(sender, instance,created, *args, **kwargs):
    if created:
        '''
        work 
            - get coupon count value
                - - example: coupon_count = 7
            - need maximum user
            - expire date
        '''

        # get coupon_count 
        get_coupon = instance.coupon_count

        # get maximum user from coupon table 
        m_user = instance.coupon.maximum_user

        # get expire date of coupon 
        exp_date = instance.coupon.expire_date

        # logic implementation
        try:
            if get_coupon == m_user:
                instance.coupon.is_active = False
                instance.coupon.save()

            elif exp_date == now.date():
                instance.coupon.is_active = False
                instance.coupon.save()
            else:
                pass
        except Exception as e:
            print(e)

