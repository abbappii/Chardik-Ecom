
from .models import ContactUs
from rest_framework import serializers

class ContactUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'