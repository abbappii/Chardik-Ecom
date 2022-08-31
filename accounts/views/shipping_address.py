

# from rest_framework.generics import GenericAPIView

# from accounts.models.profile import ShippingAddress
# from accounts.serializers.billing_address import Shipping_Address_Serialiazer

# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import generics

# '''
# shipping address
#         - list 
#         - create
# '''

# class ShippingAddressListCreateView(GenericAPIView):
#     queryset = ShippingAddress.objects.filter(is_active=True)
#     serializer_class = Shipping_Address_Serialiazer

#     def get(self,request):
#         customer = request.user.profile
#         qs = ShippingAddress.objects.fiilter(customer=customer, is_active=True)
#         serailizer = Shipping_Address_Serialiazer(qs,many=True)
#         return Response(
#             serailizer.data,
#             status=status.HTTP_200_OK)
    
#     def post(self, request):
#         customer = request.user.profile
#         qs = ShippingAddress(customer=customer)
#         serializer = Shipping_Address_Serialiazer(qs, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# # Single View 
# class ShippingAddressSingleView(generics.RetrieveAPIView):
#     queryset = ShippingAddress.objects.all()
#     serializer_class = Shipping_Address_Serialiazer


# # delete View 
# class ShippingAddressDeleteView(generics.DestroyAPIView):
#     queryset = ShippingAddress.objects.all()
#     serializer_class = Shipping_Address_Serialiazer


# # Edit View 
# class ShippingAddressEditView(generics.UpdateAPIView):
#     queryset = ShippingAddress.objects.all()
#     serializer_class = Shipping_Address_Serialiazer