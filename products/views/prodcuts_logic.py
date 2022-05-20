
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FileUploadParser,FormParser
from utils.util import *
from products.database.products import Products,Product_images,ProductAttribute
from products.serializers import *
'''
Products
produts attribute 
images 
'''


#ProductsView
class ProductListViewSet(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
   
class ProductCreateView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request,format=None):
        data = request.data
        serializer = ProductsSerializers(data=data)
        
        if serializer.is_valid():
            X =  serializer.save()
            product_images = dict((request.data).lists())['product_image']
            for image in product_images:
                modified_data = Util.modify_input_for_multiple_files(image)
                file_serializer = Product_imagesSerializer(data=modified_data)
                if file_serializer.is_valid():
                    file_serializer.save(product=X)
                
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductRetUpDesViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    lookup_field = 'slug'