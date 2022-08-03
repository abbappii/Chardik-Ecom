from accounts.models.initials import InitModels
from django.conf import settings
from django.db import models
from products.database.init_p import Brand, Categories
from products.database.products import Products

'''
Coupon Class 
    { Coupon usage 
        - fixed Card Discount
        - Parcentage Discount
    }
    models 
    property 
'''

coupon_choices = (
    ('Fixed Cart Discount','Fixed Cart Discount'),
    ('Parcentage Discount', 'Parcentage Discount')

)

class Coupon(InitModels):
    coupon_name = models.CharField(max_length=100,null=True,verbose_name=
        "Coupon Name",unique=True) 
    coupon_type = models.CharField(choices=coupon_choices,max_length=20,
        default=None,null=True,verbose_name="Coupon Type")
    coupon_amount = models.FloatField(null=True,default=0.00,
        verbose_name="Coupon Amount")
    free_shipping = models.BooleanField(default=False,null=True,
        verbose_name="Free Shipping Allow ?")
    expire_date = models.DateField(null=True,blank=True,auto_now_add=False)
    maximum_user = models.IntegerField(default=0,null=True,blank=True,verbose_name=
        "Maximum Users")
    minimum_sale = models.IntegerField(null=True,blank=True,verbose_name=
        "Minimum Sale")
    maximum_sale = models.IntegerField(null=True,blank=True,verbose_name=
        "Maximum Sale")

    # field added manytomany 
    category = models.ManyToManyField(Categories, blank=True)
    brand  = models.ManyToManyField(Brand, blank=True)
    product = models.ManyToManyField(Products, blank=True)

    def __str__(self):
        return str(self.coupon_name)

    class Meta:
        verbose_name_plural = "Coupon"
        app_label = "orders"

    


