from django.db import models
from accounts.models.initials import InitModels
# Create your models here.

class PointsOfSale(InitModels):
    outlet = models.CharField(max_length=255,blank=True, null=True)
    user = models.ForeignKey('accounts.User',on_delete=models.CASCADE)

    def __str__(self):
        return self.outlet
    
    class Meta:
        verbose_name_plural = 'Points of Sale'
