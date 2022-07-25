
'''

this file contains of 
            - bank accounts
            - deposi withdraw
            - expence
            - name
            - outlet 
                -models

'''

from django.db import models
from accounts.models.initials import InitModels

# Bank Accounts model  
class BankAccounts(InitModels):
    bank_name = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=20,decimal_places=2, default=0.00)

    def __str__(self):
        return self.bank_name
    
    class Meta:
        verbose_name_plural = 'BankAccounts'


# deposit withdraw model 
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
    amount = models.DecimalField(max_digits=20,decimal_places=2, default=0.00)

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
    date_field = models.CharField(max_length=255,null=True, blank=True)

    def __unicode__(self):
        return self.account

    class Meta:
        verbose_name_plural = 'Deposit Withdraws'




# name model 
class Name(InitModels):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Names'


# outlet model 
class Outlet(InitModels):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Outlets'


# expence model 

choice_type = (
    ('One Time','One Time'),
    ('Repeated','Repeated'),
)

class Expenses(InitModels):
    name = models.ForeignKey(
        Name,
        on_delete=models.CASCADE,
        related_name='Expence_name'
        )  
    outlet = models.ForeignKey( Outlet, on_delete=models.CASCADE, 
        related_name='outlet_name'
        )
    reference = models.CharField( max_length=255,null=True,  blank=True)

    date = models.CharField(max_length=255,null=True, blank=True)
    
    account = models.ForeignKey(BankAccounts, on_delete=models.CASCADE, 
        related_name='Bank_account'
        )
    expence_amount = models.DecimalField(max_digits=20,decimal_places=2, default=0.00)
    
    type = models.CharField(max_length=200, 
        choices=choice_type)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Expences'
