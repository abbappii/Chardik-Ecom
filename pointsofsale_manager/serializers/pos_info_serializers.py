
from pointsofsale_manager.models import PointsOfSale
from orders.database.cart_order import (
    Order
)

from rest_framework import serializers


class PointsOfSaleSerializers(serializers.ModelSerializer):
    class Meta:
        model = PointsOfSale
        fields = ['id','outlet','user']



### Order API for Point of Sale

class OrderAPI_POS(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','customer',
                'ref_code','address_shipping','address_billing','coupon',
                'ordered_date','items',
                'shipping_fee','discount_price',
                'subtotal',
                'order_from',
                'total','order_status','is_order','delivery_option',
                'mobile','email','fast_delivery'
                ]
