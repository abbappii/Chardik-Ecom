
'''
UserProfile update
User Delete
'''

from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from accounts.models.profile import Profile

from accounts.serializers.profile_up_de  import UserProfileSeriliazers

from MainApplication.scripts.permission import (
    IsAdmin,IsManager, IsCustomer
)
from accounts.models.user_model import User

'''
User Profile Update View
'''
class UserDataUpdate(GenericAPIView):
    permission_classes = [IsCustomer]

    def post(self,request):
        user = request.user
        user_query = User.objects.get(user=user)

        data = request.data
        serializer = UserProfileSeriliazers(user_query, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Information updated successfully'})
        return Response({'msg':'serializers error!'})



'''
User deletion
profile -->  User --> Delete
'''

class UserDeleteView(GenericAPIView):
    permission_classes = [IsAdmin|IsManager|IsCustomer]

    def delete(self, request, pk):
        # get profile by id 
        getProfile = Profile.objects.get(id=pk)
        # get user using profile id 
        getUser = User.objects.get(id=getProfile)

        getUser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT )

