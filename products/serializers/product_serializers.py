'''
This file contains  
    - product API
'''

from rest_framework import serializers

# importing models
from products.database.products import(
    Products,ProductAttribute,Product_images
)


## Products API

# class ProductAPI(serializers.ModelSerializer):


'''
product images
Products 
Attribute
'''

class Product_imagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product_images
        fields = ('image', )


class ProductsSerializers(serializers.ModelSerializer):
    product_image = Product_imagesSerializer(many=True, read_only=True)
    class Meta:
        model= Products
        fields = "__all__"
