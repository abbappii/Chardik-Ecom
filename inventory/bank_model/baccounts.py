
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


choice_field = (
    ('Deposit', 'Deposit'),
    ('Withdraw', 'Withdraw'),
)

class DepositWithdraw(InitModels):

    account = models.ForeignKey(
        'inventory.BankAccounts', 
        on_delete=models.CASCADE, 
        related_name='account',
        verbose_name='Bank Account'
        )
    Reference = models.CharField(
        max_length=255,
        null=True, 
        blank=True
        )
    created_by = models.CharField(
        max_length=255,
        null=True, 
        blank=True
        )
    transfer_type = models.CharField( 
        max_length=200, 
        choices=choice_field
        )
    note =  models.TextField(
        max_length=1000, 
        blank=True
        )

    def __unicode__(self):
        return self.account

    class Meta:
        verbose_name_plural = 'Deposit Withdraws'

