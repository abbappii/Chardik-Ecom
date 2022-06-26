
from django.urls import path
from products.views.prodcuts_logic import (
    ProductListViewSet,
    ProductCreateView,
    ProductRetUpDesViewSet,
    ProductVariationCreate,
    ProductVariationSingle_updateView,
    ProductVariation_DeleteView,
    ProductVariationSingleView
)

from products.views.products_init_logic import (
    CategoriesViewSet, 
    CategoriesUpdateDelete, 
    SubCategoriesViewSet, 
    SubCategoriesUpdateDelete,
    BrandView,
    BrandUpdateDelete,
    CountryView,
    CountryUpdateDelete,
    ColorVariationListAPIview,
    ColorVariationSingleAPIview,
    SizeVariationListAPIview,
    SizeVariationSingleAPIview,
    WeightVariationListAPIview,
    WeightVariationSingleAPIview
     
)

from products.views.product_review_logic import (
    ProducReviewtListView, 
    ProductReviewCreateView,
    ProductReviewRetrieveView, 
    ProductReviewEditView,
    ProductReviewDeleteView
)


from products.views.slider_logic import (
    SliderListView, 
    SliderSingleView,
    SliderCreateView,
    SliderEditView,
    SliderDeleteView
)



urlpatterns = []


urlpatterns_category = [
    path('categories/', CategoriesViewSet.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoriesUpdateDelete.as_view(), 
        name='categories_update_delete'),
    path('sub_categories/', SubCategoriesViewSet.as_view(), name='sub_categories'),
    path('sub_categories/<int:pk>/', SubCategoriesUpdateDelete.as_view(),
        name='sub_categories_update_delete'),
]

urlpatterns_product = [ 
    path('product/', ProductListViewSet.as_view(), name='products' ),
    path('product/create/',ProductCreateView.as_view(), name='product_create' ),
    path('product/<slug:slug>/',ProductRetUpDesViewSet.as_view(), 
        name='products_delete_update' ),
    # products renderer url 
    # path('product/', ProductListViewSet.as_view(), name='products' ),
    # path('product/create/',ProductCreateView.as_view(), name='product_create' ),
    # path('product/<slug:slug>/',ProductDetail.as_view(), name='products_detail' ),

    # product Variation URL
    path('product/variation/create/',ProductVariationCreate.as_view()),
    path('product/variation/view/<int:pk>/',ProductVariationSingleView.as_view()),
    path('product/variation/update/<int:pk>/',ProductVariationSingle_updateView.as_view()),
    path('product/variation/delete/<int:pk>/',ProductVariation_DeleteView.as_view()),
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

urlpatterns_slider = [ 
    path('slider/',SliderListView.as_view()),
    path('slider/create/',SliderCreateView.as_view()),
    path('slider/view/<int:pk>/', SliderSingleView.as_view()),
    path('slider/update/<int:pk>/',SliderEditView.as_view()),
    path('slider/delete/<int:pk>/',SliderDeleteView.as_view()),
]

urlpatterns_attribute = [
    path('color/',ColorVariationListAPIview.as_view()),
    path('color/<int:pk>/',ColorVariationSingleAPIview.as_view()),
    
    path('size/',SizeVariationListAPIview.as_view()),
    path('size/<int:pk>/',SizeVariationSingleAPIview.as_view()),

    path('weight/',WeightVariationListAPIview.as_view()),
    path('weight/<int:pk>/',WeightVariationSingleAPIview.as_view())
]


urlpatterns += urlpatterns_attribute
urlpatterns += urlpatterns_category
urlpatterns += urlpatterns_product
urlpatterns += urlpatterns_brand_countries
urlpatterns += urlpatterns_productsReview
urlpatterns += urlpatterns_slider