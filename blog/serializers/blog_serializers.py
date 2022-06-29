
from blog.database.blog import Blog

from rest_framework import serializers

class BlogSerializers(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id','title','description','image','url_field']
    