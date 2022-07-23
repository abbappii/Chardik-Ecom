
from inventory.bank_model.baccounts import Expenses

from rest_framework import serializers

class ExpenceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = ['id','name','outlet','reference','account','expence_amount','type','description']
    
 




