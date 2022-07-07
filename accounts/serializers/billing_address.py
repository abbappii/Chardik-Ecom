from rest_framework import serializers
from accounts.models.profile import BillingAddress





''' Billing Address Serializers '''

class Billing_Address_Serialiazer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = ['billing_address']





   