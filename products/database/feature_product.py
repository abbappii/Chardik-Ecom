
# table for feature products and product filter 
from django.db import models
from accounts.models import InitModels

# product filter model 
class Banner(InitModels):
    name = models.CharField(max_length=255, unique=True)
    banner_image = models.ImageField(upload_to = 'product_filter_image')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Product By Query'

# feature product model 
class BannerProduct(InitModels):

    banner = models.ForeignKey(
        Banner,
        on_delete=models.SET_NULL,
        null=True, 
        related_name="banner"
        )

    feature_product = models.ForeignKey(
        'products.Products',
        on_delete=models.CASCADE,
        related_name = 'feature_product'
        )		
    
    def __unicode__(self):
        return self.feature_product.name

    class Meta:
        verbose_name_plural = 'Feature Products'
