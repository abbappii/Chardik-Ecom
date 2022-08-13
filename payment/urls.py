
from django.urls import path
from .views  import *

urlpatterns = [ 
    path('pay/',payment.as_view(), name='pay_view'),
    path('pay/success/', payment_success, name='success_payment'),
    # path('refund/', refund_request, name='refund_request'),
]