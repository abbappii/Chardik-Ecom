
'''
This file contains blog logic
'''

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.generics import GenericAPIView
from blog.database.blog import Blog
from blog.serializers.blog_serializers import BlogSerializers
# importing Permission
from MainApplication.scripts.permission import(
    IsAdmin,
    IsCustomer,
)

'''
    Blog logics
        - ListView
        - Single view
        - Update View
        - Delete view
'''

# @permission_classes([IsAdmin|IsCustomer])
class BlogCreateView(GenericAPIView):
    permission_classes = [IsAdmin|IsCustomer]
    queryset = Blog.objects.filter(is_active=True)
    serializer_class = BlogSerializers

    # def get(self,request):
    #     # print(request.user.profile.get_permission_id)
    #     return Response({'hello':'hey'})

    def post(self,request):
        # print(request.user)
        user = request.user.profile

        fetchUser = Blog(user=user)
        apifetch = BlogSerializers(fetchUser,data=request.data)
        if apifetch.is_valid():
            
            apifetch.save()
            return Response(apifetch.data)
        else:
            return Response(
                {'Error':'Blog not saved'},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )

# Blog ListView
class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.filter(is_active=True)
    serializer_class = BlogSerializers

# Blog single View 
class BlogSingleView(generics.RetrieveAPIView):
    queryset = Blog.objects.filter(is_active=True)
    serializer_class = BlogSerializers

# Blog update view 
class BlogUpdateView(generics.UpdateAPIView):
    queryset = Blog.objects.filter(is_active=True)
    serializer_class = BlogSerializers

# Blog delete view 
class BlogDeleteView(generics.DestroyAPIView):
    queryset = Blog.objects.filter(is_active=True)
    serializer_class = BlogSerializers


## Blog List View admin
class AdminBlogListView(generics.ListAPIView):
    queryset = Blog.objects.filter(is_active=True,is_admin=True)
    serializer_class = BlogSerializers

## Blog List view Customer 
class CustomerBlogListView(generics.ListAPIView):
    queryset = Blog.objects.filter(is_active=True,is_customer=True)
    serializer_class = BlogSerializers