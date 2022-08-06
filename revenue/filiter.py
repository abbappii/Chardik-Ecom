

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

