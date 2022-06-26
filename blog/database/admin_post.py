from tabnanny import verbose
from django.db import models
from accounts.models.initials import InitModels

class AdminBlog(InitModels):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE,related_name='user_admin')
    
    title = models.CharField(max_length=200,blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_admin',blank = True)
    
    url_field = models.URLField(max_length=400,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'AdminBlogs'
        ordering = ['-created_at']
    



