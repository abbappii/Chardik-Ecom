'''
This file contains the Business logics of the followings 

- Product (Create , Update , view , Delete)
- Products Attribute (Create , Update , view , Delete)
- Product Images (Create , Update , view , Delete)
'''
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FileUploadParser,FormParser
from utils.util import *
# from products.database.products import Products, Variation_with_Price_variant 
from products.serializers.init_serializers import *
from products.serializers.product_serializers import (
    ProductsSerializers,Product_imagesSerializer,ProductListAPI
)
 

#ProductsView

class ProductListViewSet(generics.ListAPIView):
    queryset = Products.objects.prefetch_related('product_image','reviews').\
        exclude(flash_product__is_active=True)
    serializer_class = ProductListAPI



class ProductCreateView(GenericAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers


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
    # lookup_field = 'slug'


## Product Single View 
class ProductSingleView(generics.RetrieveAPIView):
    queryset = Products.objects.prefetch_related('product_image','reviews')
    serializer_class = ProductListAPI

# rendrer html form 
# class ProductListViewSet(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'products/product_list.html'

#     def get(self, request):
#         queryset = Products.objects.all()
#         return Response({'products': queryset})



# class ProductListViewSet(generics.ListAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializers
   
# class ProductCreateView(APIView):
#     parser_classes = (MultiPartParser, FormParser)
 
#     def post(self, request,format=None):
#         data = request.data
#         serializer = ProductsSerializers(data=data)
        
#         if serializer.is_valid():
#             X =  serializer.save()
#             product_images = dict((request.data).lists())['product_image']
#             for image in product_images:
#                 modified_data = Util.modify_input_for_multiple_files(image)
#                 file_serializer = Product_imagesSerializer(data=modified_data)
#                 if file_serializer.is_valid():
#                     file_serializer.save(product=X)

#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class ProductRetUpDesViewSet(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializers
#     lookup_field = 'slug'


# class ProductDetail(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'products/product_detail.html'

#     def get(self, request, slug):
#         product = get_object_or_404(Products, slug=slug)
#         serializer = ProductsSerializers(product)
#         return Response({'serializer': serializer, 'profile': product})

#     def post(self, request, slug):
#         product = get_object_or_404(Products, slug=slug)
#         serializer = ProductsSerializers(product, data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer, 'product': product})
#         serializer.save()
#         return redirect('products')


'''
Product Variation API
    - Create
    - Update
    - Delete
    - Single View
'''


# # Product Variation Create
# class ProductVariationCreate(generics.CreateAPIView):
#     queryset = Variation_with_Price_variant.objects.all()
#     serializer_class = VariationAPI


# # product Variation Retrieve
# class ProductVariationSingleView(generics.RetrieveAPIView):
#     queryset = Variation_with_Price_variant.objects.all()
#     serializer_class = VariationListAPI


# # Product Variation delete
# class ProductVariationSingle_updateView(generics.UpdateAPIView):
#     queryset = Variation_with_Price_variant.objects.all()
#     serializer_class = VariationAPI


# # Product Delete View
# class ProductVariation_DeleteView(generics.DestroyAPIView):
#     queryset = Variation_with_Price_variant.objects.all()
#     serializer_class = VariationListAPI

# class ProductVariationList(generics.ListAPIView):
#     queryset = Variation_with_Price_variant.objects.all()
#     serializer_class = VariationListAPI





