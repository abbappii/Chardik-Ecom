'''
THis file contains the serializers of 
    - orders
    - coupon 
'''
from rest_framework import serializers
# from orders.database.cart import Cart

# imporing models 
from orders.database.coupon import Coupon
from orders.database.cart_order import (
    Cart, 
    CartProduct,
    Order,
    OrderItem
)
'''
Coupon API serializers 
'''
class CouponAPI(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = [
            'id','coupon_name','coupon_type',
            'coupon_amount','free_shipping',
            'expire_date','minimum_user',
            'minimum_sale','maximum_sale'
        ]


''' 
Cart Api serializers
'''
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
        depth = 1

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = "__all__"
        depth = 1


'''
Order api serializers 
    -list view
'''
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        depth = 2


'''
Order API 
    order Item
    Order
'''

# Item API
class OrderItemAPI(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id','item',
                'quantity','attr',
                'is_order','amount_item'
                ]


## Order API 
    # -create v
    # -update v
    
class OrderAPI(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id',
                'ref_code','address_shipping','address_billing','coupon',
                'ordered_date','items',
                'total','order_status','is_order',
                'mobile','email','fast_delivery'
                ]
