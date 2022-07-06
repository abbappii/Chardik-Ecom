'''
API end point of APP filter
'''
from rest_framework import serializers

# imporing models 
from products.database.products import Products

from products.database.init_p import (
    Brand, Categories, Countreies
)

# importing serializer 
from products.serializers.product_serializers import (
    CategoriesSerializers,
    SubCategoriesListSerializers,
    VariationListAPI,
    Product_imagesSerializer,
    ProductReviewListAPI
)


# Products API ENDpoint 
class ProductsAPI(serializers.ModelSerializer):
    # add name fields views
    # sub_category = serializers.CharField(source = 'get_sub_category',read_only=True)
    # category = serializers.CharField(source='get_category',read_only=True)
    category=CategoriesSerializers(many=True, read_only=True)
    sub_category=SubCategoriesListSerializers(many=True, read_only=True)
    #brand=BrandSerializer(many=True, read_only=True)
    #country=CountriesSerializer(many=True, read_only=True)
    variant = VariationListAPI(many=True)
    product_image = Product_imagesSerializer(many=True)
    reviews = ProductReviewListAPI(many=True)

    class Meta:
        model = Products
        fields = ['id','brand','country','sku',
                    'category','sub_category','product_name',
                    'slug','meta','short_descriptions',
                    'long_description','alter_text',
                    'feature_image','product_image','sold_count','expire_rate',
                    'is_stock','variant','reviews']
        depth = 1

                    
        
# Category API ENDpoint
# show products under 
class CategoryBaseProductsAPI(serializers.ModelSerializer):
    Category_products = ProductsAPI(many=True)
    class Meta:
        model = Categories
        fields = ['id','category_name','Category_products']


# Brand Api Endpoint
class BranBasedApi(serializers.ModelSerializer):
    brand = ProductsAPI(many=True)
    class Meta:
        model = Brand
        fields = ['id','name','description','brand']


# Countries API EndPoint
class CountryBaseAPI(serializers.ModelSerializer):
    country = ProductsAPI(many=True)
    class Meta:
        model = Countreies
        fields = ['id','name','country']