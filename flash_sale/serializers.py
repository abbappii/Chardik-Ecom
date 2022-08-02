'''
THis file contain the API 
'''

# importing initials 
from rest_framework import serializers

# importng models
from flash_sale.models import (
    FlashSale,
    FlashProducts
)

from products.serializers.product_serializers import (
    ProductListAPI
)



'''
Flash Sale Products API
    - List, view API
    - Action (update,create,delete) API
'''
## flash Sale Products API

class FlashSale_ProductAPI(serializers.ModelSerializer):

    
    class Meta:
        model = FlashProducts
        fields = [
            'id',
            'flash_sale',
            'flash_product',
            # 'flash_price',
            # 'is_active'
            ]

## Auxilary API for nested perpose 

class FlashSale_ProductAPI_show(serializers.ModelSerializer):

    flash_product = ProductListAPI(read_only=True)

    class Meta:
        model = FlashProducts
        fields = [
            'id',
            'flash_product',
            'flash_price',
            'is_active'
            ]


'''
Flash Sale API 
    - List, view API
    - Action (update,create,delete) API
'''

## Flash Sale API (View , List)

class FlashSale_API(serializers.ModelSerializer):

    flash_sale_ID = serializers.ReadOnlyField(source = 'id')
    products = serializers.SerializerMethodField()

    class Meta:
        model = FlashSale
        fields = [
            'id',
            'flash_sale_ID',
            'name',
            'discount',
            'start_time',
            'end_time',
            'products'
        ]

    # depth = 2
    
    ## Custom method to return the list of flash products
    def get_products(self,obj):
        products_qset = FlashProducts.objects.filter(flash_sale=obj)
        return [FlashSale_ProductAPI_show(m).data for m in products_qset]

        

# Flash Sale API (Create , Update , Delete)

class FlashSale_API_func(serializers.ModelSerializer):
    
    class Meta:
        model = FlashSale
        fields = [
            'id',
            'name',
            'discount',
            'start_time',
            'end_time',
        ]