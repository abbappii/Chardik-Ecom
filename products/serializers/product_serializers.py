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


# class 

## Products API

# class ProductAPI(serializers.ModelSerializer):



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
        slug_field='product_name')
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


### Image Serializer 
class Product_imagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product_images
        fields = ('image', )


'''
Product API 
    - view 
    - delete
    - create
    - update
'''

class ProductListAPI(serializers.ModelSerializer):
    variant = VariationListAPI(many=True)
    product_image = Product_imagesSerializer(many=True)

    class Meta:
        model = Products
        fields = ['id','brand','country',
                    'category','sub_category','product_name',
                    'slug','meta','short_descriptions',
                    'long_description','alter_text',
                    'feature_image','sold_count','exprire_rate',
                    'is_stock']






'''
product images
Products 
Attribute
'''


class ProductsSerializers(serializers.ModelSerializer):
    product_image = Product_imagesSerializer(many=True, read_only=True)
    class Meta:
        model= Products
        fields = "__all__"
