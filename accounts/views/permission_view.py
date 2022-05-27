'''
This file contains the following 
    - Permission Create 
    - Edit, View , Delete
'''


from rest_framework import generics

# importing models 
from accounts.models.profile import Profile
# importng API
from accounts.serializers.profileAPI import (
    GivePermissionAPI,GivePermissionViewAPI
)
# importing Permissions 
from MainApplication.scripts.permission import (
    IsAdmin,IsManager
)


# Permission Create View

class PermissionCreateView(generics.CreateAPIView):
    permission_classes = [IsAdmin]
    queryset = Profile.objects.all()
    serializer_class = GivePermissionAPI


# Permission Edit View

class PermissionEditView(generics.UpdateAPIView):
    permission_classes = [IsAdmin|IsManager]
    queryset = Profile.objects.all()
    serializer_class = GivePermissionAPI


# Permission Delete View

class PermissionDestroyView(generics.DestroyAPIView):
    permission_classes = [IsAdmin|IsManager]
    queryset = Profile.objects.all()
    serializer_class = GivePermissionAPI


# Permission List View

class PermissionListsView(generics.ListAPIView):
    permission_classes = [IsAdmin|IsManager]
    queryset = Profile.objects.all()
    serializer_class = GivePermissionViewAPI


# Permission Signle View

class PermissionSingleView(generics.RetrieveAPIView):
    permission_classes = [IsAdmin|IsManager]
    queryset = Profile.objects.all()
    serializer_class = GivePermissionViewAPI