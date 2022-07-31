
from django.urls import path

# from pos_manager.views import OfflineProfileCreateView
from pointsofsale_manager.views.pos_info import PointsOfSaleCreateView
from pointsofsale_manager.views.offline_profile import (
    OfflineProfileCreateView,
    POS_OrderView
)

urlpatterns = [ 
    # path('',OfflineProfileCreateView.as_view()),
    path('pos-create/', PointsOfSaleCreateView.as_view()),
    path('pos-profie-create/', OfflineProfileCreateView.as_view()),
    path('order/create/',POS_OrderView.as_view())
]