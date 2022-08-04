'''
The database models for generating revenue 

'''


from django.db import models
from accounts.models.initials import (
    InitModels
)


class RevenueHistory(InitModels):
    purchase_code  = models.CharField(
        max_length=500, null=True,verbose_name="Purchase Refer"
        )
    # product_name = models.CharField(
    #     max_length=500, null=True,verbose_name="Product Refer"
    #     )
    product_name = models.ForeignKey(
        'products.Products',on_delete=models.DO_NOTHING,null=True,
        verbose_name="Product Refer"
    )
    purchase_unit = models.FloatField(null=True)
    selling_unit = models.FloatField(null=True)
    quantity = models.PositiveIntegerField(default=1)
    profits = models.FloatField(null=True)

    def __str__(self):
        return str(self.purchase_code)

    class Meta:
        verbose_name_plural = "Revenue History"


    ## Custom Property 
