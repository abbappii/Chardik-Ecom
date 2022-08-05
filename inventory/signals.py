from django.db.models.signals import post_save
from django.dispatch import receiver
from MainApplication.scripts.batch_ID import(
    unique_batchID_generate
)
from inventory.models import Purchase

from orders.database.cart_order import Order
from inventory.bank_model.baccounts import BankAccounts
from decimal import Decimal

@receiver(post_save,sender=Order)
def order_money_add_to_bank(sender,instance, created,*args,**kwargs):
    if created and instance.order_status == "Completed":
        bank = BankAccounts.objects.filter(bank_name='ORDERS_READ_ONLY').first()
       
        bank.amount += Decimal(instance.total)
        bank.save()


'''
Creating auto generated batch id 
'''

@receiver(post_save,sender=Purchase)
def Create_batchNO(sender,instance,created,*args,**kwargs):
    try:
        if created:
            instance.batch_no = unique_batchID_generate(instance)
            instance.save()
    except Exception as e:
        print(e)