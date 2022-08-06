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
    
)


urlpatterns = [
    path('list/',RevenueListView.as_view()),
    path('view/<int:pk>/',RevenueSingleView.as_view()),
    path('delete/<int:pk>/',RevenueDeleteView.as_view())
]

urlpatterns_revenue_reports = [ 
    path('daily/revenue/',RevenueReports_View.as_view()), 
    
]
urlpatterns_revenue_values = [ 
]

urlpatterns += urlpatterns_revenue_reports
urlpatterns += urlpatterns_revenue_values