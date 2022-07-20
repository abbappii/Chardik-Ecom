

from rest_framework import serializers
from inventory.bank_model.baccounts import BankAccounts

class BankAccountsSerializers(serializers.ModelSerializer):
    class Meta:
        model = BankAccounts
        fields = ['id','bank_name','amount']