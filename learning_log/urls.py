from django.contrib import admin
from django.urls import path, include

# Use static() to add URL mapping to serve static files during development (only)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls')), 
    path('accounts/', include('django.contrib.auth.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)