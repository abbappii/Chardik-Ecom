
from django.db import models

from django.utils.translation import gettext_lazy as _

from accounts.models.initials import InitModels


'''
Products 
attribute 
'''

#Product Attribute model
class ProductAttribute(InitModels):
    name = models.CharField(max_length=255,unique=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    # custom Property 
    def all_products(self):
        return [products for products in self.Category_products.all()]

    class Meta:
        verbose_name_plural = "Product Attribute"

  
#Product Model
class Products(InitModels):
    brand = models.ForeignKey(
        'products.Brand', 
        on_delete=models.CASCADE,
        related_name= 'brand'
        )
    country = models.ForeignKey(
        'products.Countreies',
        on_delete=models.CASCADE, related_name='country'
        )
    
    category = models.ManyToManyField('products.Categories',
        related_name='Category_products')
    sub_category = models.ManyToManyField('products.Sub_Categories',
        related_name='Sub_category_products')

    product_name = models.CharField(
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
    short_descriptions = models.CharField(
        max_length=1200, 
        null=True, 
        blank=True,
        verbose_name='Short Description'
        )
    long_description = models.TextField(
        null=True, 
        blank=True,
        verbose_name='Long Description'
        )
    alter_text = models.CharField(
        max_length=400, 
        null=True, 
        blank=True
        )
    sku = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='SKU'
        )
    upc = models.CharField(
        max_length=12,
        unique=True,
        verbose_name='UPC'
        )
    feature_image=models.ImageField(upload_to='products',null=True)
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

    inventory = models.IntegerField(default=0,null=True,verbose_name="Inventory")
    is_stock = models.BooleanField(default=True,verbose_name="Is Stock")


    def __str__(self) -> str:
        return self.product_name

    class Meta:
        verbose_name_plural = "Product"


    # Custom Property 

    @property
    def get_category(self):
        category = [category.category_name for category in self.category.all()]
        return category
    

    @property
    def get_sub_category(self):
        sub_category = [ sub_category.sub_category_name for  sub_category in \
             self.sub_category.all()]
        return sub_category


# product images 
class Product_images(InitModels):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, 
        related_name='product_image')
    image=models.ImageField(upload_to='product_image_gallery', blank=True)
    
    class Meta:
        verbose_name_plural = _("product images")

    class Meta:
        verbose_name_plural = "Product Image"


# Product Reviews
class ProductReview(InitModels):
    profile = models.ForeignKey('accounts.Profile',on_delete=models.SET_NULL,null=True,
        verbose_name='Profile Name')
    product = models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    star_count = models.IntegerField(null=True)
    review = models.TextField(null=True,blank=True)


    def __str__(self):
        return self.review

    class Meta:
        verbose_name_plural = "Product Review"