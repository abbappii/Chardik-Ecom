from rest_framework import serializers


from accounts.models.user_model import User
from accounts.models.profile import Profile




'''
Registration
Login
Profile
'''

#user Registration Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ['email', 'password','confirm_password']
        extra_kwargs={'password' :{'write_only':True}}

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password :
            raise ValueError("Password and Confirm Password doesn't match !!!! ")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


#user Login Serializer
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ['email','password']


#user Profile Serializer
class UserProfileSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields= ['id', 'full_name','address','city','zipcode','country',
        'phone','date_joined']