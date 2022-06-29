from django.db import models

from accounts.models.initials import InitModels

# Create your models here.

# class OfflineSale(InitModels):


#     outlet = models.CharField(max_length=255, null= True, blank=True)
#     customer = models.ForeignKey('accounts.Profile', 
#             on_delete=models.CASCADE, 
#             related_name='customer_user'
#             )

#     product = models.ForeignKey('products.Products', 
#             on_delete=models.CASCADE, 
#             related_name='all_products'
#             )
#     category = models.ForeignKey('products.Categories', 
#             on_delete=models.CASCADE, 
#             related_name='all_categories'
#             )
#     brand = models.ForeignKey('products.Brand', 
#             on_delete=models.CASCADE, 
#             related_name='all_brands'
#             )
    

#     def __unicode__(self):
#         return self.product
    
#     class Meta:
#         verbose_name_plural = 'Offlie Sales'
