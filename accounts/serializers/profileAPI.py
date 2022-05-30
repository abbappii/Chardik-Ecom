
from rest_framework import serializers

# importing models
from accounts.models.profile import Profile

# User profile API

class UserProfileSeriliazers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields= ['id', 'full_name','address','city','zipcode','country',
        'phone']


# Give Permission API

class GivePermissionAPI(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','full_name','permission']


# Permission List API

class GivePermissionViewAPI(serializers.ModelSerializer):
    permission = serializers.CharField(source = 'get_permission',read_only=True)
    class Meta:
        model = Profile
        fields = ['id','full_name','permission']