'''
This file contains  
    - product API
'''

from rest_framework import serializers

# importing models
from products.database.products import(
    Products,ProductAttribute,Product_images,
    Variation_with_Price_variant
)
from products.database.init_p import(
   ColorVariation,WeightVariation,SizeVariation
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



'''
 Product Variation Serializer 
    - Create , edit, update 
    - list , single view 
'''

# Create , edit, update 
class VariationAPI(serializers.ModelSerializer):
    class Meta:
        model = Variation_with_Price_variant
        fields = ['id','product','size',
                'color','weight','regular_price',
                'selling_price']


# List , single view
class VariationListAPI(serializers.ModelSerializer):
    
    product = serializers.SlugRelatedField(queryset=Products.objects.all(),
        slug_field='name')
    size = serializers.SlugRelatedField(queryset=SizeVariation.objects.all(),
        slug_field='size_name')
    color = serializers.SlugRelatedField(queryset= ColorVariation.objects.all(),
        slug_field='color_name')
    weight = serializers.SlugRelatedField(queryset =WeightVariation.objects.all(),
        slug_field='weight_name')
    
    class Meta:
        model = Variation_with_Price_variant
        fields = ['id','product','size',
                'color','weight','regular_price',
                'selling_price']


