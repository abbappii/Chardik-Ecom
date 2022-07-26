

from inventory.bank_model.baccounts import Name, Outlet

from rest_framework import serializers

'''
Name of expence 
        - create 
        - update 
'''
class NameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ['id','title']
    
# list api serializer 
class NameListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = '__all__'
        depth=1

'''
Outlet  
        - create 
        - update 
'''
class OutletSerializers(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = ['id','name']
        
    
# outlet api serializer 
class OutletListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = '__all__'
        depth=1