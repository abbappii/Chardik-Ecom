
from rest_framework import serializers

class FlashSaleserializer (serializers.ModelSerializer):
    start_time = serializers.DateTimeField(
                format="%Y-%m-%d %H:%M:%S", 
                input_formats=['%d-%m-%Y %H:%M:%S' , 
                'iso-8601'], 
                required = False
                )
    end_time  = serializers.DateTimeField(
                format="%Y-%m-%d %H:%M:%S", 
                input_formats=['%d-%m-%Y %H:%M:%S' , 
                'iso-8601'],
                required = False

                )
    benefit_value = serializers.DecimalField(max_digits=10, decimal_places=2) 