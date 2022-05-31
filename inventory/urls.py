from django.urls import path

from inventory.views.supplier_view import *
# from inventory.views.supplier_view import (
#     SupplierListView, SupplierRetrieveView, SupplierCreateApiView, SupplierDeleteApiView,
#     SupplierEditApiView
# )

urlpatterns = []

urlpattern_suppliers = [ 
    path('list/',SupplierListView.as_view, name = 'supplier_list'),
    path('single-view/<int:pk>/', SupplierRetrieveView.as_view(), name = 'single_view'),
    path('create/',SupplierCreateApiView.as_view, name = 'create'),
    path('delete/<int:pk>/', SupplierDeleteApiView.as_view(), name = 'delete'),
    path('edit/<int:pk>/', SupplierEditApiView.as_view(), name = 'edit'),

]

urlpatterns += urlpattern_suppliers