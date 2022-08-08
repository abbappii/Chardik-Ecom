

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


class PurchaseCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = [
            'id',
            'ref_code',
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
            'description',
            'quantity'
        ]

    def update(self, instance, validated_data):


        instance.payment_status = validated_data.get('payment_status',instance.payment_status)
        instance.due_price = validated_data.get('due_price', instance.due_price)

        if instance.payment_status == 'Paid':
            instance.due_price = 0
            print('hudai')
            return instance
        else:
            return instance
'''
Define Supplier DUE Reports 
'''

class SupplierDueReportsAPI(serializers.ModelSerializer):
    supplier = serializers.SlugRelatedField(queryset= Supplier.objects.all(),\
        slug_field='name')
    class Meta:
        model = Purchase
        fields = [
            'id',
            'supplier',
            'due_price'
                ]
        # depth = 1