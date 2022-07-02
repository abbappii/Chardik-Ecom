
from pointsofsale_manager.models import PointsOfSale

from rest_framework import serializers


class PointsOfSaleSerializers(serializers.ModelSerializer):
    class Meta:
        model = PointsOfSale
        fields = ['id','outlet','user']