

from django.db import models
from accounts.models.initials import InitModels

class Discounts_product(InitModels):
    discount_product = models.ForeignKey(
        'products.Products', 
        on_delete=models.CASCADE, 
        related_name = "discount_product"
        )
    discount = models.PositiveIntegerField(
        null=True,blank=True,verbose_name="Flash Discount Percantage"
    )
    price = models.FloatField(null=True,blank=True)

    def __str__(self):
        return f"Product : {self.discount_product}"

    class Meta:
        verbose_name_plural = "Discount Products Add"