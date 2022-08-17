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
    coupon_name = serializers.SlugField()
    class Meta:
        model = Coupon
        fields = [
            'id','coupon_name','coupon_type',
            'coupon_amount','free_shipping',
            'expire_date','maximum_user',
            'minimum_sale','maximum_sale',
            'category','brand','product','coupon_count'
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
        # fields = ['id']
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
        depth = 1


## Order API 
    # -create v
    # -update v
    
class OrderAPI(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id',
                'ref_code','address_shipping','address_billing','coupon',
                'ordered_date','items',
                'shipping_fee','discount_price',
                'subtotal',
                'order_from',
                'total','order_status','is_order','delivery_option',
                'mobile','email','created_at',
                'payment_complete','updated_at',
                'user_device','user_browser'
                ]



## View orders API

class OrderViewAPI(serializers.ModelSerializer):

    items = OrderItemAPI(many=True,read_only=True)

    class Meta:
        model = Order
        fields = ['id',
                'ref_code','address_shipping','address_billing','coupon',
                'ordered_date','items',
                'total','order_status','is_order','delivery_option',
                'mobile','email','created_at','payment_complete','updated_at',
                'user_device','user_browser'
                ]



'''
Order api serializers 
    -customer orders list view (admin)
'''

class CustomerOrdersViewAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
