'''
file contains the API 
'''

from rest_framework import serializers

# models 
from revenue.models import (
    RevenueHistory
)
from products.database.products import (
    Products
)


## revenue API 

class RevenueAPI(serializers.ModelSerializer):
    
    product_name = serializers.SlugRelatedField(
        queryset=Products.objects.filter(is_active=True),
        slug_field='product_name'
    )

    class Meta:
        model = RevenueHistory
        fields = [
            'id',
            'purchase_code',
            'product_name',
            'purchase_unit',
            'selling_unit',
            'quantity',
            'profits'
        ]
    