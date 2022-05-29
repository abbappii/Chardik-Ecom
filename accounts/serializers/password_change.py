from rest_framework import serializers
from accounts.models.user_model import User
from django.utils.encoding import force_bytes, smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import  PasswordResetTokenGenerator
from xml.dom import ValidationErr
from django.forms import ValidationError
from MainApplication.utils import Util


'''
User Password Change
User Password rest 
User Password Reset Link to email 
'''


# User Password Change
class UserPasswordChangedSerializer(serializers.Serializer):
    password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        fields = ['password','confirm_password']

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        user=self.context.get('user')
        if password != confirm_password:
            raise ValueError("Password Doesn't match")
        user.set_password(password)
        user.save()
        return attrs




# User Password email link create
class UserPasswordRestEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    class Meta:
        fields=['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print("UID : " + uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print("Token : " + token)
            link = 'http://localhost:3000/accounts/reset/'+uid +'/'+token
            print('Reset Link : ' + link)
            body = "Click the link and Reset your password" + link
            data={
                'subject':'Reset Your Password',
                'body': body,
                'to_email':user.email 
            }
            Util.sent_email(data)
        else:
            raise ValidationErr('You are not registerd User')
        return super().validate(attrs)





# User password click link to send vai email
class UserPasswordEmailLinkResetSerializer(serializers.Serializer):
    password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        fields = ['password','confirm_password']
    
    def validate(self, attrs):
        try:
            password = attrs.get('password')
            confirm_password = attrs.get('password')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password != confirm_password:
                raise ValidationError("Password Doesn't match. Please give same password")
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if not  PasswordResetTokenGenerator().check_token(user,token):
                raise ValidationError("Token Expired. Send again Password reset link from website")
            user.set_password(password)
            user.save()

            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user,token)
            raise ValidationError("Token Expired. Send again Password reset link from website")
