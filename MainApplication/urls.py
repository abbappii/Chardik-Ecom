
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.conf import settings

# Third party app Url  

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# simple JWT URL
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    
)


schema_view = get_schema_view(
   openapi.Info(
      title="Ecommerce API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.charidik.herokuapp.com/policies/terms/",
      contact=openapi.Contact(email="contact@test.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('coupon/',include('orders.urls')),
    path('user/', include('accounts.urls')),
    path('queries/',include('appFilter.urls')),

    # Configuration of Rest Framework Token
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]


urlpatterns+= staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
