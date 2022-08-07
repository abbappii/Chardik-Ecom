

# importing initials 
from django.db.models.signals import post_save
from django.dispatch import receiver

# importing accounts
from products.database.discount_products import Discounts_product



@receiver(post_save,sender=Discounts_product)
def AddPrice_of_DiscountProducts(sender,instance,created,*args,**kwargs):
    try:
        if created:
                instance.price = round (instance.discount_product.regular_price - 
                ((instance.discount / 100 ) * instance.discount_product.regular_price))
                instance.save()
    except Exception as e:
        print(e)