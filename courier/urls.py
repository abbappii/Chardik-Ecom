from django.urls import  path
from courier import views

urlpatterns = [
    path('pathao/', views.pathao_view),
    path('pathao/refresh-token/', views.pathao_refresh_token),
    path('pathao/get-cities/', views.pathao_get_cites),
    path('pathao/get-zone/', views.pathao_get_zone),
    path('pathao/get-area/', views.pathao_get_area),
    path('pathao/create-store/', views.pathao_create_store),
    path('pathao/get-store/', views.pathao_get_store),
    path('pathao/create-order/', views.pathao_create_order),
    path('pathao/price-calculation/', views.pathao_price_calculation),
]
