from rest_framework import serializers


from accounts.models.user_model import User
from accounts.models.profile import Profile




'''
Registration
Login
Profile
'''

# #user Registration Serializer
# class UserRegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(style={'input_type': 'password'})
#     confirm_password = serializers.CharField(style={'input_type': 'password'})
#     class Meta:
#         model = User
#         fields = ['email', 'password','confirm_password']
#         extra_kwargs={'password' :{'write_only':True}}

#     def validate(self, attrs):
#         password = attrs.get('password')
#         confirm_password = attrs.get('confirm_password')
#         if password != confirm_password :
#             raise ValueError("Password and Confirm Password doesn't match !!!! ")
#         return attrs

    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)


# #user Login Serializer
# class LoginSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField()
#     class Meta:
#         model = User
#         fields = ['email','password']

# login serializers
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'})
    class Meta:
        model = User
        fields = ['username','password']


#user Profile Serializer
class UserProfileSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # fields = '__all__'
        fields= ['id', 'full_name','dob','gender','bio','profile_picture','address','city','zipcode','country',
        'phone']

# User Profile list serializers 
class UserProfileListSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # fields= ['id', 'user','full_name', 'phone']
        fields = "__all__"
        depth = 1



# User passwordchange Serializer 
class UserChangePasswordSerializer(serializers.Serializer):
  password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  confirm_password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  class Meta:
    fields = ['password', 'confirm_password']

  def validate(self, attrs):
    password = attrs.get('password')
    confirm_password = attrs.get('confirm_password')
    user = self.context.get('user')
    if password != confirm_password:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    user.set_password(password)
    user.save()
    return attrs
    