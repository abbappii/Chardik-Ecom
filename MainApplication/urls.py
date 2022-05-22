
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('coupon/',include('orders.urls'))
]


urlpatterns+= staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
