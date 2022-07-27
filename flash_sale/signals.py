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

# @receiver(post_save,sender=FlashSale)
# def ChangeProductStatus_on_Created(sender,instance,created,*args,**kwargs):
#     try:
#         if created:
#             # products = Products.objects.get(id=instance.flash_products.id)
#             # instance.products.add(products)
#             # instance.products.set()
#             # instance.save()
#             print(instance.products.all())
#             # for product in instance.products.all():
#             #     product.is_in_flash_sale = True
#             #     product.save()
#             # print(instance.products.all())
#             # instance.save()
#     except Exception as e:
#         print(e)


# @receiver(post_save,sender=FlashSale)
# def ChangeProductStatus_on_Update(sender,instance,created,*args,**kwargs):
#     try:
#         if not created:
#             print(instance.products.all())
#             for product in instance.products.all():
#                 product.is_in_flash_sale = True
#                 product.save()
#     except Exception as e:
#         print(e)


# @receiver(pre_delete,sender=FlashSale)
# def ChangeProductStatus_on_Delete(sender,instance,using,*args,**kwargs):
#     try:
#         # print(instance.products.all())
#         for product in instance.products.all():
#             product.is_in_flash_sale = False
#             product.save()
#     except Exception as e:
#         print(e)



'''
Flash Sale Signals 
    - Created 
    - Updated
'''

## flash sale when created

@receiver(post_save,sender=FlashProducts)
def AddPrice_of_FlashProducts(sender,instance,created,*args,**kwargs):
    try:
        if created:
                instance.flash_price = round (instance.flash_product.regular_price - 
                ((instance.flash_sale.discount / 100 ) * instance.flash_product.regular_price))
                instance.save()
    except Exception as e:
        print(e)
        
# ## Flash sale when Updated 
# @receiver(post_save,sender=FlashSale)
# def UpdatePrice_of_FlashProducts(sender,instance,created,*args,**kwargs):
#     try:
#         if not created:
#             for product in instance.products.all():
#                 print(product)
#                 product.flash_product.flash_price = "hey"
#                 print(product.flash_product.first().flash_price)

#                 product.save()
#     # if not created:
        # instance.flash_price = round (instance.flash_product.regular_price - \
        #                     ((instance.flash_sale.discount / \
        #                     instance.flash_product.regular_price) * 100))
        # instance.save()
        # for product in instance.products.all():
        #     print(product.flash_product.first())
        # print([product.flash_product.first().flash_price for product in instance.products.all()])
            # product.flash_product.first().flash_price = 200
            # product.save()
        


    except Exception as e:
        print(e)


