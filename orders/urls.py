from django.urls import path, include
from orders.views.coupon import (
    CouponView,CouponSingleView,CouponCreateView,
    CouponDeleteView,CouponEditView
)

from rest_framework import routers
from orders.views.cart_order import *

router = routers.DefaultRouter()
router.register('cart',MyCart,basename="MyCart")
router.register('orderviewset',OrderViewset,basename='OrderView')

urlpatterns = [
    path("",include(router.urls)),
    path("addtocart/",AddtoCartView.as_view(),name="addtocart"),
    path('updatecart/',Updatecart.as_view(),name='updatecart'),
    path('editcart/',Editcart.as_view(),name='editcart'),
    path('deletecart/',DeleteCart.as_view(),name='deleltecart'),
]

coupon_URL = [
    path('list/',CouponView.as_view()),
    path('<int:pk>/',CouponSingleView.as_view()),
    path('edit/<int:pk>/',CouponEditView.as_view()),
    path('create/',CouponCreateView.as_view()),
    path('delele/<int:pk>/',CouponDeleteView.as_view())
]

urlpatterns += coupon_URL