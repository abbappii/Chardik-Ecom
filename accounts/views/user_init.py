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

from MainApplication.scripts.phone_verification import SMS_of_Phone_Verification

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
                return Response({'Error':'Sorry Password mismatch'},status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response({'Error':'No such User Found'},status=status.HTTP_204_NO_CONTENT)


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
                return Response({'Success':'Profile is created'},
                status=status.HTTP_201_CREATED)
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
                profile_ID=user.profile.id
                SMS_of_Phone_Verification(get_phone_or_email,profile_ID).start()
                getProfile = Profile.objects.get(id=profile_ID)
                getProfile.is_active = False
                getProfile.save()
                return Response({'Success':'Profile is created','profile_ID':profile_ID},
                status=status.HTTP_201_CREATED)
            else:
                return Response(apifetch.errors)

            
## Send SMS 
class SendSMS(GenericAPIView):

    def get(self,request):
        phone = "01406616646"
        number = f"88{phone}"
        profile_ID = 1
        SMS_of_Phone_Verification(number,profile_ID).start()
        return Response({'Success':'Send'})

            
## Verfify OTP through phone
class VerifyOTP(GenericAPIView):
    def post(self,request):
        get_profile_ID = request.data.get('profile_ID')
        profile = Profile.objects.get(id=get_profile_ID)
        get_otp = request.data.get('otp')
        if profile.phone_otp == get_otp :
            profile.is_phone_verified = True
            profile.is_active = True
            profile.save()
            return Response({"Success":"OTP Matched"},status=status.HTTP_200_OK)
        else:
            return Response({'Error':'OTP did not Match'},status=status.HTTP_406_NOT_ACCEPTABLE)
            

## Forget Password option with Phone 

class ForgetPassword__with__Phone(GenericAPIView):
    def get(self,request):
        get_number = request.data.get('phone')
        if Profile.objects.filter(phone=get_number):
            getProfile_ID = Profile.objects.filter(phone=get_number).first().id
            # print(getProfile_ID)
            SMS_of_Phone_Verification(get_number,getProfile_ID).start()
            
            return Response({
                'OK':'Number Is Found',
                'profile_ID':getProfile_ID
            },status=status.HTTP_200_OK)
        else:
            return Response({
                'Error':'Number Didnt Found'
            },status=status.HTTP_204_NO_CONTENT)
    
    def post(self,request):
        get_profile_ID = request.data.get('profile_ID')
        profile = Profile.objects.get(id=get_profile_ID)
        get_otp = request.data.get('otp')
        if profile.phone_otp == get_otp :
            # profile.is_phone_verified = True
            # profile.is_active = True
            # profile.save()
            return Response({"Success":"OTP Matched"},status=status.HTTP_200_OK)
        else:
            return Response({'Error':'OTP did not Match'},status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def put(self,request):
        get_profileID = request.data.get('profile_ID')
        if User.objects.filter(profile=get_profileID).first():
            get_password = request.data.get('password1')
            get_confirm_password = request.data.get('password2')
            getUser = User.objects.get(profile=get_profileID)
            getUser.password = make_password(get_password)
            getUser.confirm_password = make_password(get_confirm_password)
            getUser.save()
            return Response({
                'Success':'Password Updated !'
            },status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response({
                'Error':'Profile Didn`t Match'
            },status=status.HTTP_204_NO_CONTENT)

        