

'''
This file contains the database of 
    Flash Sale
'''

from django.db import models
from accounts.models.initials import InitModels

class FlashSale(InitModels):
    name = models.CharField(
        max_length=500,null=True,verbose_name="Flash Sale Name",blank=True
        )
    discount = models.PositiveIntegerField(
        null=True,blank=True,verbose_name="Flash Discount"
    )
    start_time = models.DateTimeField(
        null=True,auto_created=False,verbose_name="Start Time"
        )
    end_time = models.DateTimeField(
        null=True,auto_created=False,verbose_name="End Time"
    )
    products = models.ManyToManyField(
        'products.Products', related_name='flash_products'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Flash Deal"