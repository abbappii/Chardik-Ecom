from django.urls import path

from accounts.views.password_rest import (
    UserChangePasswordView,
    UserPasswordRestEmailView,
    UserPasswordEmailLinkResetView
)

from accounts.views.permission_view import (
    PermissionCreateView,
    PermissionDestroyView,
    PermissionEditView,
    PermissionListsView,
    PermissionSingleView
)

from accounts.views.user_up_del_view import( 
    UserDataUpdate, UserDeleteView
)
from accounts.views.user_init import (
    LoginView,RegisterView, 
    UserProfileView, SendSMS,
    VerifyOTP,
    ForgetPassword__with__Phone,ChangePasswordInstant, 
    UserProfileList,
    ProfileSingle_view
)

from accounts.views.billing_address import (
    BillingAddressDeleteView,
    BillingAddressView,
    ShippingAddressView
)
from accounts.views.points_profile import (
    PointLooseView,
    PointAddView
)

# from accounts.views.shipping_address import (
#     ShippingAddressDeleteView,
#     ShippingAddressListCreateView
# )
urlpatterns = []

user_URL = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('sms/',SendSMS.as_view()),
    path('verify/otp/',VerifyOTP.as_view()),
    path('forget/password/phone/',ForgetPassword__with__Phone.as_view()),
    path('change/password/',ChangePasswordInstant.as_view()),
    path('profile/list/',UserProfileList.as_view()),
    path('profile/single/view/<int:pk>/',ProfileSingle_view.as_view()),
]

permission_URL =[
    path('permission/create/',PermissionCreateView.as_view()),
    path('permission/view/',PermissionListsView.as_view()),
    path('permission/view/<int:pk>/',PermissionSingleView.as_view()),
    path('permission/edit/<int:pk>/',PermissionEditView.as_view()),
    path('permission/delete/<int:pk>/',PermissionDestroyView.as_view())
]


user_update_delete = [ 
    path('user_profile_update/',UserDataUpdate.as_view()),
    path('user_delete/<int:pk>/', UserDeleteView.as_view()),
]

user_pass_change_reset_email = [ 
    path('changepassword/', UserChangePasswordView.as_view()),
    path('send-reset-password-email/',UserPasswordRestEmailView.as_view()),
    path('reset-password/<uid>/<token>/',UserPasswordEmailLinkResetView.as_view()),
]

billingAddress_URL = [
    path('billing/address/',BillingAddressView.as_view()),
    path('shipping/address/',ShippingAddressView.as_view()),
    path('billng/address/delete/<int:pk>/', BillingAddressDeleteView.as_view()),
]

point_URL = [
    path('points/loose/',PointLooseView.as_view()),
    path('points/add/',PointAddView.as_view())
]

# shippingAddress_URL = [ 
#     path('shipping/address/list-create/',ShippingAddressListCreateView.as_view()),
#     path('shipiing/address/delete/<int:pk>/', ShippingAddressDeleteView.as_view()),
# ]

urlpatterns += user_URL
urlpatterns += permission_URL
urlpatterns += user_update_delete
urlpatterns += user_pass_change_reset_email
urlpatterns += billingAddress_URL
urlpatterns += point_URL
# urlpatterns += shippingAddress_URL