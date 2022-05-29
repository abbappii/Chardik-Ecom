from rest_framework.views import APIView
from accounts.serializers.user_auth import (UserProfileSeriliazer, 
UserRegistrationSerializer,LoginSerializer)

from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken



#get manually token from simple jwt
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# User Registration view
class UserRegisterView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            token = get_tokens_for_user(user)
            return Response({'message':'Signup Successful', 'token':token}, status=status.HTTP_201_CREATED)
        return Response({'message':'Signup Failed'}, status=status.HTTP_400_BAD_REQUEST)


#User Login View
class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'massage':'Login Successful','token':token}, status=status.HTTP_200_OK)
            return Response({'massage':'User not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#User Profile View
class UserProfileView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSeriliazer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)