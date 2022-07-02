
from rest_framework import serializers
from accounts.models.profile import Profile


# posManager serializer 
class UserOfflineProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'full_name','address','city','zipcode','country',
        'phone']