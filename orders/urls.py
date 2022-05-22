from django.urls import path
from orders.views.coupon import (
    CouponView,CouponSingleView,CouponCreateView,
    CouponDeleteView,CouponEditView
)

urlpatterns = []

coupon_URL = [
    path('list/',CouponView.as_view()),
    path('<int:pk>/',CouponSingleView.as_view()),
    path('edit/<int:pk>/',CouponEditView.as_view()),
    path('create/',CouponCreateView.as_view()),
    path('delele/<int:pk>/',CouponDeleteView.as_view())
]

urlpatterns += coupon_URL