from django.urls import path
from inventory import views
urlpatterns = [
    path('show-purchase/', views.PurchaseList.as_view()),
    path('purchase-edit-delete-update/<int:pk>/', views.PurchaseDetail.as_view()),
]
