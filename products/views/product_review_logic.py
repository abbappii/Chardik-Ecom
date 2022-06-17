
from rest_framework import generics
from products.database.reviews import ProductReview
from products.serializers.init_serializers import ProductReviewSerailizers

# Review list view 
class ProducReviewtListView(generics.ListAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerailizers


# review createview 
class ProductReviewCreateView(generics.CreateAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerailizers

# product single retrieve view 

class ProductReviewRetrieveView(generics.RetrieveAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerailizers

# product editview 
class ProductReviewEditView(generics.UpdateAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerailizers

# product delete view 
class ProductReviewDeleteView(generics.DestroyAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerailizers