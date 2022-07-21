

from asyncore import read
from venv import create
from rest_framework import serializers
from inventory.bank_model.baccounts import BankAccounts, DepositWithdraw

class BankAccountsSerializers(serializers.ModelSerializer):
    class Meta:
        model = BankAccounts
        fields = ['id','bank_name','amount']


# Deposit withdraw serializers 
                    # - use create
class DepositWithdrawSerializers(serializers.ModelSerializer):
    class Meta:
        model = DepositWithdraw
        fields = ['id','Reference','account', 'created_by', 'transfer_type','note']