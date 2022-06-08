'''
This file contains followings
    - User context
    - login view 
    - register view 
    - profile view

'''


from rest_framework.generics import GenericAPIView
from django.db.models import Q
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from django.contrib.auth.hashers import make_password

# importing API
from accounts.serializers.user_auth import LoginSerializer
from accounts.serializers.profileAPI import (
    UserProfileSeriliazers
)

# importing models 
from accounts.models.user_model import User
from accounts.models.profile import Profile

from rest_framework.views import APIView
from MainApplication.scripts.permission import IsCustomer
from accounts.serializers.user_auth import UserProfileSeriliazer            


# Login view 
class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        # getting the data from frontend 
        get_name = request.data.get('username',None)
        password = request.data.get('password',None)

        # matching the data 
        match_data = User.objects.filter(
            Q(username = get_name)|
            Q(email = get_name)|
            Q(profile__phone= get_name)|
            Q(profile__customer_ID = get_name)

        ).first()

        if match_data:
            user = authenticate(username = match_data.username, password= password)

            if user:
                return Response({
                    'username':user.username,
                    'user_obj_ID':user.id,
                    'profile_ID':user.profile.id,
                    'fullName':user.profile.full_name
                })
            else:
                return Response({'Error':'Sorry Password mismatch'})
        else:
            return Response({'Error':'Sorry, Credentials Not match!'})


# User Profile view 

class UserProfileView(APIView):
    permission_classes=[IsCustomer]

    def get(self, request):
        serializer = UserProfileSeriliazer(request.user.profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


## User Register View 

class RegisterView(GenericAPIView):
    serializer_class = UserProfileSeriliazers
    queryset = Profile.objects.all()

    def post(self,request):
        # data getting from Frontend
        password = request.data.get('password') 
        get_phone_or_email = request.data.get('phone')


        # Code run if User submit EMAIL
        if '@' in get_phone_or_email:

            apifetch = UserProfileSeriliazers(data=request.data)
            if apifetch.is_valid():

                '''
                Apifetch will check 
                    - Unique Email 
                    - Password will be taken automatically
                    - validated user will be saved
                '''

                # Unique Email Check 
                if User.objects.filter(email=apifetch.validated_data['phone']):
                    return Response({'Error':'Email Already in Used'},
                    status= status.HTTP_406_NOT_ACCEPTABLE)
                else:
                     authInfo = {
                    'email':apifetch.validated_data['phone'],
                    'password':make_password(password),
                    'confirm_password':make_password(password)
                    }
                     user = User(**authInfo)
                     user.save()
                apifetch.validated_data['user'] = user
                apifetch.validated_data['phone'] = ''          
                apifetch.save()
                return Response({'Success':'Profile is created'})
            else:
                return Response(apifetch.errors)
        
        # Code run if user submit PHONE
        else:
            apifetch = UserProfileSeriliazers(data=request.data)
            if apifetch.is_valid():
                '''
                Apifetch will check 
                    - Phone 
                    - Password will be taken automatically
                    - validated user will be saved
                '''

                # Unique Phone Number Check 
                if Profile.objects.filter(phone=apifetch.validated_data['phone']):
                    return Response({'Error':'Phone Number Already in Used'},
                    status= status.HTTP_406_NOT_ACCEPTABLE)
                else:
                     authInfo = {
                    'password':make_password(password),
                    'confirm_password':make_password(password)
                    }
                     user = User(**authInfo)
                     user.save()
                apifetch.validated_data['user'] = user
                apifetch.save()
                return Response({'Success':'Profile is created'})
            else:
                return Response(apifetch.errors)

            
        
            
            


