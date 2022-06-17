'''
This file contains  
    - product API
'''

from rest_framework import serializers

# importing models
from products.database.products import(
    Products,ProductAttribute
)


## Products API

# class ProductAPI(serializers.ModelSerializer):
