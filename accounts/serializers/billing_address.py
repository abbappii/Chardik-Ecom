from rest_framework import serializers
from accounts.models.profile import BillingAddress




'''
Region, city , area, Post code ,Address(ekhane details address hobe)

only region , city, address (required)
'''

''' Billing Address Serializers '''

class Billing_Address_Serialiazer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = [
            'id',
            'name',
            'email',
            'phone',
            'region',
            'city',
            'area',
            'post_code',
            'address',
            'is_biling'
        ]


''' Shipping Address Serializers '''

# class Shipping_Address_Serialiazer(serializers.ModelSerializer):
#     class Meta:
#         model = ShippingAddress
#         fields = [
#             'id',
#             'name',
#             'email',
#             'phone',
#             'region',
#             'city',
#             'area',
#             'post_code',
#             'address'
#         ]


   