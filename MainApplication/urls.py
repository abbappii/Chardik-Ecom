
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



'''
IN THIS SECTION , we are overwritng the Django default title, header and index title 
'''
### Admin panel Configure 
admin.site.site_header = "Chardike Super Admin Panel"
admin.site.site_title = "Chardike Backend"
admin.site.index_title = "Welcome to Chardike Super Admin Panel"

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
    path('order/',include('orders.urls')),
    path('user/', include('accounts.urls')),
    path('queries/',include('appFilter.urls')),
    path('record/',include('inventory.urls')),
    path('contact/', include('initapp.urls')),
    path('blog/', include('blog.urls')),
    path('courier/', include('courier.urls')),
    path('pointsofsale/',include('pointsofsale_manager.urls')),
    path('flash-sale/',include('flash_sale.urls')),
    path('revenue/',include('revenue.urls')),
    path('payment/',include('payment.urls')),
    
    # configure the redoc setup
     #  path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Configuration of Rest Framework Token
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]


urlpatterns+= staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
