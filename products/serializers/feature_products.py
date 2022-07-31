
from rest_framework import serializers
from products.database.feature_product import Feature_product, Product_filter

from products.serializers.product_serializers import (
    ProductListAPI
)
'''
feature product 
        - create 
        - update 
'''
class FeatureProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feature_product
        fields = ['id','feature_product','product_by_query']


'''
feature product 
        - list
'''
class FeatureProductListSerializers(serializers.ModelSerializer):
    feature_product = ProductListAPI(read_only=True)
    class Meta:
        model = Feature_product
        fields = ['id','feature_product','product_by_query','is_active']
        depth = 1


'''
product filter 
'''
# product filter model 
class ProductFilterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product_filter
        fields = ['id','name','banner_image']
