'''
API end point of APP filter
'''
from rest_framework import serializers

# imporing models 
from products.database.products import Products

from products.database.init_p import (
    Brand, Categories, Countreies
)


# Products API ENDpoint 
class ProductsAPI(serializers.ModelSerializer):
    # custom fields for naming 
    brand = serializers.SlugRelatedField(queryset = Brand.objects.all(),
        slug_field='name')
    country = serializers.SlugRelatedField(queryset = Countreies.objects.all(),
        slug_field='name')
    sub_category = serializers.CharField(source = 'get_sub_category',read_only=True)
    category = serializers.CharField(source='get_category',read_only=True)

    class Meta:
        model = Products
        fields = '__all__'
        
        
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