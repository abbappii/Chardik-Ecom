from rest_framework.views import APIView
from accounts.serializers.password_change import (UserPasswordChangedSerializer,
UserPasswordRestEmailSerializer,UserPasswordEmailLinkResetSerializer)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

'''
User Password Change View
User Password reset link create
User Password rest link send
'''

#User Password Change View
class UserPasswordChangedView(APIView):
    def post(self, request, format=None):
        permission_classes=[IsAuthenticated]
        serializer = UserPasswordChangedSerializer(data=request.data, context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'message':'Password Changed Successfully'}, status=status.HTTP_200_OK)
        return Response({'message':'Failed to Change Password'}, status=status.HTTP_400_BAD_REQUEST)


#User Password reset link create
class UserPasswordRestEmailView(APIView):
    def post(self,request,format=None):
        serializer = UserPasswordRestEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'message':'Reset Password Link sent Successfully'}, status=status.HTTP_200_OK)
        return Response({'message':'Failed to send reset Password link'}, status=status.HTTP_400_BAD_REQUEST)



#User Password rest link send
class UserPasswordEmailLinkResetView(APIView):
    def post(self, request, uid, token, format=None):
        serializer = UserPasswordEmailLinkResetSerializer(data=request.data, context={'uid':uid, 'token':token})
        if serializer.is_valid(raise_exception=True):
            return Response({'message':'Password Changed Successfully'}, status=status.HTTP_200_OK)
        return Response({'message':'Failed to Reset password'}, status=status.HTTP_400_BAD_REQUEST)