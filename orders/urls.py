from django.urls import path, include
from orders.views.coupon import (
    CouponView,CouponSingleView,CouponCreateView,
    CouponDeleteView,CouponEditView
)

# from rest_framework import routers
from orders.views.cart_order import *
from orders.views.order_view import (
    OrderSingleView,
    OrderView,
    AddOrderItem,
    OrderListview,
    OrderUpdateView,
    UserOrderListView,

    orderviewofcustomerAdminview
)

# router = routers.DefaultRouter()
# router.register('cart',MyCart,basename="MyCart")
# router.register('orderviewset',OrderViewset,basename='OrderView')

# urlpatterns = [
#     path("",include(router.urls)),
#     path("addtocart/",AddtoCartView.as_view(),name="addtocart"),
#     path('updatecart/',Updatecart.as_view(),name='updatecart'),
#     path('editcart/',Editcart.as_view(),name='editcart'),
#     path('deletecart/',DeleteCart.as_view(),name='deleltecart'),
# ]

urlpatterns =[]

coupon_URL = [
    path('coupon/list/',CouponView.as_view()),
    # path('coupon/singleview/<int:pk>/',CouponSingleView.as_view()),
    path('coupon/singleview/<slug:coupon_name>/',CouponSingleView.as_view()),
    path('coupon/edit/<int:pk>/',CouponEditView.as_view()),
    path('coupon/create/',CouponCreateView.as_view()),
    path('coupon/delele/<int:pk>/',CouponDeleteView.as_view())
]

order_URL = [
    path('order/',OrderView.as_view(),name="order_url"),
    path('add/item/',AddOrderItem.as_view(),name='add_to_cart'),

    path('list/',OrderListview.as_view()),
    path('update/<int:pk>/',OrderUpdateView.as_view()),
    path('customer/view/',UserOrderListView.as_view()),
    path('single/view/<int:pk>/', OrderSingleView.as_view ()),

    path('admin/user/order/show/<int:profileID>/', orderviewofcustomerAdminview.as_view()),

]

urlpatterns += order_URL
urlpatterns += coupon_URL