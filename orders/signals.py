
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models.user_model import User 
from orders.database.cart_order import Order

@receiver(post_save,sender=Order)
def MyCallBack(sender,instance, created,*args,**kwargs):
    print('hello world!')
    if created:
        if instance.total <= 1000:
            points_gained = 0.01 * instance.total
        elif instance.total >1000 and instance.total <= 3000:
            points_gained = 0.03 * instance.total
        elif instance.total >3000 and instance.total <= 5000:
            points_gained = 0.05 * instance.total
        elif instance.total >5000 and instance.total <= 10000:
            points_gained = 0.07 * instance.total
        else:
            points_gained = 0.08 * instance.total

        
        try:
            points = User.objects.get(user=instance.user)
            print(points)
            points.profile.points_gained = points_gained
            points.profile.save(update_fields=['points_gained'])

        except Exception as e:
            print(e)


    