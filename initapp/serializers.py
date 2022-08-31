
from .models import ContactUs
from rest_framework import serializers

class ContactUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields =  ['email','personName','subject','c_message']