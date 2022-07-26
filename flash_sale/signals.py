'''
THis file contains the Logic of following 
    - Flash sale Products status change 
    - if inactive product`s status will revert again  
'''

# importing initials 
from django.db.models.signals import post_save,pre_delete,pre_save
from django.dispatch import receiver

# importing accounts
from flash_sale.models import FlashProducts, FlashSale
from products.database.products import Products


'''
Logic of 
    - product status change when created 
'''

@receiver(post_save,sender=FlashSale)
def ChangeProductStatus_on_Created(sender,instance,created,*args,**kwargs):
    try:
        if created:
            # products = Products.objects.get(id=instance.flash_products.id)
            # instance.products.add(products)
            # instance.products.set()
            # instance.save()
            print(instance.products.all())
            # for product in instance.products.all():
            #     product.is_in_flash_sale = True
            #     product.save()
            # print(instance.products.all())
            # instance.save()
    except Exception as e:
        print(e)


@receiver(post_save,sender=FlashSale)
def ChangeProductStatus_on_Update(sender,instance,created,*args,**kwargs):
    try:
        if not created:
            print(instance.products.all())
            for product in instance.products.all():
                product.is_in_flash_sale = True
                product.save()
    except Exception as e:
        print(e)


@receiver(pre_delete,sender=FlashSale)
def ChangeProductStatus_on_Delete(sender,instance,using,*args,**kwargs):
    try:
        # print(instance.products.all())
        for product in instance.products.all():
            product.is_in_flash_sale = False
            product.save()
    except Exception as e:
        print(e)



'''
Flash Sale Signals 
'''

@receiver(post_save,sender=FlashProducts)
def UpdatePrice_of_FlashProducts(sender,instance,created,*args,**kwargs):
    try:
        if created:
            # for product in instance.products.all():
                # instance.flash_price = 100 * instance.
                # print(instance._meta.get_fields())
                print(instance.flash_sale.discount)
                print(instance.flash_product.regular_price)
                instance.flash_price = instance.flash_sale.discount / instance.flash_product.regular_price
                instance.save()
    except Exception as e:
        print(e)
    # if created:
    #     print(instance.id)