from django.urls import path
from products.views.prodcuts_logic import *
from products.views.products_init_logic import *

urlpatterns = [ 
    #Category URL
    path('categories/', CategoriesViewSet.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoriesUpdateDelete.as_view(), name='categories_update_delete'),
    
    #Sub Category URL
    path('sub_categories/', SubCategoriesViewSet.as_view(), name='sub_categories'),
    path('sub_categories/<int:pk>/', SubCategoriesUpdateDelete.as_view(),name='sub_categories_update_delete'),

    # products URL
    path('product/', ProductListViewSet.as_view(), name='products' ),
    path('product/create/',ProductCreateView.as_view(), name='product_create' ),
    path('product/<slug:slug>/',ProductRetUpDesViewSet.as_view(), name='products_delete_update' ),

    # Brand part URL
    path('brand/', BrandView.as_view(), name='brand' ),
    path('brand/<int:pk>/', BrandUpdateDelete.as_view(), name='brand_update_delete' ),


    #Country part 
    path('countries/', CountryView.as_view(), name='country' ),
    path('countries/<int:pk>/', CountryUpdateDelete.as_view(), name='country_update_delete' ),


]