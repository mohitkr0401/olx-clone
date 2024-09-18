from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('products/', include('product.urls', namespace='products')),
    path('login/', include('login.urls', namespace='login')),
    path('sell/', include('sell.urls', namespace='sell')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
if settings.DEBUG:  # Add static file serving in debug mode
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
