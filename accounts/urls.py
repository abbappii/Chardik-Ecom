from django.urls import path

from accounts.views.user_create import *
from accounts.views.permission_view import (
    PermissionCreateView,PermissionDestroyView,PermissionEditView,
    PermissionListsView,PermissionSingleView
)

urlpatterns = [ 
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view()),
]

permission_URL =[
    path('permission/create/',PermissionCreateView.as_view()),
    path('permission/view/',PermissionListsView.as_view()),
    path('permission/view/<int:pk>/',PermissionSingleView.as_view()),
    path('permission/edit/<int:pk>/',PermissionEditView.as_view()),
    path('permission/delete/<int:pk>/',PermissionDestroyView.as_view())
]


urlpatterns += permission_URL