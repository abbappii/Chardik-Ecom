
'''
This file contains the URL config of Inventory app
'''

from django.urls import path
# from inventory.views.purchase_view import (

# )
from inventory.views.supplier_view import (
    SupplierListView,SupplierEditApiView,SupplierCreateApiView,
    SupplierRetrieveView,SupplierDeleteApiView
)

urlpatterns = []

supplier_URL = [
    path('supplier/',SupplierListView.as_view()),
    path('supplier/view/<int:pk>/',SupplierRetrieveView.as_view()),
    path('supplier/update/<int:pk>/',SupplierEditApiView.as_view()),
    path('supplier/delete/<int:pk>/',SupplierDeleteApiView.as_view()),
    path('supplier/create/',SupplierCreateApiView.as_view())
]
