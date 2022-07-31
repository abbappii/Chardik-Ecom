
from rest_framework import serializers
from products.database.feature_product import Feature_product

from products.serializers.product_serializers import (
    ProductListAPI
)
# create, update 
class FeatureProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feature_product
        fields = ['id','feature_product']


# list
class FeatureProductListSerializers(serializers.ModelSerializer):
    feature_product = ProductListAPI(read_only=True)
    class Meta:
        model = Feature_product
        fields = ['id','feature_product','is_active']
