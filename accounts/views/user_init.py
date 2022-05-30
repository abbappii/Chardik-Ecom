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





# Register View 

class RegisterView(GenericAPIView):
    serializer_class = UserProfileSeriliazers
    queryset = Profile.objects.all()

    def post(self,request):
        data = request.data
        password1 = data.get('password')
        password2 = data.get('confirm_Password')
        email = data.get('email')

        # Password Checking 
        if password1 != password2:
            return Response({'Error':'Password Didn`t Match'},status=\
                    status.HTTP_406_NOT_ACCEPTABLE)
        # Email checking 
        elif User.objects.filter(email=email):
            return Response({'Error':'This email is associated with another account'},
                status = status.HTTP_406_NOT_ACCEPTABLE)
        else:
            authInfo = {
                'email':email,
                'password':make_password(password1),
                'confirm_password':make_password(password2)
            }
            user = User(**authInfo)
            user.save()
        
        # Profile Section of saving start
        add_user_to_profile = Profile(user=user)
        apifetch = UserProfileSeriliazers(add_user_to_profile,data=request.data)
        if apifetch.is_valid():
            if Profile.objects.filter(phone= apifetch.validated_data['phone']):
                return Response({'Error':'Phone Number Already in Used'},
                status= status.HTTP_406_NOT_ACCEPTABLE)
            else:
              
                apifetch.save()
                return Response({'Success':'Profile is created'})
        else:
            return Response({'Error':'No Validate data given'})

# User Profile view 

class UserProfileView(APIView):
    permission_classes=[IsCustomer]

    def get(self, request):
        serializer = UserProfileSeriliazer(request.user.profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
