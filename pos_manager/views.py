
'''
this file contains pos logic
    - createview

'''
from accounts.models.profile import Profile
from .seriallizrers import UserOfflineProfileSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import  Response

from rest_framework import status
from rest_framework.decorators import permission_classes
from django.contrib.auth.hashers import make_password

from accounts.models.user_model import User

'''
Logic for offline(pos) profile create
'''

class OfflineProfileCreateView(GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserOfflineProfileSerializers

    def post(self,request):
        phone = request.data.get('phone')
        password = request.data.get('password') 

        apifetch = UserOfflineProfileSerializers(data=request.data)
        if apifetch.is_valid():
            if Profile.objects.filter(phone=apifetch.validated_data['phone']):
                    return Response(
                        {'Error':'Phone Number Already in Used'},
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

            return Response(
                    {'Success':'Profile is created','profile_ID': profile_ID},
                status=status.HTTP_201_CREATED)
        else:
            return Response(apifetch.errors)
        

