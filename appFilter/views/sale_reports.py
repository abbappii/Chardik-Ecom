'''
Sale reports of the followings
o Daily sales
o Weekly sales
o Monthly sales
'''

from datetime import datetime,timedelta
from django.utils import timezone
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response

from orders.database.cart_order import (
    Order
)

'''
o Daily sales
o Weekly sales
o Monthly sales
'''

now = timezone.now()

class SaleReports_View(APIView):
    
    def get(self,request):
        return Response({

            # daily sale 
            'daily_sale':Order.objects.filter(order_status="Completed",created_at__gte=now.date()).\
                aggregate(total=Sum('total')),

            # hourly sale 
            'hourly_sale':Order.objects.filter(order_status="Completed",created_at__gte=datetime.now() - \
            timedelta(hours=1)).aggregate(total=Sum('total')),
            
            # 24 hours sale
            '24_hours_sale':Order.objects.filter(order_status="Completed",created_at__gte= now - \
            timedelta(hours=24)).aggregate(total_sum=Sum('total')),

            # Weekily sale
            'weekly_sale':Order.objects.filter( order_status="Completed", created_at__gte= now - \
            timedelta(days=7)).aggregate(total_sum=Sum('total')),
        
            # Monthly Sale
            'monthly_sale': Order.objects.filter(order_status="Completed",created_at__gte= now - \
            timedelta(days=30)).aggregate(total_sum=Sum('total')),

            # Half Yearly Sale 
            'half_yearly_sale':Order.objects.filter( order_status="Completed", created_at__gte = now - \
            timedelta(days=(6 * 365 / 12))).aggregate(total_sum=Sum('total')),

            # Yearly Sale 
            'yearly_sale':Order.objects.filter( order_status="Completed", created_at__gte = now - \
            timedelta(days=365)).aggregate(total_sum=Sum('total'))
        })