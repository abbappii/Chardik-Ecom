
from blog.database.blog import Blog

from rest_framework import serializers

'''
blog
    - create 
    - update
'''
class BlogSerializers(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id','title','description','image','url_field','created_at','updated_at']


'''
blog list api
'''
class BlogListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id',
                'title',
                'description',
                'image',
                'url_field',
                'created_at',
                'updated_at',

                'user_profile_image',
                'user_full_name'
            ]

        # depth = 1   