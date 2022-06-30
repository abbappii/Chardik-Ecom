
from .models import OfflineSale
from rest_framework import serializers
from accounts.models.profile import Profile

class OfflineSaleSerializers(serializers.ModelSerializer):
    class Meta:
        model = OfflineSale
        fields = ['id','outlet','user','product','category','brand']


# posManager serializer 
class UserOfflineProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'full_name','address','city','zipcode','country',
        'phone']