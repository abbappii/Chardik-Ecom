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


## flash Sale Products API

class FlashSale_ProductAPI(serializers.ModelSerializer):

    class Meta:
        model = FlashProducts
        fields = [
            'flash_sale',
            'flash_product',
            'flash_price',
            'is_active'
            ]


## Flash Sale API (View , List)

class FlashSale_API(serializers.ModelSerializer):

    products = FlashSale_ProductAPI(many=True)

    class Meta:
        model = FlashSale
        fields = [
            'name',
            'discount',
            'start_time',
            'end_time',
            'products'
        ]

# Flash Sale API (Create , Update , Delete)

class FlashSale_API(serializers.ModelSerializer):
    

    class Meta:
        model = FlashSale
        fields = [
            'name',
            'discount',
            'start_time',
            'end_time',
        ]