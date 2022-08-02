


from rest_framework.response import Response
from rest_framework.views import APIView

from inventory.bank_model.baccounts import Expenses
from inventory.bank_serializer.expence_serializers import ExpenceListSerializers
from django.db.models import Sum

from datetime import datetime, timedelta
from django.utils import timezone
now = timezone.now()


'''
hourly expences
'''
class HourlyExpenceView(APIView):
    
    def get(self,request):
        qs = Expenses.objects.filter(created_at__gte = now - timedelta(hours=1)).aggregate(last_hour=Sum('expence_amount'))
        return Response(qs)


'''
24 hours expences 
'''
class last_24_hours_ExpenceView(APIView):
    
    def get(self,request):
        qs = Expenses.objects.filter(created_at__gte = now - timedelta(hours=24)).aggregate(last_24_hour=Sum('expence_amount'))
        return Response(qs)


'''
last 7 days expences
'''

class WeeklyExpenceView(APIView):
    def get(self,request):
        qs =Expenses.objects.filter(created_at__gte= now - \
            timedelta(days=7)).aggregate(weekly=Sum('expence_amount'))
        return Response(qs)
    

'''
last 30 days expences
'''
class MonthlyExpenceView(APIView):
    def get(self,request):
        queryset = Expenses.objects.filter(created_at__gte= now - \
            timedelta(days=30)).aggregate(last_30_days =Sum('expence_amount'))
        return Response(queryset)

'''
last 6 months expences
'''
month_ago = 6
class HalfYearlyExpenceView(APIView):
    def get(self,request):
        queryset = Expenses.objects.filter(created_at__gte = now - \
            timedelta(days=(month_ago * 365 / 12))).aggregate(lastt_6_months=Sum('expence_amount'))

        return Response(queryset)

'''
last 1 years expence
'''
class YearlyExpenceView(APIView):
    def get(self,request):
        queryset = Expenses.objects.filter(created_at__gte = now - \
            timedelta(days=365)).aggregate(last_1_year_expence=Sum('expence_amount'))
        return Response(queryset)


'''
Expences with values
        - total
        - created date
'''
from inventory.bank_serializer.expence_serializers import  ExpenceListSerializers
from rest_framework import generics

# hourly expence with values 
class hourly_expence_view(generics.ListAPIView):
    queryset = Expenses.objects.filter(created_at__gte = now - timedelta(hours=1), is_active=True)
    serializer_class = ExpenceListSerializers

# 24 hours expence with values 
class twenty_4_hours_expence_view(generics.ListAPIView):
    queryset = Expenses.objects.filter(created_at__gte = now - timedelta(hours=24), is_active=True)
    serializer_class = ExpenceListSerializers

# daily expence with values 
class daily_expence_view(generics.ListAPIView):
    queryset = Expenses.objects.filter( created_at__gte=now.date(),is_active=True )
    serializer_class = ExpenceListSerializers