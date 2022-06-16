'''
This file contain of 
    - Counpon View functions
    - Buesiness Logics 
'''

from rest_framework import generics

# importing models 
from orders.database.coupon import Coupon

# importng api
from orders.serializers import CouponAPI


'''
Coupon Logics 
    - Create 
    - Update 
    - View 
    - Delete
'''

# view List Function 

class CouponView(generics.ListAPIView):
    queryset = Coupon.objects.all().order_by('-updated_at')
    serializer_class = CouponAPI


# Single View 

class CouponSingleView(generics.RetrieveAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponAPI


#  Create View 

class CouponCreateView(generics.CreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponAPI


# delete View 

class CouponDeleteView(generics.DestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponAPI


# Single Edit View 

class CouponEditView(generics.UpdateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponAPI