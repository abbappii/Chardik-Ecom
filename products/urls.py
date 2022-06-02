
from django.urls import path
from products.views.prodcuts_logic import (
    ProductListViewSet,
    ProductCreateView,
    ProductRetUpDesViewSet
)

from products.views.products_init_logic import (
    CategoriesViewSet, 
    CategoriesUpdateDelete, 
    SubCategoriesViewSet, 
    SubCategoriesUpdateDelete,
    BrandView,
    BrandUpdateDelete,
    CountryView,
    CountryUpdateDelete
     
)

from products.views.product_review_logic import (
    ProducReviewtListView, ProductReviewCreateView,
    ProductReviewRetrieveView, ProductReviewEditView,
    ProductReviewDeleteView
)

urlpatterns = [ 
    path('categories/', CategoriesViewSet.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoriesUpdateDelete.as_view(), name='categories_update_delete'),
    path('sub_categories/', SubCategoriesViewSet.as_view(), name='sub_categories'),
    path('sub_categories/<int:pk>/', SubCategoriesUpdateDelete.as_view(),
        name='sub_categories_update_delete'),
]

urlpatterns_product = [ 
    path('product/', ProductListViewSet.as_view(), name='products' ),
    path('product/create/',ProductCreateView.as_view(), name='product_create' ),
    path('product/<slug:slug>/',ProductRetUpDesViewSet.as_view(), name='products_delete_update' ),
    # products renderer url 
    # path('product/', ProductListViewSet.as_view(), name='products' ),
    # path('product/create/',ProductCreateView.as_view(), name='product_create' ),
    # path('product/<slug:slug>/',ProductDetail.as_view(), name='products_detail' ),
]


urlpatterns_brand_countries = [ 
    path('brand/', BrandView.as_view(), name='brand' ),
    path('brand/<int:pk>/', BrandUpdateDelete.as_view(), name='brand_update_delete' ),
    path('countries/', CountryView.as_view(), name='country' ),
    path('countries/<int:pk>/', CountryUpdateDelete.as_view(), name='country_update_delete' ),
]


urlpatterns_productsReview = [ 
    path('review/',ProducReviewtListView.as_view()),
    path('review/create/',ProductReviewCreateView.as_view()),
    path('review/view/<int:pk>/', ProductReviewRetrieveView.as_view()),
    path('review/update/<int:pk>/',ProductReviewEditView.as_view()),
    path('review/delete/<int:pk>/',ProductReviewDeleteView.as_view()),
]


urlpatterns += urlpatterns_product
urlpatterns += urlpatterns_brand_countries
urlpatterns += urlpatterns_productsReview