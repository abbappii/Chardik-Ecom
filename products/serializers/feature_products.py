
from rest_framework import serializers
from products.database.feature_product import Banner, BannerProduct

from products.serializers.product_serializers import (
    ProductListAPI
)
# '''
# feature product 
#         - create 
#         - update 
# '''
class Banner_Product_API(serializers.ModelSerializer):
    class Meta:
        model = BannerProduct
        fields = [
            'id',
            'banner_product',
            'banner'
        ]


# '''
# feature product nested purpose
#         
# '''
class BannerProduct_API_show(serializers.ModelSerializer):

    banner_product = ProductListAPI(read_only=True)

    class Meta:
        model = BannerProduct
        fields = [
            'id',
            'banner_product',
            'is_active'
        ]
        

class Banner_API(serializers.ModelSerializer):
    banner_ID = serializers.ReadOnlyField(source = 'id')
    products = serializers.SerializerMethodField()

    class Meta:
        model = Banner
        fields = [ 
            'id',
            'banner_ID',
            'name',
            'banner_image',
            'products'
        ]
    
    # custom method to return the list of banner products 
    def get_products(self,obj):
        products_qset = BannerProduct.objects.filter(banner=obj)
        return [BannerProduct_API_show(m).data for m in products_qset]

'''
Banner API 
        - create, 
        - update, 
        - delete 
'''

class Banner_API_func(serializers.ModelSerializer):
    
    class Meta:
        model = Banner
        fields = [
            'id',
            'name',
            'banner_image',
        ]