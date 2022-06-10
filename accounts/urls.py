from django.urls import path

from accounts.views.password_rest import (
    UserChangePasswordView,
    UserPasswordRestEmailView,
    UserPasswordEmailLinkResetView
)

from accounts.views.permission_view import (
    PermissionCreateView,PermissionDestroyView,PermissionEditView,
    PermissionListsView,PermissionSingleView
)

from accounts.views.user_up_del_view import( 
    UserDataUpdate, UserDeleteView
)
from accounts.views.user_init import (
    LoginView,RegisterView, UserProfileView, SendSMS,VerifyOTP
)

urlpatterns = [ 
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('sms/',SendSMS.as_view()),
    path('verify/otp/<int:profile_ID>/',VerifyOTP.as_view())

]

permission_URL =[
    path('permission/create/',PermissionCreateView.as_view()),
    path('permission/view/',PermissionListsView.as_view()),
    path('permission/view/<int:pk>/',PermissionSingleView.as_view()),
    path('permission/edit/<int:pk>/',PermissionEditView.as_view()),
    path('permission/delete/<int:pk>/',PermissionDestroyView.as_view())
]


user_update_delete = [ 
    path('user_update/',UserDataUpdate.as_view()),
    path('user_delete/<int:pk>/', UserDeleteView.as_view()),
]

user_pass_change_reset_email = [ 
    path('changepassword/', UserChangePasswordView.as_view()),
    path('send-reset-password-email/',UserPasswordRestEmailView.as_view()),
    path('reset-password/<uid>/<token>/',UserPasswordEmailLinkResetView.as_view()),
]

urlpatterns += permission_URL
urlpatterns += user_update_delete
urlpatterns += user_pass_change_reset_email