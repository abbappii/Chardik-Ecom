
from django.contrib import admin
from accounts.models.user_model import (
    User, Profile
)
# Register your models here.

admin.site.register(User)
admin.site.register(Profile)
