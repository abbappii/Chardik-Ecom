## Revenue URLs 

from django.urls import path

## importing views 
from revenue.views import (
    RevenueListView,
    RevenueSingleView,
    RevenueDeleteView
)

urlpatterns = [
    path('list/',RevenueListView.as_view()),
    path('view/<int:pk>/',RevenueSingleView.as_view()),
    path('delete/<int:pk>/',RevenueDeleteView.as_view())
]

