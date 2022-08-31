
from django.db import models
from accounts.models.initials import InitModels


# Product Reviews
class ProductReview(InitModels):
    profile = models.ForeignKey('accounts.Profile',on_delete=models.SET_NULL,null=True,
        verbose_name='Profile Name')
    product = models.ForeignKey('products.Products',on_delete=models.CASCADE,
        null=True,related_name='reviews')
    star_count = models.IntegerField(null=True)
    review = models.TextField(null=True,blank=True)

    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return self.review

    class Meta:
        verbose_name_plural = "Product Review"