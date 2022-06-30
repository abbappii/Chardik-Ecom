'''
This file contains 
    - POS manager URLs
'''

from django.urls import path

from pos_manager.views import OfflineProfileCreateView

urlpatterns = [ 
    path('',OfflineProfileCreateView.as_view()),
]