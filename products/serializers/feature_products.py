
from rest_framework import serializers
from products.database.feature_product import Banner, BannerProduct

from products.serializers.product_serializers import (
    ProductListAPI
)
'''
feature product 
        - create 
        - update 
'''
class BannerProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = BannerProduct
        fields = ['id','feature_product','banner']


'''
feature product 
        - list
'''
class BannerProductListSerializers(serializers.ModelSerializer):
    feature_product = ProductListAPI(read_only=True)
    class Meta:
        model = BannerProduct
        fields = ['id','feature_product','banner','is_active']
        depth = 1


'''
product filter 
'''
# product filter model 
class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id','name','banner_image']
