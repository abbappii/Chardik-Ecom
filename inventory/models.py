'''
This file contaisn the Database layout of 
    Inventory Management 
'''

from django.db import models
from accounts.models.initials import InitModels
from decimal import Decimal
# from MainApplication.scripts.batch_ID import unique_batchID_generate


'''
Supplier models
'''

class Supplier(InitModels):
    name = models.CharField(
        max_length=200,
        null=True,
        verbose_name="Supplier Name"
        )
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    description = models.TextField(null=True,verbose_name="Description")
    address = models.TextField(null=True, verbose_name="Address")
    country = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Country Name"
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Supplier List" 

'''
Purchase Models 
    '''

order_status = (
    ('Received','Recieved'),
    ('Pending','Pending'),
    ('Ordered','Ordered')
)

payment_status = (
    ('Pending','Pending'),
    ('Partial','Partial'),
    ('Paid','Paid')
)


class Purchase(InitModels):
    ref_code = models.CharField(max_length=100,null=True,blank=True,verbose_name=
        "Reference Number")
    batch_no = models.CharField(max_length=100,null=True,blank=True,verbose_name=
        "Batch No",editable=False)
    date_of_purchase = models.DateField(auto_now_add=False,null=True,blank=True,
        verbose_name="Date of Purchase")
    supplier = models.ForeignKey(Supplier,on_delete=models.SET_NULL,null=True,
        verbose_name="Select Supplier",related_name="purchase")
    order_status = models.CharField(max_length=100,choices=order_status,null=True,
        verbose_name="Order Status")
    # outlet_name = models.CharField(max_length=300,null=True,blank=True,verbose_name=
    #     "Outlet Name")
    outlet_name = models.ForeignKey('inventory.Outlet', on_delete=models.SET_NULL, null=True,related_name='p_outlet_name')

    product = models.ForeignKey('products.Products',null=True,on_delete=models.SET_NULL,
        verbose_name="Select product",related_name='purchase_product')
        
    price = models.FloatField(null=True,verbose_name="Prce")
    unit_cost = models.FloatField(null=True,blank=True,default=0.0,verbose_name="Net Unit Cost")
    other_cost = models.FloatField(null=True,verbose_name="Other Cost",default=0.0)
    due_price = models.FloatField(null=True,default=0.0,blank=True,verbose_name="Due Price")
    # payment_method = models.CharField(null=True,blank=True,max_length=200,
    #     verbose_name="Payment Method")
    payment_method = models.ForeignKey('inventory.BankAccounts', on_delete=models.SET_NULL,null=True,related_name='bank_acc_name')

    payment_status = models.CharField(max_length=100,null=True,blank=True,choices=
        payment_status,verbose_name="Payment Status")
    description = models.TextField(null=True,blank=True,verbose_name="Description")
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)


    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name_plural = "Purchase History"

    ## Net price calculated
    @property
    def Net_unitPrice(self):
        price = self.price + self.other_cost + self.unit_cost
        net_price = price / self.quantity

        return round(net_price,2)


    def save(self, *args, **kwargs):
        if not self.pk:
            total_purchase_amount = self.price
            try:
                account = self.payment_method
                account.amount -= Decimal(total_purchase_amount)
                account.save()
                # instance.payment_method.amount -= Decimal(total_purchase_amount)
                # instance.payment_method.save()
                
          
            except Exception as e:
                print(e)
        super().save(*args, **kwargs)
 