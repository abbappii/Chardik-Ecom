

from inventory.bank_model.baccounts import Name, Outlet

from rest_framework import serializers

class NameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ['id','title']
    
class OutletSerializers(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = ['id','name']
        