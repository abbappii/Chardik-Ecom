## Revenue URLs 

from django.urls import path

## importing views 
from revenue.views import (
    RevenueListView,
    RevenueSingleView,
    RevenueDeleteView
)

from revenue.filiter import (
    RevenueReports_View,
    daily_revenue,
    last_24_hour_revenue,
    weekly_revenue,
    monthly_revenue,
    half_yearly_revenue,
    yearly_revenue
)


urlpatterns = [
    path('list/',RevenueListView.as_view()),
    path('view/<int:pk>/',RevenueSingleView.as_view()),
    path('delete/<int:pk>/',RevenueDeleteView.as_view())
]

urlpatterns_revenue_reports = [ 
    path('revenue/totals/',RevenueReports_View.as_view()), 
    
]
urlpatterns_revenue_values = [ 
    path('revenue/list/last-24-hours/',last_24_hour_revenue.as_view()),
    path('revenue/list/daily/',daily_revenue.as_view()),
    path('revenue/list/weekly/',weekly_revenue.as_view()),
    path('revenue/list/monthly/', monthly_revenue.as_view()),
    path('revenue/list/half-yearly/', half_yearly_revenue.as_view()),
    path('revenue/list/yearly/', yearly_revenue.as_view()),
]

urlpatterns += urlpatterns_revenue_reports
urlpatterns += urlpatterns_revenue_values