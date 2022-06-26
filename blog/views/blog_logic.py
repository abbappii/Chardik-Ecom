
'''
This file contains blog logic
'''

from rest_framework import generics
from blog.database.blog import Blog
from blog.serializers.blog_serializers import BlogSerializers

'''
    Blog logics
        - ListView
        - Single view
        - Update View
        - Delete view
'''

# Blog ListView
class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers

# Blog single View 
class BlogSingleView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers

# Blog update view 
class BlogUpdateView(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers

# Blog delete view 
class BlogDeleteView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers

