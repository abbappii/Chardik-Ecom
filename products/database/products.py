from django.db import models
from products.database.init import *
from django.utils.translation import gettext_lazy as _


'''
Products 
attribute 
'''

#Product Attribute model
class ProductAttribute(models.Model):
    name = models.CharField(max_length=255,unique=False)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

  
#Product Model
class Products(models.Model):
    brand = models.ForeignKey(
        Brand, 
        on_delete=models.CASCADE,
        related_name= 'brand'
        )
    country = models.ForeignKey(
        Countreies,
        on_delete=models.CASCADE
        )
    
    category = models.ManyToManyField(Categories)
    sub_category = models.ManyToManyField(Sub_Categories)

    name = models.CharField(
        max_length=50, 
        null=True, 
        blank=True
        )
    slug = models.SlugField(
        max_length=250, 
        null=False, blank=False, unique=True)
    meta = models.TextField(
        max_length=500, 
        null=True, 
        blank=True
        )
    descriptions = models.TextField(
        max_length=500, 
        null=True, 
        blank=True
        )
    alter_text = models.CharField(
        max_length=100, 
        null=True, 
        blank=True
        )
    sku = models.CharField(
        max_length=20,
        unique=True
        )
    upc = models.CharField(
        max_length=12,
        unique=True
        )
    feature_image=models.ImageField(upload_to='products')
    regular_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
        )
    new_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
        )
    inventory = models.IntegerField(default=0)
    is_stock = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.name


class Product_images(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_image')
    image=models.ImageField(upload_to='product_image_gallery', blank=True)
    
    class Meta:
        verbose_name = _("product image")
        verbose_name_plural = _("product images")
      