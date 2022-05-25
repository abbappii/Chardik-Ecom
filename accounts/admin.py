
from django.contrib import admin
from accounts.models.user_model import (
    User, Profile
)


admin.site.register(User)
admin.site.register(Profile)
