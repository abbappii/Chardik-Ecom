
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.database.cart_order import Order
from orders.serializers import  OrderAPI, OrderSerializer
from django.db.models import Sum

from datetime import timedelta
# from django.utils import timezone
# now = timezone.now()
import datetime
date = datetime.date.today()
now = datetime.datetime.today()


# class passParams(APIView):
#     def get(self,request, *args, **kwargs):
#         query = Order.objects.all()

#         #custom filter parameters
#         hourly = self.request.query_params.get('hourly',None)
#         hourly_24 = self.request.query_params.get('24_hourly',None)
#         daily = self.request.query_params.get('daily',None)
#         monthly = self.request.query_params.get('monthly',None)
#         half_yearly = self.request.query_params.get('half_yearly',None)
#         yearly = self.request.query_params.get('yearly',None)

#         if hourly:
#             query = query.filter(created_at__gte = datetime.now() - timedelta(hours=1)).aggregate(hourly_sales =Sum('total'))
#         if hourly_24:
#             query = query.filter(created_at__gte=datetime.now()-timedelta(hours=24)).aggregate(hourly_24 =Sum('total'))
#         if daily:
#             query = query.filter(created_at__gte=now.date()).aggregate(daily_total=Sum('total'))
       
#         if monthly: 
#             query = query.filter(created_at__gte = now - timedelta(days=30)).aggregate(monthly_sales =Sum('total'))
#         if half_yearly:
#             query = query.filter(created_at__gte = now - timedelta(days = 6 * 365 /12 )).aggregate(half_yearly =Sum('total'))

#         if yearly:
#             query = query.filter(created_at__gte = now - timedelta(days = 365 )).aggregate(yearly =Sum('total'))

#         serializer = OrderSerializer(query, many=True)

#         return Response(serializer.data)


from rest_framework import generics

# last 24 hours 
class last_24_hour_list(generics.ListAPIView):
    queryset = Order.objects.filter( order_status="Completed", created_at__gte = now - timedelta(hours=24), is_active=True).order_by('-created_at')
    serializer_class = OrderSerializer 

# hourly 
class hourly_View(generics.ListAPIView):
    queryset = Order.objects.filter( order_status="Completed", created_at__gte = now - timedelta(hours=1), is_active=True).order_by('-created_at')
    serializer_class = OrderSerializer

# daily 

class daily_view(generics.ListAPIView):
    queryset = Order.objects.filter( order_status="Completed", created_at__gte = date, is_active=True ).order_by('-created_at')
    # print('todays date is: ',date)
    # print(now)
    serializer_class = OrderSerializer

# # monthly 
class monthly_View(generics.ListAPIView):
    queryset = Order.objects.filter( order_status="Completed", created_at__gte = now - timedelta(days=30), is_active=True).order_by('-created_at')
    serializer_class = OrderSerializer

# # half yearly 
class half_yearly_View(generics.ListAPIView):
    queryset = Order.objects.filter( order_status="Completed", created_at__gte = now - timedelta(days = 6 * 365 /12 ), is_active=True).order_by('-created_at')
    serializer_class = OrderSerializer

# # yearly 
class yearly_View(generics.ListAPIView):
    queryset = Order.objects.filter( order_status="Completed", created_at__gte = now - timedelta(days = 365 ), is_active=True).order_by('-created_at')
    serializer_class = OrderSerializer

    