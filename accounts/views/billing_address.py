'''
This file contain of 
    - Billing  View functions
    - Buesiness Logics 
'''

from rest_framework import generics

# importing models 
from accounts.models.profile import BillingAddress

# importng api
from accounts.serializers.billing_address import Billing_Address_Serialiazer

from accounts.models.user_model import User

from rest_framework.views import APIView

from rest_framework.response import Response


'''
Coupon Logics 
    - Create 
    - Update 
    - View 
    - Delete
'''

# view List Function 

class BillingAddressView(generics.ListAPIView):
    queryset = BillingAddress.objects.all().order_by('-updated_at')
    serializer_class = Billing_Address_Serialiazer


# Single View 

class BillingAddressViewFatch(generics.RetrieveAPIView):
    queryset = BillingAddress.objects.all()
    serializer_class = Billing_Address_Serialiazer


#  Create View 

class BillingAddressCreateView(generics.CreateAPIView):
    queryset = BillingAddress.objects.all()
    serializer_class = Billing_Address_Serialiazer


# delete View 

class BillingAddressDeleteView(generics.DestroyAPIView):
    queryset = BillingAddress.objects.all()
    serializer_class = Billing_Address_Serialiazer


# Single Edit View 

class BillingAddressEditView(generics.UpdateAPIView):
    queryset = BillingAddress.objects.all()
    serializer_class = BillingAddress




class ShowBillingAddress(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        get_user = BillingAddress.objects.all()
        Billing_serializer = Billing_Address_Serialiazer(get_user, many=True)
        return Response(Billing_serializer.data)