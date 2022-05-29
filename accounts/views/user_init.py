'''
This file contains followings
    - User context
    - login view 
    - register view 


'''


from rest_framework.generics import GenericAPIView
from django.db.models import Q
from rest_framework.response import Response
from django.contrib.auth import authenticate

# importing API
from accounts.serializers.user_auth import LoginSerializer

# importing models 
from accounts.models.user_model import User
from accounts.models.profile import Profile


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


