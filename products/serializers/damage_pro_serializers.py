

from rest_framework import serializers

from products.database.damage_products import DamageProducts

'''
damage products
        - list 
        - single view 
'''
class DamageProductsAPI(serializers.ModelSerializer):
    class Meta:
        model = DamageProducts
        fields = [
            'id',
            'ref',
            'outlet',
            'date',
            'responsible_person',
            'products_ids',
            'total_loss',
            'description',
            'created_at',
            'updated_at',
            'is_active'
        ]
        depth = 2



'''
damage products
        - create 
        - update
'''
class DamageProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = DamageProducts
        fields = [
            'id',
            'ref',
            'outlet',
            'date',
            'responsible_person',
            'products_ids',
            'total_loss',
            'description'
        ]