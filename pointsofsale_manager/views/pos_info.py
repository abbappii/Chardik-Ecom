from django.shortcuts import render

# Create your views here.
from pointsofsale_manager.serializers.pos_info_serializers import PointsOfSaleSerializers
from pointsofsale_manager.models import PointsOfSale

from rest_framework import generics

class PointsOfSaleCreateView(generics.CreateAPIView):
    queryset = PointsOfSale.objects.all()
    serializer_class = PointsOfSaleSerializers

