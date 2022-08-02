
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.database.cart_order import Order
from orders.serializers import OrderSerializer, OrderAPI
from django.db.models import Sum

from datetime import datetime, timedelta
from django.utils import timezone
now = timezone.now()

class passParams(APIView):
    def get(self,request, *args, **kwargs):
        query = Order.objects.all()

        #custom filter parameters
        hourly = self.request.query_params.get('hourly',None)
        hourly_24 = self.request.query_params.get('24_hourly',None)
        daily = self.request.query_params.get('daily',None)
        monthly = self.request.query_params.get('monthly',None)
        half_yearly = self.request.query_params.get('half_yearly',None)
        yearly = self.request.query_params.get('yearly',None)

        if hourly:
            query = query.filter(created_at__gte = datetime.now() - timedelta(hours=1)).aggregate(hourly_sales =Sum('total'))
        if hourly_24:
            query = query.filter(created_at__gte=datetime.now()-timedelta(hours=24)).aggregate(hourly_24 =Sum('total'))
        if daily:
            query = query.filter(created_at__gte=now.date()).aggregate(daily_total=Sum('total'))
       
        if monthly: 
            query = query.filter(created_at__gte = now - timedelta(days=30)).aggregate(monthly_sales =Sum('total'))
        if half_yearly:
            query = query.filter(created_at__gte = now - timedelta(days = 6 * 365 /12 )).aggregate(half_yearly =Sum('total'))

        if yearly:
            query = query.filter(created_at__gte = now - timedelta(days = 365 )).aggregate(yearly =Sum('total'))

        serializer = OrderSerializer(query, many=True)

        return Response(serializer.data)


from rest_framework import generics

# last 24 hours 
class last_24_hour_list(generics.ListAPIView):
    queryset = Order.objects.filter(created_at__gte = now - timedelta(hours=24), is_active=True)
    serializer_class = OrderAPI

# hourly 
class hourly_View(generics.ListAPIView):
    queryset = Order.objects.filter(created_at__gte = datetime.now() - timedelta(hours=1), is_active=True)
    serializer_class = OrderAPI

# daily 
class daily_view(generics.ListAPIView):
    queryset = Order.objects.filter( created_at__gte=now.date(), is_active=True )
    serializer_class = OrderAPI

# # monthly 
# class monthly_View(generics.ListAPIView):
#     queryset = Order.objects.filter(created_at__gte = now - timedelta(days=30), is_active=True)
#     serializer_class = OrderAPI

# # half yearly 
# class half_yearly_View(generics.ListAPIView):
#     queryset = Order.objects.filter(created_at__gte = now - timedelta(days = 6 * 365 /12 ), is_active=True)
#     serializer_class = OrderAPI

# # yearly 
# class yearly_View(generics.ListAPIView):
#     queryset = Order.objects.filter(created_at__gte = now - timedelta(days = 365 ), is_active=True)
#     serializer_class = OrderAPI

    