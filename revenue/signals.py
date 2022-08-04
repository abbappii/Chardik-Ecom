'''
This app is created for Creating history list

'''
# importing initials 
from django.dispatch import receiver
from django.db.models.signals import post_save

# importing models 
from orders.database.cart_order import (
    Order,
    OrderItem
)
from products.database.products import(
    Products
)
from revenue.models import (
    RevenueHistory
)

##  signals for creating  Revenue History

@receiver(post_save,sender=Order)
def CreateHistory(sender,instance,created,*args,**kwargs):

    try:
        if created:
            for orderItem in instance.items:
                print(orderItem)
    except Exception as e:
        print(e)



@receiver(post_save,sender=Order)
def UpdateHistory(sender,instance,created,*args,**kwargs):

    try:
        if not created and instance.order_status == 'Completed':
            for orderItem in instance.items.all():
                # print(orderItem)
                # print(orderItem.item.quantity)
                print(orderItem.item.purchase_product.last().price)
                
                obj = RevenueHistory(
                        purchase_code = orderItem.item.\
                            purchase_product.last().batch_no,
                        product_name = orderItem.item,
                        purchase_unit = orderItem.item.\
                            purchase_product.last().price,
                        selling_unit = orderItem.amount_item ,
                        quantity = orderItem.quantity   
                )
                obj.save()
    except Exception as e:
        print(e)