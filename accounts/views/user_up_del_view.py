
'''
UserProfile update
User Delete
'''

from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from accounts.models.profile import Profile


from MainApplication.scripts.permission import (
    IsAdmin,IsManager, IsCustomer
)
from accounts.models.user_model import User
from accounts.serializers.user_auth import (
    UserProfileSeriliazer
)

'''
User Profile Update View
'''
class UserDataUpdate(GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSeriliazer
    permission_classes = [IsCustomer]

    def post(self,request):
        user = request.user.profile
        user_query = Profile.objects.get(user=user)

        data = request.data
        serializer = UserProfileSeriliazer(user_query, data=data)
        if serializer.is_valid():
            serializer.save()
            # return Response({'msg': 'Information updated successfully'})
            return Response(serializer.data)

        # return Response({'msg':'serializers error!'})
        return Response(serializer.errors)




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

