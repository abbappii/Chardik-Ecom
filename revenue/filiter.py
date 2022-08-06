

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import RevenueHistory

from django.utils import timezone
from django.db.models import Sum
from datetime import timedelta

now = timezone.now()

class RevenueReports_View(APIView):
    
    def get(self,request):
        # qs = RevenueHistory.objects.filter(created_at__gte=now - \
        #     timedelta(hours=1)).\
        #         aggregate(total=Sum('profits'))
        # return Response(qs)
        return Response({
            # last 24 hours
            'last_24_hours':RevenueHistory.objects.filter(created_at__gte=now - \
            timedelta(hours=24)).\
                aggregate(total=Sum('profits')), 
            #last 7 days
            'weekly': RevenueHistory.objects.filter(created_at__gte= now - \
            timedelta(days=7)).aggregate(total_sum=Sum('profits')),

            # last month
            'monthly': RevenueHistory.objects.filter(created_at__gte= now - \
            timedelta(days=30)).aggregate(total_sum=Sum('profits')),

            # Half Yearly revenue 
            'half_yearly_sale':RevenueHistory.objects.filter( created_at__gte = now - \
            timedelta(days=(6 * 365 / 12))).aggregate(total_sum=Sum('profits')),

            # Yearly Sale 
            'yearly_sale':RevenueHistory.objects.filter(created_at__gte = now - \
            timedelta(days=365)).aggregate(total_sum=Sum('profits'))

        })



from rest_framework import generics
from .serializers import RevenueAPI

# last 24 hours 
class last_24_hour_revenue(generics.ListAPIView):
    queryset = RevenueHistory.objects.filter(created_at__gte = now - timedelta(hours=24), is_active=True)
    serializer_class = RevenueAPI

# weekly revenue 
class weekly_revenue(generics.ListAPIView):
    queryset = RevenueHistory.objects.filter(created_at__gte = now - timedelta(days=7), is_active=True)
    serializer_class = RevenueAPI

# monthly revenue 
class monthly_revenue(generics.ListAPIView):
    queryset = RevenueHistory.objects.filter(created_at__gte = now - timedelta(days=30), is_active=True)
    serializer_class = RevenueAPI

# half yearly 
class half_yearly_revenue(generics.ListAPIView):
    queryset = RevenueHistory.objects.filter(created_at__gte = now - timedelta(days = 6 * 365 /12 ), is_active=True)
    serializer_class = RevenueAPI

# yearly 
class yearly_revenue(generics.ListAPIView):
    queryset = RevenueHistory.objects.filter(created_at__gte = now - timedelta(days=365), is_active=True)
    serializer_class = RevenueAPI
