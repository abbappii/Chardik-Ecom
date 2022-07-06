
from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.database.cart_order import Order

from accounts.models.profile import Profile

@receiver(post_save,sender=Order)
def points_count(sender,instance, created,*args,**kwargs):
    # print('hello world!')
    if created:
        if instance.total <= 1000:
            points_gained = 0.1 * instance.total
        elif instance.total >1000 and instance.total <= 3000:
            points_gained = 0.3 * instance.total
        elif instance.total >3000 and instance.total <= 5000:
            points_gained = 0.5 * instance.total
        elif instance.total >5000 and instance.total <= 10000:
            points_gained = 0.7 * instance.total
        else:
            points_gained = 0.8 * instance.total


        #get user
        user = instance.user 
        try:
            # points instance check 
            points = Profile.objects.get(points_gained = user.profile.points_gained)
            print(points)
            # asign points value 
            points.profile.points_gained = points_gained
            # save points 
            points.profile.save(update_fields=['points_gained'])

        except:
            points = user.profile.points_gained 
            points = points_gained
            points.save()