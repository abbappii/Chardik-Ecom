
'''
This file contains of 
    - Slider view functions
    - Logics 
'''
from products.database.slider import Slider
from products.serializers.init_serializers import SliderSerializers

from rest_framework import generics

'''
Slider Logics 
    - List view
    - Single view
    - Create view
    - Update view
    - Delete view
'''

# list view 
class SliderListView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializers

# single view 
class SliderSingleView(generics.RetrieveAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializers


#  Create View 
class SliderCreateView(generics.CreateAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializers


# delete View 
class SliderDeleteView(generics.DestroyAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializers


# Single Edit View 
class SliderEditView(generics.UpdateAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializers