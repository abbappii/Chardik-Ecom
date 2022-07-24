'''
This file contain of 
    - Billing  View functions
    - Buesiness Logics 
'''

from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework import status

# importing models 
from accounts.models.profile import BillingAddress

# importng api
from accounts.serializers.billing_address import Billing_Address_Serialiazer


from rest_framework.generics import GenericAPIView 

from rest_framework.response import Response

from MainApplication.scripts.permission import (
    IsCustomer,
)


'''
Billing Address Logics 
    - Create 
    - Update 
    - List View 
    - single view
    - Delete
'''

# view List Function 
@permission_classes([IsCustomer])
class BillingAddressView(generics.ListAPIView):
    queryset = BillingAddress.objects.filter(is_active=True,is_billing=True)
    serializer_class = Billing_Address_Serialiazer

    def get(self,request):
        user = request.user.profile
        data_fetch = BillingAddress.objects.filter(
                customer=user,is_active=True,is_biling=True
                )
        apifetch = Billing_Address_Serialiazer(data_fetch,many=True)
        return Response(
            apifetch.data,
            status=status.HTTP_200_OK)

    def post(self,request):
        user = request.user.profile
        data_fetch = BillingAddress(customer=user)
        apifetch = Billing_Address_Serialiazer(data_fetch,data=request.data)
        if apifetch.is_valid():
            apifetch.save()
            return Response(
                apifetch.data,
                status=status.HTTP_201_CREATED)
        else:
            return Response(
                apifetch.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

@permission_classes([IsCustomer])
class ShippingAddressView(generics.ListAPIView):
    queryset = BillingAddress.objects.filter(is_active=True,is_billing=False)
    serializer_class = Billing_Address_Serialiazer

    def get(self,request):
        user = request.user.profile
        data_fetch = BillingAddress.objects.filter(
                customer=user,is_active=True,is_biling=False
                )
        apifetch = Billing_Address_Serialiazer(data_fetch,many=True)
        return Response(
            apifetch.data,
            status=status.HTTP_200_OK)


# Single View 
class BillingAddressViewFatch(generics.RetrieveAPIView):
    queryset = BillingAddress.objects.all()
    serializer_class = Billing_Address_Serialiazer


#  Create View 
class BillingAddressCreateView(generics.CreateAPIView):
    queryset = BillingAddress.objects.filter(is_active=True)
    serializer_class = Billing_Address_Serialiazer


# delete View 
class BillingAddressDeleteView(generics.DestroyAPIView):
    queryset = BillingAddress.objects.all()
    serializer_class = Billing_Address_Serialiazer


# Single Edit View 
class BillingAddressEditView(generics.UpdateAPIView):
    queryset = BillingAddress.objects.all()
    serializer_class = BillingAddress


# class ShowBillingAddress(APIView):
#     """
#     List all billingAddress.
#     """
#     def get(self, request, format=None):
#         get_user = BillingAddress.objects.all()
#         Billing_serializer = Billing_Address_Serialiazer(get_user, many=True)
#         return Response(Billing_serializer.data)