from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.database.cart_order import Order
from inventory.bank_model.baccounts import BankAccounts
from decimal import Decimal

@receiver(post_save,sender=Order)
def order_money_add_to_bank(sender,instance, created,*args,**kwargs):
    if created:
        bank = BankAccounts.objects.get(bank_name='ORDERS_READ_ONLY')
        try:
            bank.amount += Decimal(instance.total)
            bank.save()

        except Exception as e:
            print(e)