
# importing initials 
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.database.damage_products import DamageProducts

# importing accounts
from products.database.discount_products import Discounts_product

from revenue.models import RevenueHistory
from django.db.models import Sum

import datetime
date = datetime.date.today()
now = datetime.datetime.today()


@receiver(post_save,sender=Discounts_product)
def AddPrice_of_DiscountProducts(sender,instance,created,*args,**kwargs):
    try:
        if created:
                instance.price = round (instance.discount_product.regular_price - 
                ((instance.discount / 100 ) * instance.discount_product.regular_price))
                instance.save()
    except Exception as e:
        print(e)


# if damage: return reduce money form revenue 


@receiver(post_save,sender = DamageProducts)
def ReduceDamage_money_from_daily_revenue(sender,instance,created,*args,**kwargs):
   
    if created:

        try:
            last_revenue_history = RevenueHistory.objects.last()
            # print(last_revenue_history.id)
            last_revenue_history.profits -= instance.total_loss
            last_revenue_history.save()

        except Exception as e:
            print(e)