

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
        'products.Products', related_name='flash_products',
        through='FlashProducts'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Flash Deal"

    ## Customer Property 
    @property
    def flash_products(self):
        products = [product.id for product in self.products.all()]    
        return products
    ## Override the Save method 
    # def save(self,*args,**kwargs):
    #     for product in self.products.all():
    #         print(product)
    #     super(FlashSale, self).save(*args, **kwargs) 

    

## Through models for products 

class FlashProducts(InitModels):
    flash_sale = models.ForeignKey(
        'flash_sale.FlashSale',on_delete=models.CASCADE,
        null=True,related_name="sale"
        )  
    flash_product = models.ForeignKey(
        'products.Products',on_delete=models.SET_NULL,
        null=True,verbose_name="Select Prodcut",related_name='flash_product'
        )
    flash_price = models.FloatField(null=True,blank=True)


    def __str__(self):
        return f"Product : {self.flash_product}, Price : {self.flash_price}"


    class Meta:
        verbose_name_plural = "Flash Products Add"
