
'''

this file contains of bank accouts table

'''

from django.db import models
from accounts.models.initials import InitModels

class BankAccounts(InitModels):
    bank_name = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=20,decimal_places=2, default=0.00)

    def __str__(self):
        return self.bank_name
    
    class Meta:
        verbose_name_plural = 'BankAccounts'
