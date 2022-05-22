from rest_framework import serializers
from accounts.models.user_model import User


'''
Registration
Login
Profile
'''

#user Registration Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_pasworod = serializers.CharField(style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ['email', 'password','confirm_pasworod']
        extra_kwargs={'password' :{'write_only':True}}

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_pasworod = attrs.get('confirm_pasworod')
        if password != confirm_pasworod :
            raise ValueError("Password and Confirm Password doesn't match !!!! ")
        return attrs

    def create(self, validated_data):
        return User.objects._create_user(**validated_data)


#user Login Serializer
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ['email','password']


#user Profile Serializer
class UserProfileSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['id', 'username','full_name','address','city','zipcode','country','phone','date_joined']