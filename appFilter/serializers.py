'''
API end point of APP filter
'''
from rest_framework import serializers

# imporing models 
from products.database.products import Products
from products.database.init import (
    Brand, Countreies
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
        