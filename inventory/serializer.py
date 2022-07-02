

'''
this file contains Serializers 
        - Supplier Serializer
        - Purchase Serializer
'''

# import section 
from rest_framework import serializers
from inventory.models import (
    Supplier, Purchase
)


# serializer class 

# supplier serializer 
class SupplierSerializers(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id','name','description','country','phone','email','address']
    
# purchase serailizer 
class PurchaseSerialiers(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = [
            'id',
            'ref_code',
            'batch_no',
            'date_of_purchase',
            'order_status',
            'product',
            'price',
            'supplier',
            'outlet_name',
            'unit_cost',
            'other_cost',
            'due_price',
            'payment_method',
            'payment_status',
            'description'
        ]
        depth = 1