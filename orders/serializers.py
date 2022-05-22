'''
THis file contains the serializers of 
    - orders
    - coupon 
'''
from rest_framework import serializers

# imporing models 
from orders.database.order import Coupon


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