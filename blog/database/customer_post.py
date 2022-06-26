from django.db import models
from accounts.models.initials import InitModels

class CustomerBlog(InitModels):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='post_author')
    title = models.CharField(max_length=200,blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_admin',blank = True)
    
    url_field = models.URLField(max_length=400,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'CustomerBlogs'
        ordering = ['-created_at']
    