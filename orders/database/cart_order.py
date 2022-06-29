from accounts.models.initials import InitModels
from django.conf import settings
from django.db import models
from products.database.products import Products


class Cart(InitModels):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    total = models.PositiveIntegerField()
    complete = models.BooleanField(default=False)

class CartProduct(InitModels):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ManyToManyField(Products)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Cart=={self.cart.id}<==>CartProduct:{self.id}==Qualtity=={self.quantity}"


ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)







'''
Cart & Order Management
    - Order models
    - Cart models
    - Cart Item models
'''


## Order Item Models 
class OrderItem(InitModels):
    # customer = models.ForeignKey('accounts.Profile',on_delete=models.CASCADE,
    #     null=True,verbose_name="Customer Name",related_name="order_items")
    item = models.ForeignKey('products.Products',on_delete=models.SET_NULL,
        null=True,verbose_name="Products",related_name="items")
    quantity = models.IntegerField(null=True,verbose_name="Quantity")
    attr = models.CharField(max_length=300,null=True,blank=True,verbose_name="Attribute")
    is_order = models.BooleanField(default=False) 
    amount_item = models.PositiveIntegerField(null=True)

    


    def __str__(self):
        return f"Item : {self.item} === Quantitiy  \
                : {self.quantity} === Status : {'Paid' if self.is_order == True else 'Not paid'}"

    class Meta:
        verbose_name_plural =  "Order Item"
    

class Order(InitModels):
    # cart  = models.OneToOneField(Cart,on_delete=models.CASCADE)
    customer = models.ForeignKey('accounts.Profile',on_delete=models.SET_NULL,null=True,
        verbose_name="Customer")
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    # mobile = models.CharField(max_length=16)
    # email = models.CharField(max_length=200)
    address = models.ForeignKey('accounts.BillingAddress',on_delete=models.SET_NULL,
        null=True,blank=True)
    coupon = models.ForeignKey('orders.Coupon',blank=True,null=True,
        on_delete=models.SET_NULL)
    ordered_date = models.DateTimeField(null=True)
    items = models.ManyToManyField(OrderItem)
    total = models.PositiveIntegerField()
    # discount = models.PositiveIntegerField()

    order_status = models.CharField(max_length=100,choices=ORDER_STATUS,
        default="Order Received")

    payment_complete = models.BooleanField(default=False)
    is_order = models.BooleanField(default=False,null=True)

    def __str__(self):
        return str(self.customer)

    class Meta:
        verbose_name_plural = 'Customer Order'


