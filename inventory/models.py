'''
This file contaisn the Database layout of 
    Inventory Management 
'''

from django.db import models
from accounts.models.initials import InitModels



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
        "Batch No")
    date_of_purchase = models.DateField(auto_now_add=False,null=True,blank=True,
        verbose_name="Date of Purchase")
    supplier = models.ForeignKey(Supplier,on_delete=models.SET_NULL,null=True,
        verbose_name="Select Supplier",related_name="purchase")
    order_status = models.CharField(max_length=100,choices=order_status,null=True,
        verbose_name="Order Status")
    outlet_name = models.CharField(max_length=300,null=True,blank=True,verbose_name=
        "Outlet Name")
    product = models.ForeignKey('products.Products',null=True,on_delete=models.SET_NULL,
        verbose_name="Select product")
    price = models.FloatField(null=True,verbose_name="Prce")
    unit_cost = models.FloatField(null=True,blank=True,verbose_name="Net Unit Cost")
    other_cost = models.FloatField(null=True,verbose_name="Other Cost")
    due_price = models.FloatField(null=True,blank=True,verbose_name="Due Price")
    payment_method = models.CharField(null=True,blank=True,max_length=200,
        verbose_name="Payment Method")
    payment_status = models.CharField(max_length=100,null=True,blank=True,choices=
        payment_status,verbose_name="Payment Status")
    description = models.TextField(null=True,blank=True,verbose_name="Description")
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)


    def __str__(self):
        return self.ref_code

    class Meta:
        verbose_name_plural = "Purchase History"


    
    