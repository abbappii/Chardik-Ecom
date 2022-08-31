
'''
this file contains 
        - Discount products form 
'''

from rest_framework import serializers
from products.database.discount_products import Discounts_product

from products.serializers.product_serializers import (
    ProductListAPI
)

'''
Api
    create, update, delete
'''
class DiscountProductsSerailzers(serializers.ModelSerializer):
    class Meta:
        model = Discounts_product
        fields = [
            'id',
            'discount_product',
            'discount',
        ]


'''
Api 
    list, retrive

'''
class DiscountProductsListAPI(serializers.ModelSerializer):
    discount_product = ProductListAPI(read_only=True)

    class Meta:
        model = Discounts_product
        fields = [
            'id',
            'discount_product',
            'discount',
            'price',
            'created_at',
            'updated_at',
        ]