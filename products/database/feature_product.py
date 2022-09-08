
# table for feature products and product filter 
from django.db import models
from accounts.models import InitModels

# product filter model 
class Banner(InitModels):
    name = models.CharField(max_length=255, unique=True)

    title = models.CharField(
        max_length=180, 
        verbose_name="Banner Title",
        null = True
        )
    banner_image = models.ImageField(upload_to = 'product_filter_image')

    products = models.ManyToManyField(
        'products.Products', related_name='banner_products',
        through='BannerProduct')
    is_slider = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Banners'

    ## Customer Property 
    @property
    def banner_products(self):
        products = [product.id for product in self.products.all()]    
        return products

## Through models for products 
'''
THis model is an auxilary model for Flash Sale
'''
class BannerProduct(InitModels):

    banner = models.ForeignKey(
        Banner,
        on_delete=models.SET_NULL,
        null=True, 
        related_name="banner"
        )

    banner_product = models.ForeignKey(
        'products.Products',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Select Product",
        related_name='banner_product')		
    

    def __str__(self):
        return f"Product : {self.banner_product}"

    class Meta:
        verbose_name_plural = 'Banner Products Add'
