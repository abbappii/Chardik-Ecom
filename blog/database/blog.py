from django.db import models
from accounts.models.initials import InitModels

class Blog(InitModels):

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, 
        related_name='post_author')
    title = models.CharField(max_length=200,blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_admin',blank = True)
    
    url_field = models.URLField(max_length=400,blank=True)

    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Blog'
        ordering = ['-created_at']
    

    # custom property 
    @property
    def user_profile_image(self):
        # profile picture get
        if self.user.profile.profile_picture:
            return self.user.profile.profile_picture.url
        else:
            return ''

    @property
    def user_full_name(self):
        # full name get 
        if self.user.profile.full_name:
            return self.user.profile.full_name
        else:
            return ""