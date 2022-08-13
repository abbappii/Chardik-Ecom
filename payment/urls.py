
from django.urls import path
from .views  import *

urlpatterns = [ 
    path('pay/',payment.as_view(), name='pay_view'),
]