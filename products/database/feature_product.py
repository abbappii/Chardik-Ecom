
# table for feature products and product filter 
from django.db import models
from accounts.models import InitModels

# product filter model 
class Product_filter(InitModels):
    name = models.CharField(max_length=255, unique=True)
    banner_image = models.ImageField(upload_to = 'product_filter_image')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Product By Query'

# feature product model 
class Feature_product(InitModels):

    product_by_query = models.ForeignKey(
        Product_filter,
        on_delete=models.SET_NULL,
        null=True, 
        related_name="product_query_select"
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
