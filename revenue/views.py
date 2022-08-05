'''
This file contains the 
    views logic of Revenue
'''

## importing initals
from rest_framework import generics

## importing API
from revenue.serializers import(
    RevenueAPI
)
## models
from revenue.models import (
    RevenueHistory
)

## Revenue List view 
class RevenueListView(generics.ListAPIView):
    queryset = RevenueHistory.objects.filter(is_active=True)
    serializer_class = RevenueAPI


## Revenue Single view 
class RevenueSingleView(generics.RetrieveAPIView):
    queryset = RevenueHistory.objects.filter(is_active=True)
    serializer_class = RevenueAPI


## Revenue Delete View
class RevenueDeleteView(generics.DestroyAPIView):
    queryset = RevenueHistory.objects.filter(is_active=True)
    serializer_class = RevenueAPI
        