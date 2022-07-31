from operator import imod
from django.db import models
from accounts.models import InitModels

class Feature_product(InitModels):

    feature_product = models.ForeignKey(
        'products.Products',
        on_delete=models.CASCADE,
        related_name = 'feature_product'
        )		
    
    def __unicode__(self):
        return self.feature_product.product_name

    class Meta:
        verbose_name_plural = 'Feature Products'
